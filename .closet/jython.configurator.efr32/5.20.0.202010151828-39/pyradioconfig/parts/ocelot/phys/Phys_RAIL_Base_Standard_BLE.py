from pyradioconfig.parts.common.phys.phy_common import PHY_COMMON_FRAME_BLE
from pyradioconfig.calculator_model_framework.interfaces.iphy import IPhy
from py_2_and_3_compatibility import *


class PHYS_Bluetooth_LE_Ocelot(IPhy):

    def BLE_TX_Shaping_Coeffs(self, phy, model):
        phy.profile_outputs.MODEM_CTRL0_SHAPING.override = 3
        phy.profile_outputs.MODEM_SHAPING0_COEFF0.override = 0
        phy.profile_outputs.MODEM_SHAPING0_COEFF1.override = 2
        phy.profile_outputs.MODEM_SHAPING0_COEFF2.override = 5
        phy.profile_outputs.MODEM_SHAPING0_COEFF3.override = 14
        phy.profile_outputs.MODEM_SHAPING1_COEFF4.override = 28
        phy.profile_outputs.MODEM_SHAPING1_COEFF5.override = 47
        phy.profile_outputs.MODEM_SHAPING1_COEFF6.override = 67
        phy.profile_outputs.MODEM_SHAPING1_COEFF7.override = 83
        phy.profile_outputs.MODEM_SHAPING2_COEFF8.override = 98
        phy.profile_outputs.MODEM_SHAPING2_COEFF9.override = 105
        phy.profile_outputs.MODEM_SHAPING2_COEFF10.override = 104
        phy.profile_outputs.MODEM_SHAPING2_COEFF11.override = 97
        phy.profile_outputs.MODEM_SHAPING3_COEFF12.override = 85
        phy.profile_outputs.MODEM_SHAPING3_COEFF13.override = 67
        phy.profile_outputs.MODEM_SHAPING3_COEFF14.override = 50
        phy.profile_outputs.MODEM_SHAPING3_COEFF15.override = 4
        phy.profile_outputs.MODEM_SHAPING4_COEFF16.override = 22
        phy.profile_outputs.MODEM_SHAPING4_COEFF17.override = 16
        phy.profile_outputs.MODEM_SHAPING4_COEFF18.override = 14
        phy.profile_outputs.MODEM_SHAPING4_COEFF19.override = 14
        phy.profile_outputs.MODEM_SHAPING5_COEFF20.override = 13
        phy.profile_outputs.MODEM_SHAPING5_COEFF21.override = 12
        phy.profile_outputs.MODEM_SHAPING5_COEFF22.override = 10
        phy.profile_outputs.MODEM_SHAPING5_COEFF23.override = 8
        phy.profile_outputs.MODEM_SHAPING6_COEFF24.override = 7
        phy.profile_outputs.MODEM_SHAPING6_COEFF25.override = 6
        phy.profile_outputs.MODEM_SHAPING6_COEFF26.override = 5
        phy.profile_outputs.MODEM_SHAPING6_COEFF27.override = 4
        phy.profile_outputs.MODEM_SHAPING7_COEFF28.override = 3
        phy.profile_outputs.MODEM_SHAPING7_COEFF29.override = 3
        phy.profile_outputs.MODEM_SHAPING7_COEFF30.override = 2
        phy.profile_outputs.MODEM_SHAPING7_COEFF31.override = 2
        phy.profile_outputs.MODEM_SHAPING8_COEFF32.override = 2
        phy.profile_outputs.MODEM_SHAPING8_COEFF33.override = 1
        phy.profile_outputs.MODEM_SHAPING8_COEFF34.override = 1
        phy.profile_outputs.MODEM_SHAPING8_COEFF35.override = 1
        phy.profile_outputs.MODEM_SHAPING9_COEFF36.override = 1
        phy.profile_outputs.MODEM_SHAPING9_COEFF37.override = 1
        phy.profile_outputs.MODEM_SHAPING9_COEFF38.override = 1
        phy.profile_outputs.MODEM_SHAPING9_COEFF39.override = 0
        phy.profile_outputs.MODEM_SHAPING10_COEFF40.override = 0
        phy.profile_outputs.MODEM_SHAPING10_COEFF41.override = 0
        phy.profile_outputs.MODEM_SHAPING10_COEFF42.override = 0
        phy.profile_outputs.MODEM_SHAPING10_COEFF43.override = 0
        phy.profile_outputs.MODEM_SHAPING11_COEFF44.override = 0
        phy.profile_outputs.MODEM_SHAPING11_COEFF45.override = 0
        phy.profile_outputs.MODEM_SHAPING11_COEFF46.override = 0
        phy.profile_outputs.MODEM_SHAPING11_COEFF47.override = 0

    def BLE_2M_TX_Shaping_Coeffs(self, phy, model):
        phy.profile_outputs.MODEM_CTRL0_SHAPING.override = 3
        phy.profile_outputs.MODEM_SHAPING0_COEFF0.override = 1
        phy.profile_outputs.MODEM_SHAPING0_COEFF1.override = 2
        phy.profile_outputs.MODEM_SHAPING0_COEFF2.override = 7
        phy.profile_outputs.MODEM_SHAPING0_COEFF3.override = 17
        phy.profile_outputs.MODEM_SHAPING1_COEFF4.override = 33
        phy.profile_outputs.MODEM_SHAPING1_COEFF5.override = 55
        phy.profile_outputs.MODEM_SHAPING1_COEFF6.override = 75
        phy.profile_outputs.MODEM_SHAPING1_COEFF7.override = 90
        phy.profile_outputs.MODEM_SHAPING2_COEFF8.override = 103
        phy.profile_outputs.MODEM_SHAPING2_COEFF9.override = 105
        phy.profile_outputs.MODEM_SHAPING2_COEFF10.override = 98
        phy.profile_outputs.MODEM_SHAPING2_COEFF11.override = 84
        phy.profile_outputs.MODEM_SHAPING3_COEFF12.override = 64
        phy.profile_outputs.MODEM_SHAPING3_COEFF13.override = 41
        phy.profile_outputs.MODEM_SHAPING3_COEFF14.override = 21
        phy.profile_outputs.MODEM_SHAPING3_COEFF15.override = 5
        phy.profile_outputs.MODEM_SHAPING4_COEFF16.override = 0
        phy.profile_outputs.MODEM_SHAPING4_COEFF17.override = 0
        phy.profile_outputs.MODEM_SHAPING4_COEFF18.override = 0
        phy.profile_outputs.MODEM_SHAPING4_COEFF19.override = 0
        phy.profile_outputs.MODEM_SHAPING5_COEFF20.override = 1
        phy.profile_outputs.MODEM_SHAPING5_COEFF21.override = 2
        phy.profile_outputs.MODEM_SHAPING5_COEFF22.override = 3
        phy.profile_outputs.MODEM_SHAPING5_COEFF23.override = 4
        phy.profile_outputs.MODEM_SHAPING6_COEFF24.override = 4
        phy.profile_outputs.MODEM_SHAPING6_COEFF25.override = 4
        phy.profile_outputs.MODEM_SHAPING6_COEFF26.override = 3
        phy.profile_outputs.MODEM_SHAPING6_COEFF27.override = 3
        phy.profile_outputs.MODEM_SHAPING7_COEFF28.override = 3
        phy.profile_outputs.MODEM_SHAPING7_COEFF29.override = 3
        phy.profile_outputs.MODEM_SHAPING7_COEFF30.override = 3
        phy.profile_outputs.MODEM_SHAPING7_COEFF31.override = 2
        phy.profile_outputs.MODEM_SHAPING8_COEFF32.override = 2
        phy.profile_outputs.MODEM_SHAPING8_COEFF33.override = 2
        phy.profile_outputs.MODEM_SHAPING8_COEFF34.override = 2
        phy.profile_outputs.MODEM_SHAPING8_COEFF35.override = 2
        phy.profile_outputs.MODEM_SHAPING9_COEFF36.override = 2
        phy.profile_outputs.MODEM_SHAPING9_COEFF37.override = 1
        phy.profile_outputs.MODEM_SHAPING9_COEFF38.override = 1
        phy.profile_outputs.MODEM_SHAPING9_COEFF39.override = 1
        phy.profile_outputs.MODEM_SHAPING10_COEFF40.override = 0
        phy.profile_outputs.MODEM_SHAPING10_COEFF41.override = 0
        phy.profile_outputs.MODEM_SHAPING10_COEFF42.override = 0
        phy.profile_outputs.MODEM_SHAPING10_COEFF43.override = 0
        phy.profile_outputs.MODEM_SHAPING11_COEFF44.override = 0
        phy.profile_outputs.MODEM_SHAPING11_COEFF45.override = 0
        phy.profile_outputs.MODEM_SHAPING11_COEFF46.override = 0
        phy.profile_outputs.MODEM_SHAPING11_COEFF47.override = 0

    def BLE_AGC(self, phy, model):
        phy.profile_outputs.AGC_CTRL0_PWRTARGET.override = 245
        phy.profile_outputs.AGC_STEPDWN_STEPDWN0.override = 1
        phy.profile_outputs.AGC_STEPDWN_STEPDWN1.override = 2
        phy.profile_outputs.AGC_STEPDWN_STEPDWN2.override = 3
        phy.profile_outputs.AGC_STEPDWN_STEPDWN3.override = 3
        phy.profile_outputs.AGC_STEPDWN_STEPDWN4.override = 3
        phy.profile_outputs.AGC_STEPDWN_STEPDWN5.override = 5

    def BLE_DSA(selfs, phy, model):
        phy.profile_outputs.MODEM_DSACTRL_ARRTOLERTHD0.override = 1
        phy.profile_outputs.MODEM_DSACTRL_ARRTOLERTHD1.override = 2
        phy.profile_outputs.MODEM_DSACTRL_FREQAVGSYM.override = 0
        phy.profile_outputs.MODEM_DSACTRL_GAINREDUCDLY.override = 2
        phy.profile_outputs.MODEM_DSATHD0_FDEVMAXTHD.override = 90
        phy.profile_outputs.MODEM_DSATHD0_FDEVMINTHD.override = 16
        phy.profile_outputs.MODEM_DSATHD0_SPIKETHD.override = 60
        phy.profile_outputs.MODEM_DSATHD0_UNMODTHD.override = 8
        phy.profile_outputs.MODEM_DSATHD1_AMPFLTBYP.override = 0
        phy.profile_outputs.MODEM_DSATHD1_FREQSCALE.override = 1
        phy.profile_outputs.MODEM_DSATHD1_POWABSTHD.override = 3000
        phy.profile_outputs.MODEM_DSATHD1_POWRELTHD.override = 2
        phy.profile_outputs.MODEM_DSATHD1_PWRDETDIS.override = 0
        phy.profile_outputs.MODEM_DSATHD2_FDADJTHD.override = 20
        phy.profile_outputs.MODEM_DSATHD2_FREQESTTHD.override = 16
        phy.profile_outputs.MODEM_DSATHD2_INTERFERDET.override = 1
        phy.profile_outputs.MODEM_DSATHD2_JUMPDETEN.override = 0
        phy.profile_outputs.MODEM_DSATHD2_PMDETFORCE.override = 1
        phy.profile_outputs.MODEM_DSATHD2_PMDETPASSTHD.override = 4
        phy.profile_outputs.MODEM_DSATHD2_POWABSTHDLOG.override = 248
        phy.profile_outputs.MODEM_DSATHD3_FDEVMAXTHDLO.override = 160
        phy.profile_outputs.MODEM_DSATHD3_FDEVMINTHDLO.override = 8
        phy.profile_outputs.MODEM_DSATHD3_SPIKETHDLO.override = 90
        phy.profile_outputs.MODEM_DSATHD4_ARRTOLERTHD0LO.override = 1
        phy.profile_outputs.MODEM_DSATHD4_ARRTOLERTHD1LO.override = 3
        phy.profile_outputs.MODEM_DSATHD4_POWABSTHDLO.override = 1000
        phy.profile_outputs.MODEM_DSATHD4_SWTHD.override = 1

    # BLE 1M Legacy
    def Bluetooth_LE_base(self, phy, model):
        PHY_COMMON_FRAME_BLE(phy, model)
        self.BLE_AGC(phy, model)
        self.BLE_TX_Shaping_Coeffs(phy, model)

        phy.profile_inputs.bandwidth_hz.value = 1260000
        phy.profile_inputs.base_frequency_hz.value = long(2450000000)
        phy.profile_inputs.baudrate_tol_ppm.value = 1000
        phy.profile_inputs.bitrate.value = 1000000
        phy.profile_inputs.channel_spacing_hz.value = 2000000
        phy.profile_inputs.deviation.value = 250000
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsa_enable.value = True
        phy.profile_inputs.dsss_chipping_code.value = long(0)
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.errors_in_timing_window.value = 1
        phy.profile_inputs.freq_offset_hz.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.if_frequency_hz.value = 1370000
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK2
        phy.profile_inputs.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_1000KHz
        phy.profile_inputs.pll_bandwidth_rx.value = model.vars.pll_bandwidth_rx.var_enum.BW_250KHz
        phy.profile_inputs.preamble_length.value = 8
        phy.profile_inputs.rssi_period.value = 3
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 0.5
        phy.profile_inputs.symbols_in_timing_window.value = 0
        phy.profile_inputs.target_osr.value = 5
        phy.profile_inputs.timing_detection_threshold.value = 140
        phy.profile_inputs.timing_sample_threshold.value = 0
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.xtal_frequency_hz.value = 38400000
        phy.profile_inputs.demod_select.value = model.vars.demod_select.var_enum.LEGACY

        phy.profile_outputs.AGC_CTRL2_DISRFPKD.override = 1
        phy.profile_outputs.AGC_CTRL4_RFPKDCNTEN.override = 0
        phy.profile_outputs.AGC_GAINRANGE_PNGAINSTEP.override = 1
        phy.profile_outputs.AGC_LNABOOST_LNABWADJ.override = 0
        phy.profile_outputs.FRC_AUTOCG_AUTOCGEN.override = 7
        phy.profile_outputs.MODEM_CTRL0_FRAMEDETDEL.override = 2
        phy.profile_outputs.MODEM_CTRL2_SQITHRESH.override = 200
        phy.profile_outputs.MODEM_DSACTRL_DSAMODE.override = 0
        phy.profile_outputs.MODEM_TIMING_OFFSUBNUM.override = 7

    def PHY_Bluetooth_LE(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='Official BLE 1Mbps Legacy PHY for Panther',
                            phy_name=phy_name)
        self.Bluetooth_LE_base(phy, model)
        return phy

    def PHY_Bluetooth_LE_EnPkd(self, model):
        phy = self.PHY_Bluetooth_LE(model, 'PHY_Bluetooth_LE_EnPkd')
        phy.profile_outputs.AGC_CTRL2_DISRFPKD.override = 0
        phy.profile_outputs.AGC_CTRL4_RFPKDCNTEN.override = 1
        return phy

    # BLE 1M Viterbi
    def Bluetooth_LE_Viterbi_base(self, phy, model):
        PHY_COMMON_FRAME_BLE(phy, model)
        self.BLE_AGC(phy, model)
        self.BLE_TX_Shaping_Coeffs(phy, model)
        self.BLE_DSA(phy, model)

        phy.profile_inputs.bandwidth_hz.value = 1099233
        phy.profile_inputs.base_frequency_hz.value = long(2402000000)
        phy.profile_inputs.baudrate_tol_ppm.value = 1000
        phy.profile_inputs.bitrate.value = 1000000
        phy.profile_inputs.channel_spacing_hz.value = 2000000
        phy.profile_inputs.deviation.value = 250000
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsa_enable.value = True
        phy.profile_inputs.dsss_chipping_code.value = long(0)
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.errors_in_timing_window.value = 1
        phy.profile_inputs.freq_offset_hz.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.if_frequency_hz.value = 1370000
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK2
        phy.profile_inputs.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_1000KHz
        phy.profile_inputs.pll_bandwidth_rx.value = model.vars.pll_bandwidth_rx.var_enum.BW_250KHz
        phy.profile_inputs.preamble_length.value = 8
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 0.5
        phy.profile_inputs.symbols_in_timing_window.value = 0
        phy.profile_inputs.target_osr.value = 4
        phy.profile_inputs.timing_detection_threshold.value = 140
        phy.profile_inputs.timing_sample_threshold.value = 0
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.xtal_frequency_hz.value = 38400000

        phy.profile_outputs.FRC_AUTOCG_AUTOCGEN.override = 7
        phy.profile_outputs.MODEM_CGCLKSTOP_FORCEOFF.override = 65535
        phy.profile_outputs.MODEM_TXBR_TXBRDEN.override = 5
        phy.profile_outputs.MODEM_TXBR_TXBRNUM.override = 24
        phy.profile_outputs.MODEM_VITERBIDEMOD_VITERBIKSI1.override = 62
        phy.profile_outputs.MODEM_VITERBIDEMOD_VITERBIKSI2.override = 42
        phy.profile_outputs.MODEM_VITERBIDEMOD_VITERBIKSI3.override = 30
        phy.profile_outputs.MODEM_VTCORRCFG1_EXPSYNCLEN.override = 148
        phy.profile_outputs.MODEM_VTCORRCFG1_VTFRQLIM.override = 100
        phy.profile_outputs.MODEM_VTCORRCFG0_EXPECTPATT.override = 2491575950

    def PHY_Bluetooth_LE_Viterbi(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='Bluetooth LE Viterbi phase-DSA',
                            phy_name=phy_name)
        self.Bluetooth_LE_Viterbi_base(phy, model)
        return phy

    # BLE 2M Viterbi
    def Bluetooth_LE_2M_Viterbi_base(self, phy, model):
        PHY_COMMON_FRAME_BLE(phy, model)
        self.BLE_AGC(phy, model)
        self.BLE_2M_TX_Shaping_Coeffs(phy, model)
        self.BLE_DSA(phy, model)

        phy.profile_inputs.bandwidth_hz.value = 2500000
        phy.profile_inputs.base_frequency_hz.value = long(2402000000)
        phy.profile_inputs.baudrate_tol_ppm.value = 1000
        phy.profile_inputs.bitrate.value = 2000000
        phy.profile_inputs.channel_spacing_hz.value = 2000000
        phy.profile_inputs.deviation.value = 500000
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsa_enable.value = True
        phy.profile_inputs.dsss_chipping_code.value = long(0)
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.errors_in_timing_window.value = 1
        phy.profile_inputs.freq_offset_hz.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.if_frequency_hz.value = 1370000
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK2
        phy.profile_inputs.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_1500KHz
        phy.profile_inputs.pll_bandwidth_rx.value = model.vars.pll_bandwidth_rx.var_enum.BW_250KHz
        phy.profile_inputs.preamble_length.value = 16
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 0.5
        phy.profile_inputs.symbols_in_timing_window.value = 0
        phy.profile_inputs.target_osr.value = 4
        phy.profile_inputs.timing_detection_threshold.value = 140
        phy.profile_inputs.timing_sample_threshold.value = 0
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.xtal_frequency_hz.value = 38400000
        phy.profile_inputs.src1_range_available_minimum.value = 133
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.AFC_LOCK_AT_FRAME_DETECT

        phy.profile_outputs.MODEM_CGCLKSTOP_FORCEOFF.override = 65535
        phy.profile_outputs.MODEM_DSACTRL_ARRTHD.override = 5
        phy.profile_outputs.MODEM_AFCADJTX_AFCSCALEM.override = 27
        phy.profile_outputs.MODEM_AFCADJRX_AFCSCALEM.override = 27
        phy.profile_outputs.MODEM_DSATHD0_FDEVMAXTHD.override = 180
        phy.profile_outputs.MODEM_DSATHD3_FDEVMAXTHDLO.override = 180
        phy.profile_outputs.MODEM_DSATHD4_POWABSTHDLO.override = 1500
        phy.profile_outputs.MODEM_VTBLETIMING_TIMINGDELAY.override = 220
        phy.profile_outputs.MODEM_VTBLETIMING_FLENOFF.override = 4
        phy.profile_outputs.MODEM_VTCORRCFG1_EXPSYNCLEN.override = 148
        phy.profile_outputs.MODEM_VTCORRCFG1_VTFRQLIM.override = 220
        phy.profile_outputs.MODEM_VTTRACK_HIPWRTHD.override = 43
        phy.profile_outputs.MODEM_VTCORRCFG0_EXPECTPATT.override = 2491575950

    def PHY_Bluetooth_LE_2M_Viterbi(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='Official 2Mbps BLE phase-DSA PHY for Panther',
                            phy_name=phy_name)
        self.Bluetooth_LE_2M_Viterbi_base(phy, model)
        return phy

    # BLE 1M TRecS + Viterbi
    def Bluetooth_LE_Viterbi_noDSA_base(self, phy, model):
        phy.profile_inputs.bandwidth_hz.value = 1099233
        phy.profile_inputs.base_frequency_hz.value = long(2402000000)
        phy.profile_inputs.baudrate_tol_ppm.value = 1000
        phy.profile_inputs.bitrate.value = 1000000
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.deviation.value = 250000
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsa_enable.value = False
        phy.profile_inputs.dsss_chipping_code.value = long(0)
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.errors_in_timing_window.value = 1
        phy.profile_inputs.freq_offset_hz.value = 0
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.if_frequency_hz.value = 1370000
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK2
        phy.profile_inputs.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_1000KHz
        phy.profile_inputs.pll_bandwidth_rx.value = model.vars.pll_bandwidth_rx.var_enum.BW_250KHz
        phy.profile_inputs.preamble_length.value = 8
        phy.profile_inputs.rssi_period.value = 3
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 0.5
        phy.profile_inputs.symbols_in_timing_window.value = 0
        phy.profile_inputs.target_osr.value = 4
        phy.profile_inputs.timing_detection_threshold.value = 140
        phy.profile_inputs.timing_sample_threshold.value = 0
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.xtal_frequency_hz.value = 38400000

        # Decimation and Demod Overrides
        phy.profile_outputs.MODEM_CGCLKSTOP_FORCEOFF.override = 56831
        phy.profile_outputs.MODEM_CTRL0_FRAMEDETDEL.override = 2
        phy.profile_outputs.MODEM_CTRL6_RXBRCALCDIS.override = 1
        phy.profile_outputs.MODEM_PRE_BASE.override = 2

        # Shaping overrides
        self.BLE_TX_Shaping_Coeffs(phy, model)

        # FRC Overrides
        PHY_COMMON_FRAME_BLE(phy, model)
        phy.profile_outputs.FRC_AUTOCG_AUTOCGEN.override = 7
        phy.profile_outputs.FRC_PUNCTCTRL_PUNCT0.override = 1
        phy.profile_outputs.FRC_PUNCTCTRL_PUNCT1.override = 1

        # This should be set only on DSA PHYs (PGLYNX-566), sowe can clear it.
        phy.profile_outputs.FRC_CTRL_WAITEOFEN.override = 0

        # Radio Controller Overrides
        phy.profile_outputs.RAC_SYNTHREGCTRL_MMDLDOVREFTRIM.override = 3

        # Viterbi Demod Overrides
        phy.profile_outputs.MODEM_VITERBIDEMOD_SYNTHAFC.override = 1
        phy.profile_outputs.MODEM_VITERBIDEMOD_VITERBIKSI1.override = 65
        phy.profile_outputs.MODEM_VITERBIDEMOD_VITERBIKSI2.override = 45
        phy.profile_outputs.MODEM_VITERBIDEMOD_VITERBIKSI3.override = 24
        phy.profile_outputs.MODEM_VTCORRCFG1_EXPECTHT.override = 5
        phy.profile_outputs.MODEM_VTCORRCFG1_VTFRQLIM.override = 100
        phy.profile_outputs.MODEM_VTCORRCFG0_EXPECTPATT.override = 2491575950

    def Bluetooth_LE_Viterbi_noDSA_halfrate_base(self, phy, model):
        self.Bluetooth_LE_Viterbi_noDSA_base(phy, model)
        phy.profile_inputs.if_frequency_hz.value = 700000
        phy.profile_inputs.adc_rate_mode.value = model.vars.adc_rate_mode.var_enum.HALFRATE

        phy.profile_outputs.RAC_IFADCTRIM0_IFADCENHALFMODE.override = 1
        phy.profile_outputs.AGC_AGCPERIOD0_MAXHICNTTHD.override = 9
        phy.profile_outputs.AGC_AGCPERIOD0_PERIODHI.override = 14
        phy.profile_outputs.AGC_AGCPERIOD1_PERIODLOW.override = 45
        phy.profile_outputs.AGC_CTRL0_PWRTARGET.override = 245
        phy.profile_outputs.AGC_CTRL2_DISRFPKD.override = 1
        phy.profile_outputs.AGC_CTRL4_RFPKDCNTEN.override = 0
        phy.profile_outputs.AGC_GAINRANGE_PNGAINSTEP.override = 1
        phy.profile_outputs.AGC_GAINSTEPLIM0_CFLOOPSTEPMAX.override = 4
        phy.profile_outputs.AGC_GAINSTEPLIM0_HYST.override = 3
        phy.profile_outputs.AGC_GAINSTEPLIM1_PNINDEXMAX.override = 14
        phy.profile_outputs.AGC_HICNTREGION0_HICNTREGION0.override = 4
        phy.profile_outputs.AGC_HICNTREGION0_HICNTREGION1.override = 5
        phy.profile_outputs.AGC_HICNTREGION0_HICNTREGION2.override = 6
        phy.profile_outputs.AGC_HICNTREGION0_HICNTREGION3.override = 7
        phy.profile_outputs.AGC_HICNTREGION1_HICNTREGION4.override = 8
        #FIXME phy.profile_outputs.AGC_PNRFATT1_LNAMIXRFATT3.override = 3
        #FIXME phy.profile_outputs.AGC_PNRFATT1_LNAMIXRFATT4.override = 6
        #FIXME phy.profile_outputs.AGC_PNRFATT2_LNAMIXRFATT5.override = 9
        #FIXME phy.profile_outputs.AGC_PNRFATT2_LNAMIXRFATT6.override = 13
        #FIXME phy.profile_outputs.AGC_PNRFATT3_LNAMIXRFATT7.override = 16
        #FIXME phy.profile_outputs.AGC_PNRFATT3_LNAMIXRFATT8.override = 22
        #FIXME phy.profile_outputs.AGC_PNRFATT4_LNAMIXRFATT9.override = 30
        #FIXME phy.profile_outputs.AGC_PNRFATT4_LNAMIXRFATT10.override = 32
        #FIXME phy.profile_outputs.AGC_PNRFATT5_LNAMIXRFATT11.override = 43
        #FIXME phy.profile_outputs.AGC_PNRFATT5_LNAMIXRFATT12.override = 51
        #FIXME phy.profile_outputs.AGC_PNRFATT6_LNAMIXRFATT13.override = 63
        #FIXME phy.profile_outputs.AGC_PNRFATT6_LNAMIXRFATT14.override = 126
        phy.profile_outputs.AGC_STEPDWN_STEPDWN0.override = 1
        phy.profile_outputs.AGC_STEPDWN_STEPDWN1.override = 2
        phy.profile_outputs.AGC_STEPDWN_STEPDWN2.override = 3
        phy.profile_outputs.AGC_STEPDWN_STEPDWN3.override = 3
        phy.profile_outputs.AGC_STEPDWN_STEPDWN4.override = 3
        phy.profile_outputs.AGC_STEPDWN_STEPDWN5.override = 5
        phy.profile_outputs.FRC_CTRL_LPMODEDIS.override = 1

    def PHY_Bluetooth_LE_Viterbi_noDSA(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='BLE Viterbi No DSA PHY for Lynx',
                            phy_name=phy_name)
        self.Bluetooth_LE_Viterbi_noDSA_halfrate_base(phy, model)
        return phy

    def PHY_Bluetooth_LE_Viterbi_noDSA_EnPkd(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base,
                            readable_name='BLE Viterbi No DSA PHY for Lynx with Peak Detector Enabled',
                            phy_name=phy_name)
        self.Bluetooth_LE_Viterbi_noDSA_halfrate_base(phy, model)

        phy.profile_outputs.AGC_CTRL2_DISRFPKD.override = 0
        phy.profile_outputs.AGC_CTRL4_RFPKDCNTEN.override = 1

    def PHY_Bluetooth_1M_prod(self, model, phy_name=None):
        phy = self.PHY_Bluetooth_LE_Viterbi_noDSA_EnPkd(model, phy_name='PHY_Bluetooth_1M_prod')
        return phy

    def PHY_Bluetooth_LE_1M_Viterbi_917M_noDSA(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='PHY_Bluetooth_LE_1M_Viterbi_917M_noDSA',
                            phy_name=phy_name)
        self.Bluetooth_LE_Viterbi_noDSA_halfrate_base(phy, model)

        phy.profile_inputs.if_frequency_hz.value = 1066666
        phy.profile_inputs.base_frequency_hz.value = long(917000000)

        phy.profile_outputs.SYNTH_DIVCTRL_LODIVFREQCTRL.override = 3
        return phy

    def PHY_Bluetooth_LE_Viterbi_noDSA_fullrate(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='BLE Viterbi No DSA Fullrate PHY for Lynx',
                            phy_name=phy_name)
        self.Bluetooth_LE_Viterbi_noDSA_base(phy, model)

        # default bandwidth will cause halfrate unless forced
        phy.profile_inputs.adc_rate_mode.value = model.vars.adc_rate_mode.var_enum.FULLRATE

        return phy

    def PHY_Bluetooth_LE_Viterbi_noDSA_fullrate_EnPkd(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base,
                            readable_name='BLE Viterbi No DSA Fullrate PHY for Lynx with Peak Detector Enabled',
                            phy_name=phy_name)
        self.Bluetooth_LE_Viterbi_noDSA_base(phy, model)

        # default bandwidth will cause halfrate unless forced
        phy.profile_inputs.adc_rate_mode.value = model.vars.adc_rate_mode.var_enum.FULLRATE

        phy.profile_outputs.AGC_CTRL2_DISRFPKD.override = 0
        phy.profile_outputs.AGC_CTRL4_RFPKDCNTEN.override = 1

        return phy

    # BLE 2M TRecs + Viterbi
    def Bluetooth_LE_2M_Viterbi_noDSA_base(self, phy, model):
        self.Bluetooth_LE_Viterbi_noDSA_base(phy, model)

        phy.profile_inputs.bitrate.value = 2000000
        phy.profile_inputs.bandwidth_hz.value = 2200000
        phy.profile_inputs.deviation.value = 500000
        phy.profile_inputs.preamble_length.value = 16
        phy.profile_inputs.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_1500KHz
        phy.profile_inputs.src1_range_available_minimum.value = 133

    def PHY_Bluetooth_LE_2M_Viterbi_noDSA_fullrate(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='BLE Viterbi 2M No DSA Fullrate PHY for Lynx',
                            phy_name=phy_name)
        self.Bluetooth_LE_2M_Viterbi_noDSA_base(phy, model)

        phy.profile_inputs.adc_rate_mode.value = model.vars.adc_rate_mode.var_enum.FULLRATE
        return phy

    def PHY_Bluetooth_LE_2M_Viterbi_noDSA_fullrate_EnPkd(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base,
                            readable_name='BLE Viterbi 2M No DSA Fullrate PHY for Lynx with Peak Detector Enabled',
                            phy_name=phy_name)
        self.Bluetooth_LE_2M_Viterbi_noDSA_base(phy, model)

        phy.profile_inputs.adc_rate_mode.value = model.vars.adc_rate_mode.var_enum.FULLRATE

        phy.profile_outputs.AGC_CTRL2_DISRFPKD.override = 0
        phy.profile_outputs.AGC_CTRL4_RFPKDCNTEN.override = 1

    def PHY_Bluetooth_2M_prod(self, model, phy_name=None):
        phy = self.PHY_Bluetooth_LE_2M_Viterbi_noDSA_fullrate_EnPkd(model, phy_name='PHY_Bluetooth_2M_prod')
        return phy

    '''
    # BLR 125K
    def Bluetooth_LongRange_base(self, phy, model):
        PHY_COMMON_FRAME_BLE(phy, model)
        self.BLE_AGC(phy, model)

        phy.profile_inputs.bandwidth_hz.value = 1230000
        phy.profile_inputs.base_frequency_hz.value = long(2450000000)
        phy.profile_inputs.baudrate_tol_ppm.value = 1000
        phy.profile_inputs.bitrate.value = 1000000
        phy.profile_inputs.channel_spacing_hz.value = 2000000
        phy.profile_inputs.deviation.value = 250000
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsa_enable.value = True
        phy.profile_inputs.dsss_chipping_code.value = long(0)
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.errors_in_timing_window.value = 1
        phy.profile_inputs.freq_offset_hz.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.header_addtrailtxdata_en.value = True  # We need to add Trail TX Data to the header (subframe 0), which is the Coding/Rate Indication (CI/RI)
        phy.profile_inputs.header_calc_crc.value = False  # The header (subframe 0) does not include a CRC
        phy.profile_inputs.header_excludesubframewcnt_en.value = True  # With Dynamic frame length (DFL) mode, we need to exclude the header (subframe 0) from Word Counter
        phy.profile_inputs.header_white_en.value = False  # No whitening in the header (subframe 0)
        phy.profile_inputs.if_frequency_hz.value = 1370000
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK2
        phy.profile_inputs.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_1000KHz
        phy.profile_inputs.pll_bandwidth_rx.value = model.vars.pll_bandwidth_rx.var_enum.BW_200KHz
        phy.profile_inputs.preamble_length.value = 20
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 0.5
        phy.profile_inputs.symbols_in_timing_window.value = 0
        phy.profile_inputs.target_osr.value = 4
        phy.profile_inputs.timing_detection_threshold.value = 140
        phy.profile_inputs.timing_sample_threshold.value = 0
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.xtal_frequency_hz.value = 38400000
        phy.profile_inputs.src1_range_available_minimum.value = 128
        phy.profile_inputs.demod_select.value = model.vars.demod_select.var_enum.LONGRANGE
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.adc_rate_mode.value = model.vars.adc_rate_mode.var_enum.FULLRATE

        phy.profile_outputs.AGC_CTRL2_DISRFPKD.override = 1
        phy.profile_outputs.AGC_CTRL4_RFPKDCNTEN.override = 0
        phy.profile_outputs.AGC_LNABOOST_LNABWADJ.override = 0
        phy.profile_outputs.AGC_GAINRANGE_PNGAINSTEP.override = 1
        phy.profile_outputs.FRC_CTRL_RXFCDMODE.override = 0  # Override the RXFCDMODE to FCDMODE0 (FCD2 is reloaded when SCNT reaches 0)
        phy.profile_outputs.FRC_FCD0_INCLUDECRC.override = 0
        phy.profile_outputs.FRC_FCD0_WORDS.override = 3  # SYNCWORD size (4 bytes) - 1 = 3
        phy.profile_outputs.FRC_FCD2_ADDTRAILTXDATA.override = 0
        phy.profile_outputs.FRC_FCD2_CALCCRC.override = 1
        phy.profile_outputs.FRC_FCD2_EXCLUDESUBFRAMEWCNT.override = 0
        phy.profile_outputs.FRC_FCD2_INCLUDECRC.override = 1
        phy.profile_outputs.FRC_FCD2_WORDS.override = 255
        phy.profile_outputs.FRC_AUTOCG_AUTOCGEN.override = 7
        phy.profile_outputs.FRC_CONVGENERATOR_GENERATOR0.override = 13
        phy.profile_outputs.FRC_CONVGENERATOR_GENERATOR1.override = 15
        phy.profile_outputs.FRC_FECCTRL_CONVMODE.override = 1
        phy.profile_outputs.FRC_PUNCTCTRL_PUNCT0.override = 1
        phy.profile_outputs.FRC_PUNCTCTRL_PUNCT1.override = 1
        phy.profile_outputs.FRC_TRAILTXDATACTRL_TRAILTXDATACNT.override = 4
        phy.profile_outputs.MODEM_AFC_AFCRXMODE.override = 0 # Was missed
        phy.profile_outputs.MODEM_CTRL0_CODING.override = 3
        phy.profile_outputs.MODEM_CTRL0_FRAMEDETDEL.override = 1
        phy.profile_outputs.MODEM_CTRL1_COMPMODE.override = 3
        phy.profile_outputs.MODEM_CTRL1_SYNCDATA.override = 1
        phy.profile_outputs.MODEM_CTRL2_RATESELMODE.override = 2
        phy.profile_outputs.MODEM_CTRL3_TSAMPDEL.override =2 # Was missed
        phy.profile_outputs.MODEM_DSACTRL_DSAMODE.override = 0  # Was missed
        phy.profile_outputs.MODEM_LONGRANGE1_AVGWIN.override = 3
        phy.profile_outputs.MODEM_LONGRANGE1_CHPWRACCUDEL.override = 3
        phy.profile_outputs.MODEM_LONGRANGE1_HYSVAL.override = 3
        phy.profile_outputs.MODEM_LONGRANGE1_LOGICBASEDLRDEMODGATE.override = 1
        phy.profile_outputs.MODEM_LONGRANGE1_LOGICBASEDPUGATE.override = 1
        phy.profile_outputs.MODEM_LONGRANGE1_LRSS.override = 4
        phy.profile_outputs.MODEM_LONGRANGE1_LRTIMEOUTTHD.override = 400
        phy.profile_outputs.MODEM_LONGRANGE2_LRCHPWRTH1.override = 8
        phy.profile_outputs.MODEM_LONGRANGE2_LRCHPWRTH2.override = 14
        phy.profile_outputs.MODEM_LONGRANGE2_LRCHPWRTH3.override = 20
        phy.profile_outputs.MODEM_LONGRANGE2_LRCHPWRTH4.override = 26
        phy.profile_outputs.MODEM_LONGRANGE3_LRCHPWRTH5.override = 32
        phy.profile_outputs.MODEM_LONGRANGE3_LRCHPWRTH6.override = 38
        phy.profile_outputs.MODEM_LONGRANGE3_LRCHPWRTH7.override = 44
        phy.profile_outputs.MODEM_LONGRANGE3_LRCHPWRTH8.override = 50
        phy.profile_outputs.MODEM_LONGRANGE4_LRCHPWRSH2.override = 1
        phy.profile_outputs.MODEM_LONGRANGE4_LRCHPWRSH3.override = 2
        phy.profile_outputs.MODEM_LONGRANGE4_LRCHPWRSH4.override = 3
        phy.profile_outputs.MODEM_LONGRANGE4_LRCHPWRTH10.override = 62
        phy.profile_outputs.MODEM_LONGRANGE4_LRCHPWRTH9.override = 56
        phy.profile_outputs.MODEM_LONGRANGE5_LRCHPWRSH10.override = 9
        phy.profile_outputs.MODEM_LONGRANGE5_LRCHPWRSH11.override = 10
        phy.profile_outputs.MODEM_LONGRANGE5_LRCHPWRSH5.override = 4
        phy.profile_outputs.MODEM_LONGRANGE5_LRCHPWRSH6.override = 5
        phy.profile_outputs.MODEM_LONGRANGE5_LRCHPWRSH7.override = 6
        phy.profile_outputs.MODEM_LONGRANGE5_LRCHPWRSH8.override = 7
        phy.profile_outputs.MODEM_LONGRANGE5_LRCHPWRSH9.override = 8
        phy.profile_outputs.MODEM_LONGRANGE6_LRCHPWRSPIKETH.override = 29
        phy.profile_outputs.MODEM_LONGRANGE6_LRSPIKETHD.override = 95
        phy.profile_outputs.MODEM_LONGRANGE_LRBLE.override = 1
        phy.profile_outputs.MODEM_LONGRANGE_LRBLEDSA.override = 1
        phy.profile_outputs.MODEM_LONGRANGE_LRCORRTHD.override = 1100
        phy.profile_outputs.MODEM_LONGRANGE_LRDEC.override = 3
        phy.profile_outputs.MODEM_LONGRANGE_LRTIMCORRTHD.override = 1000
        phy.profile_outputs.MODEM_MODINDEX_FREQGAINE.override = 2
        phy.profile_outputs.MODEM_MODINDEX_FREQGAINM.override = 2
        phy.profile_outputs.MODEM_TXBR_TXBRDEN.override = 5
        phy.profile_outputs.MODEM_TXBR_TXBRNUM.override = 24
        phy.profile_outputs.MODEM_VITERBIDEMOD_VTDEMODEN.override = 1
        phy.profile_outputs.MODEM_VTBLETIMING_DISDEMODOF.override = 1
        phy.profile_outputs.MODEM_VTCORRCFG1_VTFRQLIM.override = 110
        phy.profile_outputs.MODEM_VTTRACK_TIMEACQUTHD.override = 32

    def PHY_Bluetooth_LongRange_dsa_125kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='Bluetooth LongRange DSA 125kbps PHY for Lynx',
                            phy_name=phy_name)
        self.Bluetooth_LongRange_base(phy, model)
        return phy

    def PHY_Bluetooth_LongRange_dsa_125kbps_EnPkd(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base,
                            readable_name='Bluetooth LongRange DSA 125kbps PHY for Lynx with Peak Detector Enabled',
                            phy_name=phy_name)
        self.Bluetooth_LongRange_base(phy, model)
        phy.profile_outputs.AGC_CTRL2_DISRFPKD.override = 0
        phy.profile_outputs.AGC_CTRL4_RFPKDCNTEN.override = 1
        return phy

    def PHY_Bluetooth_LR_125k_prod(self, model, phy_name=None):
        phy = self.PHY_Bluetooth_LongRange_dsa_125kbps_EnPkd(model, phy_name='PHY_Bluetooth_LR_125k_prod')
        return phy

    def PHY_Bluetooth_LongRange_NOdsa_125kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='Bluetooth LongRange DSA 125kbps',
                            phy_name=phy_name)
        self.Bluetooth_LongRange_base(phy, model)
        phy.profile_outputs.AGC_CTRL2_DISRFPKD.override = 0
        phy.profile_outputs.AGC_CTRL4_RFPKDCNTEN.override = 1
        phy.profile_outputs.AGC_GAINRANGE_PNGAINSTEP.override = 4
        return phy

    # BLR 500k
    def Bluetooth_LongRange_500kbps_base(self, phy, model):
        self.Bluetooth_LongRange_base(phy, model)
        phy.profile_outputs.FRC_CTRL_RATESELECT.override = 2
        phy.profile_outputs.FRC_TRAILTXDATACTRL_TRAILTXDATA.override = 1
        phy.profile_outputs.MODEM_LONGRANGE2_LRCHPWRTH1.override = 10
        phy.profile_outputs.MODEM_LONGRANGE2_LRCHPWRTH2.override = 16
        phy.profile_outputs.MODEM_LONGRANGE2_LRCHPWRTH3.override = 22
        phy.profile_outputs.MODEM_LONGRANGE2_LRCHPWRTH4.override = 28
        phy.profile_outputs.MODEM_LONGRANGE3_LRCHPWRTH5.override = 34
        phy.profile_outputs.MODEM_LONGRANGE3_LRCHPWRTH6.override = 40
        phy.profile_outputs.MODEM_LONGRANGE3_LRCHPWRTH7.override = 46
        phy.profile_outputs.MODEM_LONGRANGE3_LRCHPWRTH8.override = 52
        phy.profile_outputs.MODEM_LONGRANGE4_LRCHPWRTH10.override = 64
        phy.profile_outputs.MODEM_LONGRANGE4_LRCHPWRTH9.override = 58
        phy.profile_outputs.MODEM_LONGRANGE6_LRCHPWRSH12.override = 10
        phy.profile_outputs.MODEM_LONGRANGE6_LRCHPWRTH11.override = 72

    def PHY_Bluetooth_LongRange_dsa_500kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='Bluetooth LongRange DSA 500kbps PHY for Lynx',
                            phy_name=phy_name)
        self.Bluetooth_LongRange_500kbps_base(phy, model)
        return phy

    def PHY_Bluetooth_LongRange_dsa_500kbps_EnPkd(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base,
                            readable_name='Bluetooth LongRange DSA 500kbps PHY for Lynx with Peak Detector Enabled',
                            phy_name=phy_name)
        self.Bluetooth_LongRange_500kbps_base(phy, model)
        phy.profile_outputs.AGC_CTRL2_DISRFPKD.override = 0
        phy.profile_outputs.AGC_CTRL4_RFPKDCNTEN.override = 1
        return phy

    def PHY_Bluetooth_LR_500k_prod(self, model, phy_name=None):
        phy = self.PHY_Bluetooth_LongRange_dsa_500kbps_EnPkd(model, phy_name='PHY_Bluetooth_LR_500k_prod')
        return phy

    def PHY_Bluetooth_LongRange_NOdsa_500kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='Bluetooth LongRange DSA 500kbps',
                            phy_name=phy_name)
        self.Bluetooth_LongRange_500kbps_base(phy, model)
        phy.profile_outputs.AGC_CTRL2_DISRFPKD.override = 0
        phy.profile_outputs.AGC_CTRL4_RFPKDCNTEN.override = 1
        phy.profile_outputs.AGC_GAINRANGE_PNGAINSTEP.override = 4
        return phy

    def PHY_Bluetooth_1M_Concurrent(self, model, phy_name=None):
        # Start with the BLE LR 125k PHY
        phy = self.PHY_Bluetooth_LongRange_dsa_125kbps(model, phy_name='PHY_Bluetooth_1M_Concurrent')

        # The concurrent PHY needs to have:
        # Enable concurrent mode
        # FRC = BLE LR 125k, with added sub-frame description for BLE 1M uncoded
        # Demod = BLE LR 125k
        # TRECS/Viterbi = BLE 1M
        # BLE LR = BLE LR 125k
        # DSA = BLE LR 125k

        # FIXME: the following commented out registers don't exist in Ocelot/Bobcat at this point
        # Enable concurrent mode
        # phy.profile_outputs.MODEM_COCURRMODE_CONCURRENT.override = 1

        # Overrides for TRECS/Viterbi (copied from BLE 1M)
        phy.profile_outputs.MODEM_VITERBIDEMOD_SYNTHAFC.override = 1
        phy.profile_outputs.MODEM_VITERBIDEMOD_VITERBIKSI1.override = 65
        phy.profile_outputs.MODEM_VITERBIDEMOD_VITERBIKSI2.override = 45
        phy.profile_outputs.MODEM_VITERBIDEMOD_VITERBIKSI3.override = 24
        phy.profile_outputs.MODEM_VITERBIDEMOD_VTDEMODEN.override = 1
        phy.profile_outputs.MODEM_VTBLETIMING_TIMINGDELAY.override = 60
        phy.profile_outputs.MODEM_VTBLETIMING_VTBLETIMINGSEL.override = 1
        # phy.profile_outputs.MODEM_VTCORRCFG1_CORRSHFTLEN.override = 42
        phy.profile_outputs.MODEM_VTCORRCFG1_EXPECTHT.override = 5
        phy.profile_outputs.MODEM_VTCORRCFG1_EXPSYNCLEN.override = 146
        phy.profile_outputs.MODEM_VTCORRCFG1_VTFRQLIM.override = 100
        phy.profile_outputs.MODEM_VTTRACK_FREQTRACKMODE.override = 1
        # phy.profile_outputs.MODEM_VTTRACK_TIMEOUTMODE.override = 0
        phy.profile_outputs.MODEM_REALTIMCFE_MINCOSTTHD.override = 600
        phy.profile_outputs.MODEM_REALTIMCFE_RTCFEEN.override = 1
        phy.profile_outputs.MODEM_REALTIMCFE_RTSCHWIN.override = 10
        phy.profile_outputs.MODEM_REALTIMCFE_TRACKINGWIN.override = 5
        phy.profile_outputs.MODEM_REALTIMCFE_VTAFCFRAME.override = 1

        return phy
    '''

    def PHY_Bluetooth_1M_AOX_prod(self, model, phy_name=None):
        phy = self.PHY_Bluetooth_LE_Viterbi_noDSA_fullrate(model, phy_name='PHY_Bluetooth_1M_AOX_prod')
        # force fullrate and dec1 = 1 to match LYNX AOX config (which uses DEC1 switching)
        model.vars.adc_clock_mode.value_forced = model.vars.adc_clock_mode.var_enum.VCODIV
        model.vars.adc_rate_mode.value_forced = model.vars.adc_rate_mode.var_enum.FULLRATE
        #phy.profile_outputs.MODEM_CF_DEC0.override = 4  # 4
        #phy.profile_outputs.MODEM_CF_DEC1.override = 1  # dec1_actual = MODEM_CF_DEC1 + 1
        model.vars.dec1.value_forced = 2
        #phy.profile_outputs.MODEM_CF_DEC2.override = 0  # dec2_actual = MODEM_CF_DEC2 + 1
        return phy

    def PHY_Bluetooth_2M_AOX_prod(self, model, phy_name=None):
        phy = self.PHY_Bluetooth_LE_2M_Viterbi_noDSA_fullrate(model, phy_name='PHY_Bluetooth_2M_AOX_prod')
        return phy
