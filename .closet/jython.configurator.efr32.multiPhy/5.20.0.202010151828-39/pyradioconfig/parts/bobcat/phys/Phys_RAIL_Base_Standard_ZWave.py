from pyradioconfig.parts.ocelot.phys.Phys_RAIL_Base_Standard_ZWave import PHYS_ZWave_Ocelot
from py_2_and_3_compatibility import *

class PHYS_ZWave_Bobcat(PHYS_ZWave_Ocelot):

    def PHY_ZWave_100kbps_912MHz_OQPSK(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='PHY_ZWave_100kbps_912MHz_OQPSK for Bobcat', phy_name=phy_name)
        phy.profile_inputs.antdivmode.value = model.vars.antdivmode.var_enum.DISABLE
        self.ZWave_100kbps_912MHz_OQPSK(phy, model)

        # Forcing to VCODIV HALFRATE for Bobcat
        model.vars.adc_clock_mode.value_forced = model.vars.adc_clock_mode.var_enum.VCODIV
        model.vars.adc_rate_mode.value_forced = model.vars.adc_rate_mode.var_enum.HALFRATE

        # FIXME - added for enabling dynamic frame control
        phy.profile_inputs.var_length_numbits.value = 8
        phy.profile_inputs.var_length_includecrc.value = True
        phy.profile_outputs.FRC_WCNTCMP1_LENGTHFIELDLOC.override = 7

        # Overrides for the SQ block
        phy.profile_outputs.MODEM_SQ_SQEN.override = 1
        T_b = 1.25e-6
        phy.profile_outputs.MODEM_SQ_SQTIMOUT.override = int(250e-6 / T_b)  # Timeout before checking for timing detect. Units: T_b. Zwave_LR_timing_21.xlsx:I13
        phy.profile_outputs.MODEM_SQEXT_SQSTG2TIMOUT.override = int(3.2e-3 / T_b) # Timeout after timing detect to check for preamble. Units T_b.
        phy.profile_outputs.MODEM_SQEXT_SQSTG3TIMOUT.override = 16 * 8 # Timeout after preamble to check for sync word. Units T_b. Cell B25

        # Reduce HICNTREGINON0 to speed up AGC when near upper threshold
        phy.profile_outputs.AGC_HICNTREGION0_HICNTREGION0.override = 10
        phy.profile_outputs.AGC_STEPDWN_STEPDWN0.override = 1
        phy.profile_outputs.AGC_STEPDWN_STEPDWN1.override = 2
        phy.profile_outputs.AGC_STEPDWN_STEPDWN2.override = 3
        phy.profile_outputs.AGC_STEPDWN_STEPDWN3.override = 4
        phy.profile_outputs.AGC_STEPDWN_STEPDWN4.override = 5
        phy.profile_outputs.AGC_STEPDWN_STEPDWN5.override = 6

        # Increase threshold and delay to reduce false detections
        phy.profile_outputs.MODEM_COH3_DYNIIRCOEFOPTION.override = 1
        phy.profile_outputs.MODEM_COH2_FIXEDCDTHFORIIR.override = 140
        phy.profile_outputs.MODEM_LONGRANGE6_LRSPIKETHD.override = 140
        phy.profile_outputs.AGC_GAINSTEPLIM0_CFLOOPDEL.override = 127

        # Disable TX side AFC adjustments.
        phy.profile_outputs.MODEM_AFCADJTX_AFCSCALEM.override = 0
        phy.profile_outputs.MODEM_AFCADJTX_AFCSCALEE.override = 0

        return phy

    def PHY_ZWave_100kbps_912MHz_OQPSK_beam(self, model, phy_name=None):
        pass

    def PHY_ZWave_100kbps_916MHz(self, model, phy_name=None):
        pass

    def PHY_ZWave_100kbps_916MHz_DSA_Beam_Passthrough(self, model):
        pass

    def PHY_ZWave_100kbps_916MHz_DSA_Beam_Passthrough_lowside(self, model):
        pass

    def PHY_ZWave_100kbps_916MHz_lowside(self, model, phy_name=None):
        pass

    def PHY_ZWave_100kbps_916MHz_viterbi(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='PHY_ZWave_100kbps_916MHz_viterbi for Bobcat', phy_name=phy_name)
        self.ZWave_100kbps_base(phy, model)

        # Forcing to VCODIV HALFRATE for Bobcat
        model.vars.adc_clock_mode.value_forced = model.vars.adc_clock_mode.var_enum.VCODIV
        model.vars.adc_rate_mode.value_forced = model.vars.adc_rate_mode.var_enum.HALFRATE

        phy.profile_inputs.xtal_frequency_hz.value = 39000000
        # phy.profile_inputs.rx_xtal_error_ppm.value = 20
        # phy.profile_inputs.tx_xtal_error_ppm.value = 20

        phy.profile_inputs.demod_select.value = model.vars.demod_select.var_enum.TRECS_SLICER
        phy.profile_inputs.base_frequency_hz.value = long(916000000)

        phy.profile_inputs.symbols_in_timing_window.value = 12
        phy.profile_inputs.syncword_0.value = long(0x55F0)
        phy.profile_inputs.syncword_length.value = 16
        # sync word is 8 bits, rest are taken from the preamble.
        phy.profile_inputs.preamble_length.value = phy.profile_inputs.preamble_length.value -  phy.profile_inputs.syncword_length.value + 8
        phy.profile_inputs.symbols_in_timing_window.value = 12

        phy.profile_outputs.MODEM_TRECPMPATT_PMEXPECTPATT.override = long(2863311530)
        phy.profile_outputs.MODEM_TRECPMDET_PMMINCOSTTHD.override = 200

        phy.profile_outputs.MODEM_VTCORRCFG1_KSI3SWENABLE.override = 1
#        phy.profile_outputs.MODEM_VTCORRCFG1_VITERBIKSI3WB.override = 44
#        phy.profile_outputs.MODEM_VITERBIDEMOD_VITERBIKSI3.override = 42

        # forcing wider bw_acq to improve freq offset performance
        phy.profile_inputs.bandwidth_hz.value = 210000

        # Overrides for the SQ block
        phy.profile_outputs.MODEM_SQ_SQEN.override = 1
        phy.profile_outputs.MODEM_SQ_SQTIMOUT.override = int(250 / 10)  # Timeout before checking for timing detect. Units: T_b.
        phy.profile_outputs.MODEM_SQEXT_SQSTG2TIMOUT.override = phy.profile_inputs.preamble_length.value - (phy.profile_inputs.syncword_length.value - 8)
        phy.profile_outputs.MODEM_SQEXT_SQSTG3TIMOUT.override = phy.profile_inputs.syncword_length.value +16

        # Reduce HICNTREGINON0 to speed up AGC when near upper threshold
        phy.profile_outputs.AGC_HICNTREGION0_HICNTREGION0.override = 10

        # Disable TX side AFC adjustments.
        phy.profile_outputs.MODEM_AFCADJTX_AFCSCALEM.override = 0
        phy.profile_outputs.MODEM_AFCADJTX_AFCSCALEE.override = 0

        phy.profile_outputs.AGC_STEPDWN_STEPDWN0.override = 1
        phy.profile_outputs.AGC_STEPDWN_STEPDWN1.override = 2
        phy.profile_outputs.AGC_STEPDWN_STEPDWN2.override = 3
        phy.profile_outputs.AGC_STEPDWN_STEPDWN3.override = 4
        phy.profile_outputs.AGC_STEPDWN_STEPDWN4.override = 5
        phy.profile_outputs.AGC_STEPDWN_STEPDWN5.override = 6

        phy.profile_outputs.MODEM_PHDMODCTRL_REMODEN.override = 0
        phy.profile_outputs.MODEM_PHDMODCTRL_REMODDWN.override = 0

        phy.profile_outputs.MODEM_TRECPMDET_PMCOSTVALTHD.override = 2

        return phy

    def PHY_ZWave_100kbps_916MHz_viterbi_beam(self, model, phy_name=None):
        pass

    def PHY_ZWave_100kbps_916MHz_viterbi_lowside(self, model, phy_name=None):
        pass

    def PHY_ZWave_100kbps_916MHz_viterbi_lowside_beam(self, model, phy_name=None):
        pass

    def PHY_ZWave_40kbps_908MHz(self, model, phy_name=None):
        pass

    def PHY_ZWave_40kbps_908MHz_viterbi(self, model, phy_name=None):
        pass

    def PHY_ZWave_40kbps_908MHz_viterbi_beam(self, model, phy_name=None):
        pass

    def PHY_ZWave_40kbps_9p6kbps_908MHz_viterbi_conc(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, 'PHY_ZWave_40kbps_9p6kbps_908MHz_viterbi_conc on Bobcat')
        self.ZWave_40kbps_908MHz_viterbi_base(phy, model)
        self.ZWave_9p6kbps_908MHz_bcr_conc_base(phy, model)

        # RAIL overrides the RF to the correct region frequency and concurrent frequency
        # This concurrent PHY from the calculator transmits and receives on the standard R2 RF.
        phy.profile_inputs.base_frequency_hz.value = long(908400000)

        # FULLRATE needed to find DFE configuration (allowing bwsel_max=0.5 is alternate for Halfrate)
        model.vars.adc_clock_mode.value_forced = model.vars.adc_clock_mode.var_enum.VCODIV
        model.vars.adc_rate_mode.value_forced = model.vars.adc_rate_mode.var_enum.FULLRATE

        phy.profile_outputs.MODEM_PHDMODCTRL_BCRTRECSCONC.override = 1
        phy.profile_outputs.MODEM_FRMSCHTIME_DSARSTSYCNEN.override = 1 # Needed for concurrent demod for PGOCELOT-5282

        # Overrides for the SQ block
        phy.profile_outputs.MODEM_SQ_SQEN.override = 1
        phy.profile_outputs.MODEM_SQ_SQTIMOUT.override = int(1800 / 25) # Timeout before checking for timing detect. Units: T_b.
        phy.profile_outputs.MODEM_SQEXT_SQSTG2TIMOUT.override = 80 # Timeout after timing detect to check for preamble. Units T_b.
        phy.profile_outputs.MODEM_SQEXT_SQSTG3TIMOUT.override = 16 # Timeout after preamble to check for sync word. Units T_b.
        phy.profile_outputs.MODEM_TRECPMDET_PMCOSTVALTHD.override = 2

        return phy

    def PHY_ZWave_9p6kbps_908MHz(self, model, phy_name=None):
        pass

    def PHY_ZWave_9p6kbps_908MHz_bcr(self, model, phy_name=None):
        pass

    def PHY_ZWave_9p6kbps_908MHz_bcr_conc(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, 'PHY_ZWave_40kbps_9p6kbps_908MHz_viterbi_conc on Bobcat')
        self.ZWave_40kbps_908MHz_viterbi_base(phy, model)
        self.ZWave_9p6kbps_908MHz_bcr_conc_base(phy, model)

        # RAIL overrides the RF to the correct region frequency and concurrent frequency
        # This concurrent PHY from the calculator transmits and receives on the standard R1 RF.
        phy.profile_inputs.base_frequency_hz.value = long(908420000)

        # FULLRATE needed to find DFE configuration (allowing bwsel_max=0.5 is alternate for Halfrate)
        model.vars.adc_clock_mode.value_forced = model.vars.adc_clock_mode.var_enum.VCODIV
        model.vars.adc_rate_mode.value_forced = model.vars.adc_rate_mode.var_enum.FULLRATE

        # overrides from PHY_ZWave_40kbps_9p6kbps_908MHz_viterbi_conc to convert to 9.6kbps
        phy.profile_inputs.preamble_pattern.value = 6
        phy.profile_inputs.preamble_pattern_len.value = 4
        phy.profile_inputs.preamble_length.value = 160
        phy.profile_outputs.MODEM_PHDMODCTRL_BCRTRECSCONC.override = 1
        phy.profile_outputs.MODEM_FRMSCHTIME_DSARSTSYCNEN.override = 1 # Needed for concurrent demod for PGOCELOT-5282
        phy.profile_outputs.MODEM_SQ_SQEN.override = 1
        phy.profile_outputs.MODEM_SQ_SQTIMOUT.override = int(1800 / 25) # Timeout before checking for timing detect. Units: T_b.
        phy.profile_outputs.MODEM_SQEXT_SQSTG2TIMOUT.override = 160 # Timeout before checking for preamble in chips
        phy.profile_outputs.MODEM_SQEXT_SQSTG3TIMOUT.override = 16 # Timeout after preamble to check for sync word. Units T_b.

        # for registers to get BCR demod to work properly
        phy.profile_outputs.MODEM_SRCCHF_SRCENABLE2.override = 0
        phy.profile_outputs.MODEM_MODINDEX_MODINDEXM.override = 26
        phy.profile_outputs.MODEM_TXBR_TXBRDEN.override = 128
        phy.profile_outputs.MODEM_TXBR_TXBRNUM.override = 32500
        phy.profile_outputs.MODEM_BCRDEMODCTRL_BBPMDETEN.override = 1
        phy.profile_outputs.MODEM_TRECPMPATT_PMEXPECTPATT.override = 0x33333333
        phy.profile_outputs.MODEM_SRCCHF_SRCENABLE2.override = 0
        phy.profile_outputs.MODEM_CTRL0_CODING.override = 1
        phy.profile_outputs.MODEM_CTRL1_SYNCBITS.override = 31
        phy.profile_outputs.MODEM_SYNC0_SYNC0.override = 0xAA556666
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0

        # force the following to keep register differences between PHY_ZWave_40kbps_9p6kbps_908MHz_viterbi_conc and
        # this phy at minimum. not required for proper function - add/remove/modify these as the other PHY changes
        # Diffing between the two concurrent PHYs should only have registers diffs in
        # {MODEM_BCRDEMODCTRL_BBPMDETEN, MODEM_CTRL0_CODING, MODEM_CTRL0_MAPFSK, MODEL_CTRL1_SYNCBITS, MODEM_FRMSCHTIME_FRMSCHTIME,
        # MODEM_PRE_{BASE,BASEBITS,TXBASES}, MODEM_SRCCHF.SRCENABLE2, MODEM_SYNC0_SYNC0, MODEM_TIMING_TIMINGBASES, MODEM_TRECPMPATT_PMEXPECTPATT, MODEM_TXBR, SYNTH_FREQ}
        phy.profile_outputs.AGC_CTRL7_SUBDEN.override = 0
        phy.profile_outputs.AGC_CTRL7_SUBINT.override = 0
        phy.profile_outputs.AGC_CTRL7_SUBNUM.override = 0
        phy.profile_outputs.AGC_CTRL7_SUBPERIOD.override = 0
        phy.profile_outputs.MODEM_AFC_AFCDEL.override = 5
        phy.profile_outputs.MODEM_MODINDEX_FREQGAINE.override = 1
        phy.profile_outputs.MODEM_MODINDEX_FREQGAINM.override = 1
        phy.profile_outputs.MODEM_PHDMODCTRL_REMODOSR.override = 6
        phy.profile_outputs.MODEM_RXBR_RXBRINT.override = 3
        phy.profile_outputs.MODEM_REALTIMCFE_MINCOSTTHD.override = 300
        phy.profile_outputs.MODEM_REALTIMCFE_SYNCACQWIN.override = 3
        phy.profile_outputs.MODEM_VTCORRCFG0_EXPECTPATT.override = 2853175295
        phy.profile_outputs.MODEM_VTCORRCFG1_EXPSYNCLEN.override = 142
        phy.profile_outputs.MODEM_VTCORRCFG1_EXPECTHT.override = 11

        phy.profile_outputs.MODEM_BCRCTRL0_CRSLOW.override = 2
        phy.profile_outputs.MODEM_BCRDEMODARR0_SCHPRDHI.override = 0

        phy.profile_outputs.MODEM_AFCADJRX_AFCSCALEE.override = 1
        phy.profile_outputs.MODEM_AFCADJRX_AFCSCALEM.override = 25
        phy.profile_outputs.MODEM_BCRDEMODCTRL_PREATH.override = 20

        return phy

    def PHY_ZWave_9p6kbps_908MHz_viterbi(self, model, phy_name=None):
        pass
