from pyradioconfig.parts.common.phys.phy_common import PHY_COMMON_FRAME_BLE
from pyradioconfig.calculator_model_framework.interfaces.iphy import IPhy
from py_2_and_3_compatibility import *

class PHYS_Internal_Bluetooth_LE_Ocelot(IPhy):

    def __init__(self):
        pass

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

    def Bluetooth_LE_Viterbi_noDSA_base(self, phy, model):
        """ Frequency planning """
        phy.profile_inputs.base_frequency_hz.value = 915000000
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.baudrate_tol_ppm.value = 1000

        """ Modulation Type """
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK2

        """ Symbol mapping and Encoding """
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED

        """ DSSS Parameters """
        phy.profile_inputs.dsss_chipping_code.value = long(0)
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0

        """ Shaping Filter """
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 0.5
        self.BLE_TX_Shaping_Coeffs(phy, model)

        """ DSA Parameters """
        phy.profile_inputs.dsa_enable.value = False

        """ Preamble Parameters """
        phy.profile_inputs.preamble_length.value = 8

        """ XO Parameters """
        phy.profile_inputs.xtal_frequency_hz.value = 39000000
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.tx_xtal_error_ppm.value = 0

        """ Timing parameters """
        phy.profile_inputs.symbols_in_timing_window.value = 0

        """ Frame """
        PHY_COMMON_FRAME_BLE(phy, model)
        phy.profile_outputs.FRC_AUTOCG_AUTOCGEN.override = 7
        phy.profile_outputs.FRC_PUNCTCTRL_PUNCT0.override = 1
        phy.profile_outputs.FRC_PUNCTCTRL_PUNCT1.override = 1

        """ Advanced inputs """
        phy.profile_outputs.MODEM_CGCLKSTOP_FORCEOFF.override = 56831
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON

        # This should be set only on DSA PHYs (PGLYNX-566), sowe can clear it.
        phy.profile_outputs.FRC_CTRL_WAITEOFEN.override = 0

        """ For Ocelot, need to force adc clock mode to be same as bobcat """
        phy.profile_inputs.adc_clock_mode.value = model.vars.adc_clock_mode.var_enum.VCODIV

    def Bluetooth_LE_Viterbi_noDSA_halfrate_base(self, phy, model):
        self.Bluetooth_LE_Viterbi_noDSA_base(phy, model)
        phy.profile_inputs.if_frequency_hz.value = 700000
        phy.profile_inputs.adc_rate_mode.value = model.vars.adc_rate_mode.var_enum.HALFRATE

        phy.profile_inputs.bandwidth_hz.value = 1099233
        phy.profile_inputs.bitrate.value = 1000000
        phy.profile_inputs.deviation.value = 250000

    def Bluetooth_LE_Viterbi_noDSA_fullrate_base(self, phy, model):
        self.Bluetooth_LE_Viterbi_noDSA_base(phy, model)
        phy.profile_inputs.if_frequency_hz.value = 1370000
        phy.profile_inputs.adc_rate_mode.value = model.vars.adc_rate_mode.var_enum.FULLRATE

        phy.profile_inputs.bitrate.value = 2000000
        phy.profile_inputs.bandwidth_hz.value = 2200000
        phy.profile_inputs.deviation.value = 500000
        phy.profile_inputs.preamble_length.value = 16
        phy.profile_inputs.src1_range_available_minimum.value = 133

    def PHY_Internal_Bluetooth_LE_Viterbi_noDSA(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='BLE Viterbi No DSA PHY for Ocelot 915 MHz',
                            phy_name=phy_name)
        self.Bluetooth_LE_Viterbi_noDSA_halfrate_base(phy, model)
        return phy

    def PHY_Internal_Bluetooth_LE_2M_Viterbi_noDSA_fullrate(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='BLE Viterbi No DSA Fullrate PHY for Ocelot 915 MHz',
                            phy_name=phy_name)
        self.Bluetooth_LE_Viterbi_noDSA_fullrate_base(phy, model)
        return phy