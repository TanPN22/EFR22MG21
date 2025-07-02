from pyradioconfig.parts.common.phys.phy_common import PHY_COMMON_FRAME_154
from pyradioconfig.parts.lynx.phys.Phys_IEEE802154 import PHYS_IEEE802154_Lynx
from pyradioconfig.parts.common.phys.phy_common import PHY_COMMON_FRAME_INTERNAL
from pyradioconfig.parts.panther.phys.PHY_internal_base import Phy_Internal_Base

from py_2_and_3_compatibility import *

class PHYS_Internal_IEEE802154_Ocelot(PHYS_IEEE802154_Lynx):

    def IEEE802154_Internal_915MHz_cohdsa_base(self, phy, model):
        """ Frequency Planning """
        phy.profile_inputs.base_frequency_hz.value = long(915e6)
        phy.profile_inputs.channel_spacing_hz.value = 5000000
        phy.profile_inputs.bitrate.value = 250000
        phy.profile_inputs.deviation.value = 500000
        phy.profile_inputs.if_frequency_hz.value = 1370000

        phy.profile_inputs.bandwidth_hz.value = 2524800
        phy.profile_inputs.baudrate_tol_ppm.value = 0

        PHY_COMMON_FRAME_154(phy, model)
        # Override min length for 802.15.4E Seq# Suppression
        phy.profile_inputs.var_length_minlength.value = 4
        # Phy_Internal_Base.AGC_FAST_LOOP_base(phy, model)

        """ Modulation """
        phy.profile_inputs.demod_select.value = model.vars.demod_select.var_enum.COHERENT
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.OQPSK

        """ Shaping filter """
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Custom_OQPSK
        phy.profile_inputs.shaping_filter_param.value = 0.0

        """ Symbol mapping and encoding """
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.symbol_encoding.value = model.vars.symbol_encoding.var_enum.DSSS
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED

        """ DSSS Configurations """
        phy.profile_inputs.dsss_chipping_code.value = long(0x744AC39B)
        phy.profile_inputs.dsss_len.value = 32
        phy.profile_inputs.dsss_spreading_factor.value = 8

        """ Preamble """
        phy.profile_inputs.preamble_length.value = 32
        phy.profile_inputs.preamble_pattern.value = 0
        phy.profile_inputs.preamble_pattern_len.value = 4

        """ Timing """
        phy.profile_inputs.symbols_in_timing_window.value = 12
        phy.profile_inputs.timing_detection_threshold.value = 65
        phy.profile_inputs.timing_sample_threshold.value = 0
        phy.profile_inputs.number_of_timing_windows.value = 7

        """ Sync """
        phy.profile_inputs.syncword_0.value = long(0xe5)
        phy.profile_inputs.syncword_1.value = long(0x0)
        phy.profile_inputs.syncword_length.value = 8

        """ XO Configuration """
        phy.profile_inputs.xtal_frequency_hz.value = 39000000
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.tx_xtal_error_ppm.value = 0

        """ Dynamic BBSS """
        phy.profile_outputs.MODEM_LONGRANGE1_AVGWIN.override = 4

        phy.profile_outputs.MODEM_LONGRANGE2_LRCHPWRTH1.override = 20
        phy.profile_outputs.MODEM_LONGRANGE2_LRCHPWRTH2.override = 26
        phy.profile_outputs.MODEM_LONGRANGE2_LRCHPWRTH3.override = 33
        phy.profile_outputs.MODEM_LONGRANGE2_LRCHPWRTH4.override = 40
        phy.profile_outputs.MODEM_LONGRANGE3_LRCHPWRTH5.override = 46
        phy.profile_outputs.MODEM_LONGRANGE3_LRCHPWRTH6.override = 52
        phy.profile_outputs.MODEM_LONGRANGE3_LRCHPWRTH7.override = 59
        phy.profile_outputs.MODEM_LONGRANGE3_LRCHPWRTH8.override = 66
        phy.profile_outputs.MODEM_LONGRANGE4_LRCHPWRTH9.override = 73
        phy.profile_outputs.MODEM_LONGRANGE4_LRCHPWRTH10.override = 80

        phy.profile_outputs.MODEM_LONGRANGE4_LRCHPWRSH1.override = 3
        phy.profile_outputs.MODEM_LONGRANGE4_LRCHPWRSH2.override = 4
        phy.profile_outputs.MODEM_LONGRANGE4_LRCHPWRSH3.override = 5
        phy.profile_outputs.MODEM_LONGRANGE4_LRCHPWRSH4.override = 5
        phy.profile_outputs.MODEM_LONGRANGE5_LRCHPWRSH5.override = 6
        phy.profile_outputs.MODEM_LONGRANGE5_LRCHPWRSH6.override = 7
        phy.profile_outputs.MODEM_LONGRANGE5_LRCHPWRSH7.override = 8
        phy.profile_outputs.MODEM_LONGRANGE5_LRCHPWRSH8.override = 9
        phy.profile_outputs.MODEM_LONGRANGE5_LRCHPWRSH9.override = 10
        phy.profile_outputs.MODEM_LONGRANGE5_LRCHPWRSH10.override = 11
        phy.profile_outputs.MODEM_LONGRANGE5_LRCHPWRSH11.override = 12

        """ Pre-filter """
        phy.profile_outputs.MODEM_LONGRANGE1_PREFILTLEN.override = 3

        """ Coherent DSA """
        phy.profile_outputs.MODEM_LONGRANGE1_LRTIMEOUTTHD.override = 320
        phy.profile_outputs.MODEM_COH2_DSAPEAKCHPWRTH.override = 200

        phy.profile_outputs.MODEM_LONGRANGE6_LRCHPWRSPIKETH.override = 40
        phy.profile_outputs.MODEM_LONGRANGE6_LRSPIKETHD.override = 105
        phy.profile_outputs.MODEM_COH2_FIXEDCDTHFORIIR.override = 105

        """ Dynamic Pre/Sync Threshold """
        phy.profile_outputs.MODEM_COH0_COHCHPWRTH0.override = 33
        phy.profile_outputs.MODEM_COH0_COHCHPWRTH1.override = 40
        phy.profile_outputs.MODEM_COH0_COHCHPWRTH2.override = 100

        phy.profile_outputs.MODEM_COH1_SYNCTHRESH0.override = 20
        phy.profile_outputs.MODEM_COH1_SYNCTHRESH1.override = 23
        phy.profile_outputs.MODEM_COH1_SYNCTHRESH2.override = 26

        phy.profile_outputs.MODEM_COH2_SYNCTHRESHDELTA1.override = 2
        phy.profile_outputs.MODEM_COH2_SYNCTHRESHDELTA2.override = 4

        """  """
        phy.profile_outputs.MODEM_CTRL5_RESYNCBAUDTRANS.override = 0

        """ For Ocelot, need to force adc clock mode to be same as bobcat """
        phy.profile_inputs.adc_clock_mode.value = model.vars.adc_clock_mode.var_enum.VCODIV

        # Derived empirically to improve wifi blocking performance
        # https://confluence.silabs.com/display/RAIL/Panther+Weaksymbols+WifiBlocker+Characterization
        phy.profile_outputs.MODEM_CTRL2_SQITHRESH.override = 56

    def PHY_Internal_IEEE802154_915MHz_cohdsa(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='802154 915 MHz cohdsa', phy_name=phy_name)

        self.IEEE802154_Internal_915MHz_cohdsa_base(phy, model)
        return phy