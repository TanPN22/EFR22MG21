from .pro2plusdemodulatorcore import Pro2PlusDemodulatorCore
from .pro2_ocelotmodemfields import Pro2OcelotDemodulatorFields
from .decode_api import engfsk,en2fsk,en4gfsk,enook
from .trueround import trueround
import math

class Pro2OcelotDemodulatorCore(Pro2PlusDemodulatorCore):

    def __init__(self):
        self.fields = Pro2OcelotDemodulatorFields()
        self._init_decim_table()

    def _calc_step_1(self, modem_calc):

        #  BCR loop & raw data mode register
        # sampling rate of CH filter
        ###CRW Modified for BCR DEMOD in Ocelot###
        self.Fs_rx_CH = modem_calc.inputs.API_Fs_rx_CH

        ###From Pro2 Calculator###
        # CH filter's OSR: # OSR_rx_CH = Fs_rx_CH/API_Rsymb;
        self.OSR_rx_CH = self.Fs_rx_CH / modem_calc.inputs.API_Rsymb
        # Calculate ndec0 in data filter
        if (enook(modem_calc.inputs.API_modulation_type)):  # OOK
            self.fields.ndec0 = math.floor(
                math.log(self.OSR_rx_CH / self.OOKminOSR, 2))  # make OSR >= 7 (#define self.OOKminOSR)
            # if (self.fields.ndec0 < 0):
            #     modem_calc.calc_log.add_to_log(
            #         '# Error: OOK filter BW is too small for the data rate. Please increase OOK_BW and try again.\n',
            #         True)
            self.fields.ndec0 = min(5, max(self.fields.ndec0, 0))  # limit to [1,5] for OOK!

            if (modem_calc.inputs.API_OSRtune < 0):
                modem_calc.warning2log += '# In OOK mode, OSR step down is prohibited. API_OSRtune is reset to 0 \n'
            #                 print(('CALC:input:OSRtune', 'In OOK mode, OSR step down is prohibited. API_OSRtune is reset to 0 '))
            else:  # >0
                Nndec0 = self.fields.ndec0 - modem_calc.inputs.API_OSRtune
                if (Nndec0 < 0):
                    newOSRt = self.fields.ndec0 - 1
                    self.fields.ndec0 = 1
                    modem_calc.warning2log += '# No room to step up BCR OSR by {} steps, instead OSRtune={} steps is applied \n'.format(
                        modem_calc.inputs.API_OSRtune, newOSRt)
                #                     print(('CALC:input:OSRtune', ' No room to step up BCR OSR by {} steps, instead OSRtune={} steps is applied'.format(modem_calc.inputs.API_OSRtune, newOSRt)))
                else:
                    self.fields.ndec0 = Nndec0
        else:  # FSK
            # during revB0 EZR2 eval we found self.ndec0>0 yields better performance in (G)FSK if
            # (self.fields.hModInd>=2 & OSR/H >=8) target OSR=24 ==>96 to improve BER at 2.4kbps hi-band
            OSR_per_h = self.OSR_rx_CH / self.fields.hModInd
            if (self.fields.hModInd >= 2 and not (enook(modem_calc.inputs.API_modulation_type)) and OSR_per_h >= 8):
                self.fields.ndec0 = max(min(5, trueround(math.log(self.OSR_rx_CH / 96, 2))),
                                        0)  # target OSR=24 =>96
            else:
                self.fields.ndec0 = 0  # originally self.ndec0=0 for FSK

        ###From Pro2+ Calculator###
        self.raw_diff = self.gaussain_factor * 64 * self.max_hModInd / self.OSR_rx_CH
        self.fields.rawflt_sel = 0  # 0=8tap MA
        self.raweye_factor = 1.3  # magnified RAWEYE multiple for hi self.fields.hModInd && hi OSR

    def _calc_step_2(self, modem_calc):
        # The peak of MA filter input includes two parts:
        # (1)DC-offset caused by tx-rx freq. error (2) frequency modulation
        peak_ma_in = (128 * self.fields.tx_rx_err / modem_calc.inputs.API_Rsymb / self.OSR_rx_CH) + self.raw_diff

        # Set MA gain to max. and adjust it later
        self.fields.rawgain = 3
        # The peak of MA filter output
        peak_ma_out = self.raweye_factor * peak_ma_in * (8 - 2 * self.fields.rawflt_sel)

        # 4/5/2012: minmax detector BAD with self.ndec0>0
        # force self.ndec0=0 as long as OSR<511 for FSK minmaxdet!! OSR overflow in low Rb /hi BW
        ndec0_opt0 = (self.fields.nonstdpk and self.fields.detector == 3 and not (
            enook(modem_calc.inputs.API_modulation_type)))
        if (ndec0_opt0 and self.OSR_rx_CH > 2 ** 9):
            self.fields.ndec0 = 1  # >511?  osr=ufix12.3

        # if self.ndec0 is used, make sure input of self.ndec0 is not overflow. ndc0_input[8:0] = MA_out[8:0]
        # if self.ndec0 is NOT used, make sure MA[12:0] output is not overflow
        if (self.fields.ndec0 > 0):
            if (peak_ma_out >= 2 ** 8):  # self.rawgain \in {0,1,2,3}
                self.fields.rawgain = min(
                    max(0, self.fields.rawgain - math.ceil((math.log((peak_ma_out / 2 ** 8), 2)))), 3)
        else:
            if (peak_ma_out >= 2 ** 12):
                self.fields.rawgain = min(max(0, self.fields.rawgain - math.ceil(math.log((peak_ma_out / 2 ** 12), 2))),3)

        ###CRW Modified for BCR DEMOD in Ocelot###
        if (enook(modem_calc.inputs.API_modulation_type)):
            tap2ma_gain = 1
        else:
            tap2ma_gain = 4

        self.raw_flt_gain = 16 ** ((self.fields.ndec0 > 0)) * (8 - 4 * self.fields.rawflt_sel) *tap2ma_gain  # 10-bit  in ocelot

        # expected raw data eye-opening
        self.fields.raweye = int(min(trueround(0.5*self.raweye_factor * self.raw_flt_gain * self.raw_diff), 2047))  # 11-bit

    def _calc_step_11(self, modem_calc):
        ###CRW Modified for BCR DEMOD in Ocelot###
        #  AFC Loop GAIN
        self.afc_gain_cal = (2 * modem_calc.inputs.API_Rsymb) / modem_calc.inputs.API_fb_frequency_resolution

        self.afc_adj = 1
        # if (modem_calc.inputs.API_Rsymb >= 100e3):  # 100kbps RX_BW = 206kHz
        #     self.afc_adj = 0
        # else:
        #     self.afc_adj = 1

    def _calc_orig_afclim(self, modem_calc, k_ratio, afc_RX_BW):
        ###CRW Modified for BCR DEMOD in Ocelot###
        # 9/11/2012 afclim to be modified once we know better the formula
        # 15-bit with 0 bit fraction
        orig_afclim = trueround(2 ** 6 * afc_RX_BW * 1000 *
                                (k_ratio + (0.04 - afc_RX_BW / 206 / 100) * self.afc_adj)
                                / self.fields.afc_gain / modem_calc.inputs.API_fb_frequency_resolution)
        return orig_afclim

    def _calc_step_22(self, modem_calc):
        # demodulator SFR register
        # ANT-DIV && ADC reset enable
        self.fields.en_adc_rst = 0
        self.fields.adcwatch = 0
        # if (modem_calc.inputs.API_ant_div==1) :
        #     self.fields.antdiv = 1
        #     if (en4gfsk(modem_calc.inputs.API_modulation_type)) :
        #        self.fields.ant2pm_thd = 15 # default
        #     else :
        #        self.fields.ant2pm_thd = 8 # default
        # else :
        #     self.fields.antdiv = 0
        # In Ocelot, PRO2 legacy ANT-DIV will be disabled
        self.fields.antdiv = 0
        ###CRW Modified for BCR DEMOD in Ocelot###
        if (self.fields.oneshot_afc == 1):
            self.fields.anwait = 0
        else:
            self.fields.anwait = 2

        # jira 1621 & 1218
        #For IF bandwidths >500kHz we will enable the ADC gain correction (MODEM_AGC_CONTROL = 0x02)
        # and the RSSI jump detector will be increased to 9dB.
        #For IF bandwidths <=500kHz we will disable the ADC gain correction (MODEM_AGC_CONTROL = 0x00)
        # and the RSSI jump detector will be increased to 6dB.
        if(self.Ch_Fil_Bw >500):
            self.fields.adc_gain_cor_en = 1
            self.fields.jmpdlylen = 0   # 0: 2Tb; 1: 4Tb
            self.fields.rssijmpthd = 8
        else:
            self.fields.adc_gain_cor_en = 0
            self.fields.jmpdlylen = 0   # Jira SI4440-1769
            self.fields.rssijmpthd = 6

        # jira-1362: set res_lockup_byp in BERT/ API bit in BCR_MISC0 available after revC2
        if (modem_calc.inputs.API_BER_mode==1):
            self.fields.res_lockup_byp = 1  # disable "consecutive diff counter"
            self.fields.enrssijmp = 0       # jira-1621: disable rssi-jump in BERT
        else:
            self.fields.res_lockup_byp = 0
            #if (self.fields.signal_dsa_mode  ==1 and self.fields.afcbd>0 and self.filter_k2>self.filter_k1):
            if (self.fields.enrssijmp==1 and self.fields.afcbd>0 and self.filter_k2>self.filter_k1):
                self.fields.rssijmpthd = 15   # sufficient across filters?