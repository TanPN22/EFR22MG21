from pyradioconfig.calculator_model_framework.interfaces.iphy import IPhy
from pyradioconfig.parts.panther.phys.PHY_internal_base import Phy_Internal_Base
from pyradioconfig.parts.common.phys.phy_common import PHY_COMMON_FRAME_INTERNAL

class PHYS_Studio_Base_Ocelot(IPhy):

    ##########2FSK PHYS##########

    #Base Functions

    def Studio_2GFSK_base(self, phy, model):

        # Required Inputs
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK2
        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 40
        phy.profile_inputs.rx_xtal_error_ppm.value = 10
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 0.5
        phy.profile_inputs.syncword_0.value = 0xf68d
        phy.profile_inputs.syncword_1.value = 0x0
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.tx_xtal_error_ppm.value = 10
        phy.profile_inputs.xtal_frequency_hz.value = 39000000

        # Common frame settings
        PHY_COMMON_FRAME_INTERNAL(phy, model)

    #Derivative PHYs

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-149
    def PHY_Studio_915M_2GFSK_2Mbps_500K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 2Mbps 500K', phy_name=phy_name)

        # Start with the base function
        self.Studio_2GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 2000000
        phy.profile_inputs.deviation.value = 500000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 915000000

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-150
    def PHY_Studio_915M_2GFSK_500Kbps_175K_mi0p7(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 500Kbps 175K', phy_name=phy_name)

        # Start with the base function
        self.Studio_2GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.deviation.value = 175000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 915000000

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-146
    def PHY_Studio_868M_2GFSK_38p4Kbps_20K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='868M 2GFSK 38.4Kbps 20K', phy_name=phy_name)

        # Start with the base function
        self.Studio_2GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 38400
        phy.profile_inputs.deviation.value = 20000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 868000000

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-145
    def PHY_Datasheet_868M_2GFSK_2p4Kbps_1p2K_ETSI(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='868MHz 2GFSK 2.4Kbps 1.2KHz ETSI',
                            phy_name=phy_name)

        # Start with the base function
        self.Studio_2GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.channel_spacing_hz.value = 25000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 868000000

        # Define PHY as ETSI compatible
        phy.profile_inputs.etsi_cat1_compatible.value = model.vars.etsi_cat1_compatible.var_enum.Band_868

        # For the ETSI PHYs, define the ETSI BW that will be used to accomodate frequency tolerance
        # Do this by setting the bandwidth explicitly instead of the xtal error
        phy.profile_inputs.bandwidth_hz.value = 10000

        # Set the xtal tol to match the forced AFC bandwidth
        phy.profile_inputs.rx_xtal_error_ppm.value = 3
        phy.profile_inputs.tx_xtal_error_ppm.value = 3

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-190
    def PHY_Studio_868M_2GFSK_600bps_800(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='868MHz 2GFSK 600bps 800Hz', phy_name=phy_name)

        # Start with the base function
        self.Studio_2GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 600
        phy.profile_inputs.deviation.value = 800

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 868000000

        # Use lower xtal tol only for low deviation PHYs
        # 20ppm (default RX+TX tol) here is 17.36kHz which is much too wide compared to the deviation of this PHY
        phy.profile_inputs.rx_xtal_error_ppm.value = 5
        phy.profile_inputs.tx_xtal_error_ppm.value = 5

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-78
    def PHY_Studio_490M_2GFSK_38p4Kbps_20K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='490MHz 2GFSK 38.4Kbps 20KHz', phy_name=phy_name)

        # Start with the base function
        self.Studio_2GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 38400
        phy.profile_inputs.deviation.value = 20000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 490000000

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-81
    def PHY_Datasheet_490M_2GFSK_10Kbps_25K_20ppm(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='490MHz 2GFSK 10Kbps 25KHz 20ppm', phy_name=phy_name)

        # Start with the base function
        self.Studio_2GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 10000
        phy.profile_inputs.deviation.value = 25000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 490000000

        # This PHY has a special requirement of 20ppm rx/tx tol (per Apps)
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.tx_xtal_error_ppm.value = 20

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-76
    def PHY_Studio_490M_2GFSK_10Kbps_5K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='490MHz 2GFSK 10Kbps 5KHz', phy_name=phy_name)

        # Start with the base function
        self.Studio_2GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 10000
        phy.profile_inputs.deviation.value = 5000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 490000000

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-77
    def PHY_Studio_490M_2GFSK_2p4Kbps_1p2K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='490MHz 2GFSK 2.4Kbps 1.2KHz', phy_name=phy_name)

        # Start with the base function
        self.Studio_2GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 490000000

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-58
    def PHY_Studio_434M_2GFSK_100Kbps_50K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='434M 2GFSK 100Kbps 50K', phy_name=phy_name)

        # Start with the base function
        self.Studio_2GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 100000
        phy.profile_inputs.deviation.value = 50000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 434000000

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-60
    def PHY_Studio_434M_2GFSK_50Kbps_25K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='434M 2GFSK 50Kbps 25K', phy_name=phy_name)

        # Start with the base function
        self.Studio_2GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 50000
        phy.profile_inputs.deviation.value = 25000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 434000000

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-59
    def PHY_Studio_434M_2GFSK_2p4Kbps_1p2K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='434M 2GFSK 2.4Kbps 1.2K', phy_name=phy_name)

        # Start with the base function
        self.Studio_2GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 434000000

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-39
    def PHY_Studio_315M_2GFSK_38p4Kbps_20K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='315MHz 2GFSK 38.4Kbps 20KHz', phy_name=phy_name)

        # Start with the base function
        self.Studio_2GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 38400
        phy.profile_inputs.deviation.value = 20000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 315000000

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-25
    def PHY_Datasheet_169M_2GFSK_2p4Kbps_1p2K_ETSI(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='169MHz 2GFSK 2.4Kbps 1.2KHz ETSI',
                            phy_name=phy_name)

        # Start with the base function
        self.Studio_2GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.channel_spacing_hz.value = 25000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 169000000

        # Define PHY as ETSI compatible
        phy.profile_inputs.etsi_cat1_compatible.value = model.vars.etsi_cat1_compatible.var_enum.Band_169

        # For the ETSI PHYs, define the ETSI BW that will be used to accomodate frequency tolerance
        # Do this by setting the bandwidth explicitly instead of the xtal error
        phy.profile_inputs.bandwidth_hz.value = 10000

        # Set the xtal tol to match the forced AFC bandwidth
        phy.profile_inputs.rx_xtal_error_ppm.value = 15
        phy.profile_inputs.tx_xtal_error_ppm.value = 15

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-24
    def PHY_Studio_169M_2GFSK_2p4Kbps_1p2K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='169MHz 2GFSK 2.4Kbps 1.2KHz', phy_name=phy_name)

        # Start with the base function
        self.Studio_2GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 169000000

        return phy

    ##########4FSK PHYS##########

    # Base Functions

    def Studio_4GFSK_base(self, phy, model):

        # Required Inputs
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK4
        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 40
        phy.profile_inputs.rx_xtal_error_ppm.value = 10
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 1.0
        phy.profile_inputs.syncword_0.value = 0xf68d
        phy.profile_inputs.syncword_1.value = 0x0
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.tx_xtal_error_ppm.value = 10
        phy.profile_inputs.xtal_frequency_hz.value = 39000000

        # Common frame settings
        PHY_COMMON_FRAME_INTERNAL(phy, model)

    # Derivative PHYs

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-151
    def PHY_Studio_915M_4GFSK_200Kbps_16p6K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 4GFSK 200Kbps 16.6K', phy_name=phy_name)

        # Start with the base function
        self.Studio_4GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 200000
        phy.profile_inputs.deviation.value = 16666 #Inner symbol deviation

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 915000000

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-65
    def PHY_Studio_434M_4GFSK_50Kbps_8p33K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='434M 4GFSK 50Kbps 8.33K', phy_name=phy_name)

        # Start with the base function
        self.Studio_4GFSK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 50000
        phy.profile_inputs.deviation.value = 8330 #Inner symbol deviation

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 434000000

        return phy

    ##########OOK PHYS##########

    # Base Functions

    def Studio_OOK_base(self, phy, model):
        # Required Inputs
        phy.profile_inputs.baudrate_tol_ppm.value = 1000
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.deviation.value = 0
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.OOK
        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 40
        phy.profile_inputs.rx_xtal_error_ppm.value = 10
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.NONE
        phy.profile_inputs.shaping_filter_param.value = 1.5
        phy.profile_inputs.syncword_0.value = 0xf68d
        phy.profile_inputs.syncword_1.value = 0x0
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.tx_xtal_error_ppm.value = 10
        phy.profile_inputs.xtal_frequency_hz.value = 39000000

        # Common frame settings
        PHY_COMMON_FRAME_INTERNAL(phy, model)

    # Derivative PHYs

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-147
    def PHY_Studio_915M_OOK_120kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M OOK 120kbps', phy_name=phy_name)

        # Start with the base function
        self.Studio_OOK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 120000
        phy.profile_inputs.bandwidth_hz.value = 350000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 915000000

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-152
    def PHY_Studio_915M_OOK_4p8kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M OOK 4.8kbps', phy_name=phy_name)

        # Start with the base function
        self.Studio_OOK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 4800
        phy.profile_inputs.bandwidth_hz.value = 350000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 915000000

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-45
    def PHY_Studio_433M_OOK_4p8kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='433M OOK 4.8kbps', phy_name=phy_name)

        # Start with the base function
        self.Studio_OOK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 4800
        phy.profile_inputs.bandwidth_hz.value = 350000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 433920000

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-41
    def PHY_Studio_315M_OOK_40kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='315M OOK 40kbps', phy_name=phy_name)

        # Start with the base function
        self.Studio_OOK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 40000
        phy.profile_inputs.bandwidth_hz.value = 350000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 315000000

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-36
    def PHY_Studio_315M_OOK_4p8kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='315M OOK 4.8kbps', phy_name=phy_name)

        # Start with the base function
        self.Studio_OOK_base(phy, model)

        # Add data-rate specific parameters
        phy.profile_inputs.bitrate.value = 4800
        phy.profile_inputs.bandwidth_hz.value = 350000

        # Add band-specific parameters
        phy.profile_inputs.base_frequency_hz.value = 315000000

        return phy

    ##########GMSK PHYS##########

    # Base Functions

    def Studio_GMSK_base(self, phy, model):
        """ Modulation Type """
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.MSK

        """ Symbol Mapping and Encoding """
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED

        """ Baudrate """
        phy.profile_inputs.baudrate_tol_ppm.value = 0

        """ DSSS Parameters """
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0

        """ Shaping Filter Parameters """
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 0.5

        """ Preamble Parameters """
        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 40

        """ Syncword Parameters """
        phy.profile_inputs.syncword_0.value = 0xf68d
        phy.profile_inputs.syncword_1.value = 0x0
        phy.profile_inputs.syncword_length.value = 16

        """ XO Parameters """
        phy.profile_inputs.xtal_frequency_hz.value = 39000000
        phy.profile_inputs.rx_xtal_error_ppm.value = 10
        phy.profile_inputs.tx_xtal_error_ppm.value = 10

        # Common frame settings
        PHY_COMMON_FRAME_INTERNAL(phy, model)

    # Owner: Young-Joon Choi
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-189
    def PHY_Studio_868M_GMSK_500Kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='868M GMSK 500Kbps', phy_name=phy_name)

        # : Common base function for GMSK PHYs
        self.Studio_GMSK_base(phy, model)

        """ Frequency Planning """
        phy.profile_inputs.base_frequency_hz.value = 868000000
        phy.profile_inputs.channel_spacing_hz.value = 1000000

        """ Datarate / Bandwidth """
        phy.profile_inputs.bitrate.value = 500000
        # : modulation index = 0.5 = 2 * deviation / data_rate for GMSK. Therefore, deviation = 0.25 * data_rate
        phy.profile_inputs.deviation.value = 125000
        return phy
    pass # : End PHY_Studio_868M_GMSK_500Kbps

    ##########TBD PHYs##########

    def PHY_Datasheet_868M_2GFSK_2p4Kbps_1p2K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='868M 2GFSK 2.4Kbps 1.2K', phy_name=phy_name)

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # phy.profile_inputs.bandwidth_hz.value = 4800
        phy.profile_inputs.base_frequency_hz.value = 868000000
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.if_frequency_hz.value = 400000

        return phy


    def PHY_Datasheet_868M_2GFSK_500Kbps_125K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='868M 2GFSK 500Kbps 125K', phy_name=phy_name)

        Phy_Internal_Base.GFSK_915M_base(phy, model)
        phy.profile_inputs.base_frequency_hz.value = 868000000

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.deviation.value = 125000
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON

        return phy

    def PHY_Datasheet_915M_2GFSK_600bps_300(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 600bps 300', phy_name=phy_name)

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 600
        phy.profile_inputs.deviation.value = 300
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.errors_in_timing_window.value = 1
        phy.profile_inputs.timing_sample_threshold.value = 12

        return phy

    def PHY_Datasheet_915M_2GFSK_100Kbps_50K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 100Kbps 50K', phy_name=phy_name)

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 100000
        phy.profile_inputs.deviation.value = 50000
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.if_frequency_hz.value = 300000

        return phy

    def PHY_Datasheet_915M_2GFSK_200Kbps_100K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 200Kbps 100K', phy_name=phy_name)

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 200000
        phy.profile_inputs.deviation.value = 100000
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.agc_power_target.value = -8
        phy.profile_inputs.errors_in_timing_window.value = 1
        phy.profile_inputs.timing_sample_threshold.value = 12

        return phy

    def PHY_Datasheet_915M_2GFSK_50Kbps_25K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 50Kbps 25K', phy_name=phy_name)

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 50000
        phy.profile_inputs.deviation.value = 25000
        #phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        #phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        #phy.profile_inputs.if_frequency_hz.value = 400000
        phy.profile_inputs.bandwidth_hz.alue = 100000

        return phy


    def PHY_Datasheet_915M_4GFSK_400Kbps_33p3K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 4GFSK 400Kbps 33.3K', phy_name=phy_name)
        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.base_frequency_hz.value = 915000000
        phy.profile_inputs.bitrate.value = 400000
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.deviation.value = 33333
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_LOCK_AT_PREAMBLE_DETECT
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK4
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 1.0

        phy.profile_inputs.bandwidth_hz.value = 370000
        phy.profile_inputs.if_frequency_hz.value = 400000
        phy.profile_inputs.agc_power_target.value = -8
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.timing_resync_period.value = 3
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.symbols_in_timing_window.value = 15

        return phy

    def PHY_Datasheet_169M_2GFSK_38p4Kbps_20K(self, model, phy_name=None):

        phy = self._makePhy(model, model.profiles.Base, readable_name='169MHz 2GFSK 38.4Kbps 20KHz', phy_name=phy_name)

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = 169000000
        phy.profile_inputs.bitrate.value = 38400
        phy.profile_inputs.deviation.value = 20000
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.bandwidth_hz.value = 75000

        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON

        return phy

    def PHY_Datasheet_490M_2GFSK_100Kbps_50K(self, model, phy_name=None):

        phy = self._makePhy(model, model.profiles.Base, readable_name='490MHz 2GFSK 100Kbps 50KHz', phy_name=phy_name)
        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = 490000000
        phy.profile_inputs.bitrate.value = 100000
        phy.profile_inputs.deviation.value = 50000
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 20

        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.if_frequency_hz.value = 400000

        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON

        return phy

    def PHY_Datasheet_434M_4GFSK_9p6Kbps_0p8K(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='434M 4GFSK 9.6Kbps 0.8KHz', phy_name=phy_name)

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.base_frequency_hz.value = 434000000
        phy.profile_inputs.bitrate.value = 9600
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.deviation.value = 800

        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_LOCK_AT_PREAMBLE_DETECT
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK4
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 1.0

        phy.profile_inputs.bandwidth_hz.value = 8500
        phy.profile_inputs.if_frequency_hz.value = 400000
        phy.profile_inputs.agc_power_target.value = -8
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.timing_resync_period.value = 3

        return phy

    def PHY_Datasheet_315M_2GFSK_2p4Kbps_1p2K(self, model, phy_name=None):

        phy = self._makePhy(model, model.profiles.Base, readable_name='315MHz 2GFSK 2.4Kbps 1.2KHz', phy_name=phy_name)

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = 315000000
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 12
        phy.profile_inputs.freq_offset_hz.value = 4000
        phy.profile_inputs.timing_sample_threshold.value = 8


        return phy

    def PHY_Datasheet_315M_2GFSK_500Kbps_125K(self, model, phy_name=None):

        phy = self._makePhy(model, model.profiles.Base, readable_name='315MHz 2GFSK 500Kbps 125KHz', phy_name=phy_name)

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = 315000000
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.deviation.value = 125000

        phy.profile_inputs.number_of_timing_windows.value = 2
        phy.profile_inputs.symbols_in_timing_window.value = 8
        phy.profile_inputs.afc_step_scale.value = 0.75

        return phy

    def PHY_Datasheet_285M_2GFSK_2p4Kbps_1p2K(self, model, phy_name=None):

        phy = self._makePhy(model, model.profiles.Base, readable_name='285MHz 2GFSK 2.4Kbps 1.2KHz', phy_name=phy_name)

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = 285000000
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.timing_detection_threshold.value = 12
        phy.profile_inputs.freq_offset_hz.value = 4000
        phy.profile_inputs.timing_sample_threshold.value = 8

        return phy

    def PHY_Datasheet_285M_2GFSK_500Kbps_125K(self, model, phy_name=None):

        phy = self._makePhy(model, model.profiles.Base, readable_name='285MHz 2GFSK 500Kbps 125KHz', phy_name=phy_name)

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        phy.profile_inputs.base_frequency_hz.value = 285000000
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.deviation.value = 125000
        phy.profile_inputs.number_of_timing_windows.value = 2
        phy.profile_inputs.symbols_in_timing_window.value = 8
        phy.profile_inputs.afc_step_scale.value = 0.75

        return phy

    def PHY_Datasheet_915M_2GFSK_300bps_300(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 300bps 300Hz deviation')

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 300
        phy.profile_inputs.deviation.value = 300
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.symbols_in_timing_window.value = 32
        return phy

    def PHY_Datasheet_915M_2GFSK_100Kbps_50K_antdiv(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 100Kbps 50K antenna diversity', phy_name=phy_name)

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 100000
        phy.profile_inputs.deviation.value = 50000
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.if_frequency_hz.value = 300000

        phy.profile_inputs.preamble_length.value = 120
        phy.profile_inputs.number_of_timing_windows.value = 1
        phy.profile_inputs.rssi_period.value = 3
        phy.profile_inputs.timing_sample_threshold.value = 5

        #TODO: FIXME: 750KHz is the narrowest TX BW Series 2 has defined..... Much larger than Series 1
        phy.profile_inputs.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_750KHz

        phy.profile_inputs.antdivmode.value = model.vars.antdivmode.var_enum.ANTSELRSSI
        phy.profile_inputs.antdivrepeatdis.value = model.vars.antdivrepeatdis.var_enum.REPEATFIRST

        return phy

    def PHY_Datasheet_915M_2GFSK_200Kbps_100K_antdiv(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='915M 2GFSK 200Kbps 100K antenna diversity', phy_name=phy_name)

        Phy_Internal_Base.GFSK_915M_base(phy, model)

        # Add values to existing inputs
        phy.profile_inputs.bitrate.value = 200000
        phy.profile_inputs.deviation.value = 100000
        phy.profile_inputs.timing_detection_threshold.value = 20
        phy.profile_inputs.timing_sample_threshold.value = 12
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.src_disable.value = model.vars.src_disable.var_enum.DISABLED
        phy.profile_inputs.if_frequency_hz.value = 300000

        phy.profile_inputs.preamble_length.value = 120
        phy.profile_inputs.number_of_timing_windows.value = 1
        phy.profile_inputs.rssi_period.value = 3
        phy.profile_inputs.timing_sample_threshold.value = 10

        phy.profile_inputs.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_750KHz
        phy.profile_inputs.antdivmode.value = model.vars.antdivmode.var_enum.ANTSELRSSI
        phy.profile_inputs.antdivrepeatdis.value = model.vars.antdivrepeatdis.var_enum.REPEATFIRST

        return phy

    ##########SUN FSK PHYs (exposed using Base Profile)##########

    def SUN_FSK_2GFSK_base(self, phy, model):

        # General Inputs
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.fec_en.value = model.vars.fec_en.var_enum.NONE
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0  # Table 20.8.SUN 2-FSK symbol encoding
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK2
        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian  # 17.2.4 GFSK modulation
        phy.profile_inputs.shaping_filter_param.value = 0.5
        # TODO: Do we support both uncoded and coded?  If so, need to create additional config's
        phy.profile_inputs.syncword_0.value = 0b1001000001001110  # Table 20.2.SUN FSK PHY SFD values for 2-FSK (uncoded), page 494
        #phy.profile_inputs.syncword_0.value = 0b0110111101001110  # Table 20.2.SUN FSK PHY SFD values for 2-FSK (FEC coded), page 494
        phy.profile_inputs.syncword_1.value = 0
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.syncword_tx_skip.value = False
        phy.profile_inputs.xtal_frequency_hz.value = 39000000

        # Packet Inputs
        phy.profile_inputs.frame_length_type.value = model.vars.frame_length_type.var_enum.VARIABLE_LENGTH
        phy.profile_inputs.frame_bitendian.value = model.vars.frame_bitendian.var_enum.MSB_FIRST
        phy.profile_inputs.payload_crc_en.value = True

        # Variable length includes header
        phy.profile_inputs.header_calc_crc.value = True
        phy.profile_inputs.header_en.value = True
        phy.profile_inputs.header_size.value = 8
        phy.profile_inputs.header_white_en.value = True  # 17.2.3 Data whitening. Support for data whitening is optional.

        # Whitening Inputs
        phy.profile_inputs.white_poly.value = model.vars.white_poly.var_enum.PN9
        phy.profile_inputs.white_seed.value = 0b111111111
        phy.profile_inputs.white_output_bit.value = 0

        # CRC Inputs
        phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_input_order.value = model.vars.crc_input_order.var_enum.MSB_FIRST
        phy.profile_inputs.crc_invert.value = False
        phy.profile_inputs.crc_pad_input.value = False

    def SUN_FSK_4GFSK_base(self, phy, model):
        # General Inputs
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.fec_en.value = model.vars.fec_en.var_enum.NONE
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK4 # Table 20.9.SUN 4-FSK symbol encoding
        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian  # 17.2.4 GFSK modulation
        phy.profile_inputs.shaping_filter_param.value = 0.5
        # TODO: Do we support both uncoded and coded?  If so, need to create additional config's
        phy.profile_inputs.syncword_0.value = 0b01111101111111110111010111111101  # Table 20.2.SUN FSK PHY SFD values for 2-FSK, page 494
        phy.profile_inputs.syncword_1.value = 0
        phy.profile_inputs.syncword_length.value = 32
        phy.profile_inputs.syncword_tx_skip.value = False
        phy.profile_inputs.xtal_frequency_hz.value = 39000000

        # Packet Inputs
        phy.profile_inputs.frame_length_type.value = model.vars.frame_length_type.var_enum.VARIABLE_LENGTH
        phy.profile_inputs.frame_bitendian.value = model.vars.frame_bitendian.var_enum.MSB_FIRST
        phy.profile_inputs.payload_crc_en.value = True

        # Variable length includes header
        phy.profile_inputs.header_calc_crc.value = True
        phy.profile_inputs.header_en.value = True
        phy.profile_inputs.header_size.value = 8
        phy.profile_inputs.header_white_en.value = True  # 17.2.3 Data whitening. Support for data whitening is optional.

        # Whitening Inputs
        phy.profile_inputs.white_poly.value = model.vars.white_poly.var_enum.PN9
        phy.profile_inputs.white_seed.value = 0b111111111
        phy.profile_inputs.white_output_bit.value = 0

        # CRC Inputs
        phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_input_order.value = model.vars.crc_input_order.var_enum.MSB_FIRST
        phy.profile_inputs.crc_invert.value = False
        phy.profile_inputs.crc_pad_input.value = False

    def PHY_IEEE802154_SUN_FSK_169MHz_2FSK_2p4kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='IEEE 802.15.4 SUN FSK 169MHz 2FSK 2.4kbps mi=2.0', phy_name=phy_name)

        phy.profile_inputs.base_frequency_hz.value =  169406250 # Freq mapping Table 10.10. Channel numbering for SUN PHYs
        phy.profile_inputs.channel_spacing_hz.value = 12500
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK2
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0  # Table 20.8.SUN 2-FSK symbol encoding
        phy.profile_inputs.bitrate.value = 2400
        phy.profile_inputs.deviation.value = 2400  # 2400*2.0 / 2

        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 4*16 # phyFskPreambleLength 4-64 repetitions of the preamble pattern (which is 16 bits)
        phy.profile_inputs.syncword_0.value = 0b0110111101001110  # Table 20.2.SUN FSK PHY SFD values for 2-FSK, page 494
        phy.profile_inputs.syncword_1.value = 0
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.syncword_tx_skip.value = False

        phy.profile_inputs.header_white_en.value = True # 17.2.3 Data whitening. Support for data whitening is optional.
        phy.profile_inputs.white_poly.value = model.vars.white_poly.var_enum.PN9
        phy.profile_inputs.white_seed.value = 0b111111111
        phy.profile_inputs.white_output_bit.value = 0

        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian # 17.2.4 GFSK modulation
        phy.profile_inputs.shaping_filter_param.value = 0.5

        phy.profile_inputs.xtal_frequency_hz.value = 38400000
        phy.profile_inputs.rx_xtal_error_ppm.value = 16
        phy.profile_inputs.tx_xtal_error_ppm.value = 16

        phy.profile_inputs.crc_poly.value = model.vars.crc_poly.var_enum.BCH15_11
        phy.profile_inputs.crc_seed.value = 0xFF
        phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_pad_input.value = False
        phy.profile_inputs.crc_input_order.value = model.vars.crc_input_order.var_enum.MSB_FIRST
        phy.profile_inputs.crc_invert.value = False

        phy.profile_inputs.fec_en.value = model.vars.fec_en.var_enum.NONE
        phy.profile_inputs.frame_bitendian.value = model.vars.frame_bitendian.var_enum.MSB_FIRST

        # change to fixed length is mainly for test purpose (performance comparison), if use variable length, need to pass length parameter to packet builder like ZigBee
        phy.profile_inputs.frame_length_type.value = model.vars.frame_length_type.var_enum.VARIABLE_LENGTH
        phy.profile_inputs.payload_crc_en.value = True

        # Absent from Ocelot, was used on Nerio
        # phy.profile_inputs.payload_excludesubframewcnt_en.value = False

        # used fixed length, no header needed, same for header_CRC
        phy.profile_inputs.header_en.value = True
        phy.profile_inputs.header_size.value = 8
        phy.profile_inputs.header_calc_crc.value = True

        # Add required inputs to allow calculators to run
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED

        # Forces from FPGA verification
        phy.profile_inputs.number_of_timing_windows.value = 1 # force ADDTIMSEQ=0
        phy.profile_inputs.timing_sample_threshold.value = 0  # force TSAMPMODE=0

        return phy

    def PHY_IEEE802154_SUN_FSK_169MHz_2FSK_4p8kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='IEEE 802.15.4 SUN FSK 169MHz 2FSK 4.8kbps mi=0.5', phy_name=phy_name)

        phy.profile_inputs.base_frequency_hz.value = 169406250 # Freq mapping Table 10.10. Channel numbering for SUN PHYs
        phy.profile_inputs.channel_spacing_hz.value = 12500
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK2
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0  # Table 20.8.SUN 2-FSK symbol encoding
        phy.profile_inputs.bitrate.value = 4800
        phy.profile_inputs.deviation.value = 1200  # 4800*0.5 / 2

        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 4*16 # phyFskPreambleLength 4-64 repetitions of the preamble pattern (which is 16 bits)
        phy.profile_inputs.syncword_0.value = 0b0110111101001110  # Table 20.2.SUN FSK PHY SFD values for 2-FSK, page 494
        phy.profile_inputs.syncword_1.value = 0
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.syncword_tx_skip.value = False



        phy.profile_inputs.header_white_en.value = True # 17.2.3 Data whitening. Support for data whitening is optional.
        phy.profile_inputs.white_poly.value = model.vars.white_poly.var_enum.PN9
        phy.profile_inputs.white_seed.value = 0b111111111
        phy.profile_inputs.white_output_bit.value = 0

        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian # 17.2.4 GFSK modulation
        phy.profile_inputs.shaping_filter_param.value = 0.5

        phy.profile_inputs.xtal_frequency_hz.value = 38400000
        phy.profile_inputs.rx_xtal_error_ppm.value = 8
        phy.profile_inputs.tx_xtal_error_ppm.value = 8


        phy.profile_inputs.crc_poly.value = model.vars.crc_poly.var_enum.BCH15_11
        phy.profile_inputs.crc_seed.value = 0xFF
        phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_pad_input.value = False
        phy.profile_inputs.crc_input_order.value = model.vars.crc_input_order.var_enum.MSB_FIRST
        phy.profile_inputs.crc_invert.value = False

        phy.profile_inputs.fec_en.value = model.vars.fec_en.var_enum.NONE
        phy.profile_inputs.frame_bitendian.value = model.vars.frame_bitendian.var_enum.MSB_FIRST

        # change to fixed length is mainly for test purpose (performance comparison), if use variable length, need to pass length parameter to packet builder like ZigBee
        phy.profile_inputs.frame_length_type.value = model.vars.frame_length_type.var_enum.VARIABLE_LENGTH
        phy.profile_inputs.payload_crc_en.value = True

        # Absent from Ocelot, was used on Nerio
        # phy.profile_inputs.payload_excludesubframewcnt_en.value = False

        # used fixed length, no header needed, same for header_CRC
        phy.profile_inputs.header_en.value = True
        phy.profile_inputs.header_size.value = 8
        phy.profile_inputs.header_calc_crc.value = True

        # Add required inputs to allow calculators to run
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED

        ######## Viterbi Demod
        phy.profile_inputs.target_osr.value = 5
        #
        # phy.profile_outputs.MODEM_VTCORRCFG1_KSI3SWENABLE.override = 1
        # phy.profile_outputs.MODEM_VTCORRCFG1_VITERBIKSI3WB.override = 32
        # phy.profile_outputs.MODEM_VITERBIDEMOD_VITERBIKSI3.override = 28

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-29
    def PHY_IEEE802154_SUN_FSK_169MHz_4FSK_9p6kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base,
                            readable_name='IEEE 802.15.4 SUN FSK 169MHz 4FSK 9.6kbps mi=0.33', phy_name=phy_name)

        phy.profile_inputs.base_frequency_hz.value = 169406250  # Freq mapping Table 10.10. Channel numbering for SUN PHYs
        phy.profile_inputs.channel_spacing_hz.value = 12500
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK4
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0  # Table 20.9.SUN 4-FSK symbol encoding
        phy.profile_inputs.bitrate.value = 9600
        phy.profile_inputs.deviation.value = 800

        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 4 * 32  # phyFskPreambleLength 4-64 repetitions of the preamble pattern (which is 16 bits)
        phy.profile_inputs.syncword_0.value = 0b01111101111111110111010111111101  # Table 20.2.SUN FSK PHY SFD values for 2-FSK, page 494
        phy.profile_inputs.syncword_1.value = 0
        phy.profile_inputs.syncword_length.value = 32
        phy.profile_inputs.syncword_tx_skip.value = False

        phy.profile_inputs.header_white_en.value = True  # 17.2.3 Data whitening. Support for data whitening is optional.
        phy.profile_inputs.white_poly.value = model.vars.white_poly.var_enum.PN9
        phy.profile_inputs.white_seed.value = 0b111111111
        phy.profile_inputs.white_output_bit.value = 0

        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian  # 17.2.4 GFSK modulation
        phy.profile_inputs.shaping_filter_param.value = 0.5

        phy.profile_inputs.xtal_frequency_hz.value = 39000000
        phy.profile_inputs.rx_xtal_error_ppm.value = 6  # 20.6.3 Equation for Rsymb = 4800, mi=0.333, rnd up to 6
        phy.profile_inputs.tx_xtal_error_ppm.value = 6  # 20.6.3 Equation for Rsymb = 4800, mi=0.333, rnd up to 6

        phy.profile_inputs.crc_poly.value = model.vars.crc_poly.var_enum.BCH15_11
        phy.profile_inputs.crc_seed.value = 0xFF
        phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_pad_input.value = False
        phy.profile_inputs.crc_input_order.value = model.vars.crc_input_order.var_enum.MSB_FIRST
        phy.profile_inputs.crc_invert.value = False

        phy.profile_inputs.fec_en.value = model.vars.fec_en.var_enum.NONE
        phy.profile_inputs.frame_bitendian.value = model.vars.frame_bitendian.var_enum.MSB_FIRST

        phy.profile_inputs.frame_length_type.value = model.vars.frame_length_type.var_enum.VARIABLE_LENGTH
        phy.profile_inputs.payload_crc_en.value = True

        # used fixed length, no header needed, same for header_CRC
        phy.profile_inputs.header_en.value = True
        phy.profile_inputs.header_size.value = 8
        phy.profile_inputs.header_calc_crc.value = True

        # Add required inputs to allow calculators to run
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-61
    def PHY_IEEE802154_SUN_FSK_450MHz_2FSK_4p8kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base,
                            readable_name='IEEE 802.15.4 SUN FSK 450MHz 2FSK 4.8kbps mi=1.0', phy_name=phy_name)

        phy.profile_inputs.base_frequency_hz.value = 450006250  # Freq mapping Table 10.10. Channel numbering for SUN PHYs
        phy.profile_inputs.channel_spacing_hz.value = 12500
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK2
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0  # Table 20.8.SUN 2-FSK symbol encoding
        phy.profile_inputs.bitrate.value = 4800
        phy.profile_inputs.deviation.value = 2400  # 4800*1.0 / 2

        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 4 * 16  # phyFskPreambleLength 4-64 repetitions of the preamble pattern (which is 16 bits)
        phy.profile_inputs.syncword_0.value = 0b0110111101001110  # Table 20.2.SUN FSK PHY SFD values for 2-FSK, page 494
        phy.profile_inputs.syncword_1.value = 0
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.syncword_tx_skip.value = False

        phy.profile_inputs.header_white_en.value = True  # 17.2.3 Data whitening. Support for data whitening is optional.
        phy.profile_inputs.white_poly.value = model.vars.white_poly.var_enum.PN9
        phy.profile_inputs.white_seed.value = 0b111111111
        phy.profile_inputs.white_output_bit.value = 0

        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian  # 17.2.4 GFSK modulation
        phy.profile_inputs.shaping_filter_param.value = 0.5

        phy.profile_inputs.xtal_frequency_hz.value = 38400000
        phy.profile_inputs.rx_xtal_error_ppm.value = 6
        phy.profile_inputs.tx_xtal_error_ppm.value = 6

        phy.profile_inputs.crc_poly.value = model.vars.crc_poly.var_enum.BCH15_11
        phy.profile_inputs.crc_seed.value = 0xFF
        phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_pad_input.value = False
        phy.profile_inputs.crc_input_order.value = model.vars.crc_input_order.var_enum.MSB_FIRST
        phy.profile_inputs.crc_invert.value = False

        phy.profile_inputs.fec_en.value = model.vars.fec_en.var_enum.NONE
        phy.profile_inputs.frame_bitendian.value = model.vars.frame_bitendian.var_enum.MSB_FIRST

        phy.profile_inputs.frame_length_type.value = model.vars.frame_length_type.var_enum.VARIABLE_LENGTH
        phy.profile_inputs.payload_crc_en.value = True

        # used fixed length, no header needed, same for header_CRC
        phy.profile_inputs.header_en.value = True
        phy.profile_inputs.header_size.value = 8
        phy.profile_inputs.header_calc_crc.value = True

        # Add required inputs to allow calculators to run
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-62
    def PHY_IEEE802154_SUN_FSK_450MHz_4FSK_9p6kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base,
                            readable_name='IEEE 802.15.4 SUN FSK 450MHz 4FSK 9.6kbps mi=0.33', phy_name=phy_name)

        phy.profile_inputs.base_frequency_hz.value = 450006250  # Freq mapping Table 10.10. Channel numbering for SUN PHYs
        phy.profile_inputs.channel_spacing_hz.value = 12500
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK4
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0  # Table 20.9.SUN 4-FSK symbol encoding
        phy.profile_inputs.bitrate.value = 9600
        phy.profile_inputs.deviation.value = 800

        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 4 * 32  # phyFskPreambleLength 4-64 repetitions of the preamble pattern (which is 16 bits)
        phy.profile_inputs.syncword_0.value = 0b01111101111111110111010111111101  # Table 20.2.SUN FSK PHY SFD values for 2-FSK, page 494
        phy.profile_inputs.syncword_1.value = 0
        phy.profile_inputs.syncword_length.value = 32
        phy.profile_inputs.syncword_tx_skip.value = False

        phy.profile_inputs.header_white_en.value = True  # 17.2.3 Data whitening. Support for data whitening is optional.
        phy.profile_inputs.white_poly.value = model.vars.white_poly.var_enum.PN9
        phy.profile_inputs.white_seed.value = 0b111111111
        phy.profile_inputs.white_output_bit.value = 0

        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian  # 17.2.4 GFSK modulation
        phy.profile_inputs.shaping_filter_param.value = 0.5

        phy.profile_inputs.xtal_frequency_hz.value = 39000000
        phy.profile_inputs.rx_xtal_error_ppm.value = 2 * 3  # adding *3 in case standard mod index is incorrect
        phy.profile_inputs.tx_xtal_error_ppm.value = 2 * 3

        phy.profile_inputs.crc_poly.value = model.vars.crc_poly.var_enum.BCH15_11
        phy.profile_inputs.crc_seed.value = 0xFF
        phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_pad_input.value = False
        phy.profile_inputs.crc_input_order.value = model.vars.crc_input_order.var_enum.MSB_FIRST
        phy.profile_inputs.crc_invert.value = False

        phy.profile_inputs.fec_en.value = model.vars.fec_en.var_enum.NONE
        phy.profile_inputs.frame_bitendian.value = model.vars.frame_bitendian.var_enum.MSB_FIRST

        phy.profile_inputs.frame_length_type.value = model.vars.frame_length_type.var_enum.VARIABLE_LENGTH
        phy.profile_inputs.payload_crc_en.value = True

        # used fixed length, no header needed, same for header_CRC
        phy.profile_inputs.header_en.value = True
        phy.profile_inputs.header_size.value = 8
        phy.profile_inputs.header_calc_crc.value = True

        # Add required inputs to allow calculators to run
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED

        return phy

    def PHY_IEEE802154_SUN_FSK_779MHz_2FSK_100kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base,
                            readable_name='IEEE 802.15.4 SUN FSK 779MHz 2FSK 100kbps mi=1.0', phy_name=phy_name)

        phy.profile_inputs.base_frequency_hz.value = 779200000  # Freq mapping Table 10.10. Channel numbering for SUN PHYs
        phy.profile_inputs.channel_spacing_hz.value = 400000
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK2
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0  # Table 20.8.SUN 2-FSK symbol encoding
        phy.profile_inputs.bitrate.value = 100000
        phy.profile_inputs.deviation.value = 50000  # 100000*1.0 / 2

        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 4 * 16  # phyFskPreambleLength 4-64 repetitions of the preamble pattern (which is 16 bits)
        phy.profile_inputs.syncword_0.value = 0b0110111101001110  # Table 20.2.SUN FSK PHY SFD values for 2-FSK, page 494
        phy.profile_inputs.syncword_1.value = 0
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.syncword_tx_skip.value = False

        phy.profile_inputs.header_white_en.value = True  # 17.2.3 Data whitening. Support for data whitening is optional.
        phy.profile_inputs.white_poly.value = model.vars.white_poly.var_enum.PN9
        phy.profile_inputs.white_seed.value = 0b111111111
        phy.profile_inputs.white_output_bit.value = 0

        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian  # 17.2.4 GFSK modulation
        phy.profile_inputs.shaping_filter_param.value = 0.5

        phy.profile_inputs.xtal_frequency_hz.value = 38400000
        phy.profile_inputs.rx_xtal_error_ppm.value = 50
        phy.profile_inputs.tx_xtal_error_ppm.value = 50

        phy.profile_inputs.crc_poly.value = model.vars.crc_poly.var_enum.BCH15_11
        phy.profile_inputs.crc_seed.value = 0xFF
        phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_pad_input.value = False
        phy.profile_inputs.crc_input_order.value = model.vars.crc_input_order.var_enum.MSB_FIRST
        phy.profile_inputs.crc_invert.value = False

        phy.profile_inputs.fec_en.value = model.vars.fec_en.var_enum.NONE
        phy.profile_inputs.frame_bitendian.value = model.vars.frame_bitendian.var_enum.MSB_FIRST

        # change to fixed length is mainly for test purpose (performance comparison), if use variable length, need to pass length parameter to packet builder like ZigBee
        phy.profile_inputs.frame_length_type.value = model.vars.frame_length_type.var_enum.VARIABLE_LENGTH
        phy.profile_inputs.payload_crc_en.value = True

        # Absent from Ocelot, was used on Nerio
        # phy.profile_inputs.payload_excludesubframewcnt_en.value = False

        # used fixed length, no header needed, same for header_CRC
        phy.profile_inputs.header_en.value = True
        phy.profile_inputs.header_size.value = 8
        phy.profile_inputs.header_calc_crc.value = True

        # Add required inputs to allow calculators to run
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED

        return phy

    def PHY_IEEE802154_SUN_FSK_779MHz_4FSK_200kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base,
                            readable_name='IEEE 802.15.4 SUN FSK 779MHz 4FSK 200kbps mi=0.33', phy_name=phy_name)

        phy.profile_inputs.base_frequency_hz.value = 779400000  # Freq mapping Table 10.10. Channel numbering for SUN PHYs
        phy.profile_inputs.channel_spacing_hz.value = 400000
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK4
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0  # Table 20.9.SUN 4-FSK symbol encoding
        phy.profile_inputs.bitrate.value = 200000
        phy.profile_inputs.deviation.value = int(100000 / 6)

        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 4 * 32  # phyFskPreambleLength 4-64 repetitions of the preamble pattern (which is 16 bits)
        phy.profile_inputs.syncword_0.value = 0b01111101111111110111010111111101  # Table 20.2.SUN FSK PHY SFD values for 2-FSK, page 494
        phy.profile_inputs.syncword_1.value = 0
        phy.profile_inputs.syncword_length.value = 32
        phy.profile_inputs.syncword_tx_skip.value = False

        phy.profile_inputs.header_white_en.value = True  # 17.2.3 Data whitening. Support for data whitening is optional.
        phy.profile_inputs.white_poly.value = model.vars.white_poly.var_enum.PN9
        phy.profile_inputs.white_seed.value = 0b111111111
        phy.profile_inputs.white_output_bit.value = 0

        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian  # 17.2.4 GFSK modulation
        phy.profile_inputs.shaping_filter_param.value = 0.5

        phy.profile_inputs.xtal_frequency_hz.value = 38400000
        phy.profile_inputs.rx_xtal_error_ppm.value = 24
        phy.profile_inputs.tx_xtal_error_ppm.value = 24

        phy.profile_inputs.crc_poly.value = model.vars.crc_poly.var_enum.BCH15_11
        phy.profile_inputs.crc_seed.value = 0xFF
        phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_pad_input.value = False
        phy.profile_inputs.crc_input_order.value = model.vars.crc_input_order.var_enum.MSB_FIRST
        phy.profile_inputs.crc_invert.value = False

        phy.profile_inputs.fec_en.value = model.vars.fec_en.var_enum.NONE
        phy.profile_inputs.frame_bitendian.value = model.vars.frame_bitendian.var_enum.MSB_FIRST

        # change to fixed length is mainly for test purpose (performance comparison), if use variable length, need to pass length parameter to packet builder like ZigBee
        phy.profile_inputs.frame_length_type.value = model.vars.frame_length_type.var_enum.VARIABLE_LENGTH
        phy.profile_inputs.payload_crc_en.value = True

        # Absent from Ocelot, was used on Nerio
        # phy.profile_inputs.payload_excludesubframewcnt_en.value = False

        # used fixed length, no header needed, same for header_CRC
        phy.profile_inputs.header_en.value = True
        phy.profile_inputs.header_size.value = 8
        phy.profile_inputs.header_calc_crc.value = True

        # Add required inputs to allow calculators to run
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED

        # forces from FPGA verification
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.AFC_LOCK_AT_PREAMBLE_DETECT

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-163
    def PHY_IEEE802154_SUN_FSK_896MHz_2FSK_40kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base,
                            readable_name='IEEE 802.15.4 SUN FSK 896MHz 2FSK 40kbps mi=0.5', phy_name=phy_name)

        # Start with the WiSUN base function for 2GFSK
        self.SUN_FSK_2GFSK_base(phy, model)

        # Standard-specific inputs
        phy.profile_inputs.base_frequency_hz.value = 896050000  # Freq mapping Table 10.10. Channel numbering for SUN PHYs
        phy.profile_inputs.channel_spacing_hz.value = 5 * 12500
        phy.profile_inputs.bitrate.value = 40000
        phy.profile_inputs.deviation.value = 10000  # 4800*0.5 / 2
        phy.profile_inputs.preamble_length.value = 4 * 16  # phyFskPreambleLength 4-64 repetitions of the preamble pattern (which is 16 bits)
        phy.profile_inputs.syncword_0.value = 0b0110111101001110  # Table 20.2.SUN FSK PHY SFD values for 2-FSK, page 494
        phy.profile_inputs.rx_xtal_error_ppm.value = 13
        phy.profile_inputs.tx_xtal_error_ppm.value = 13
        phy.profile_inputs.crc_poly.value = model.vars.crc_poly.var_enum.BCH15_11
        phy.profile_inputs.crc_seed.value = 0xFF
        phy.profile_inputs.baudrate_tol_ppm.value = 0

        return phy

    # Owner: Casey Weltzin
    # JIRA Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-164
    def PHY_IEEE802154_SUN_FSK_920MHz_4FSK_400kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base,
                            readable_name='IEEE 802.15.4 SUN FSK 920MHz 4FSK 400kbps mi=0.33', phy_name=phy_name)

        # IEEE802154 SUN FSK 868MHz 2GFSK 50kbps WISUN 1a EU

        # Start with the WiSUN base function for 4GFSK
        self.SUN_FSK_4GFSK_base(phy, model)

        # Standard-specific inputs
        phy.profile_inputs.base_frequency_hz.value = 920800000  # Freq mapping Table 10.10. Channel numbering for SUN PHYs
        phy.profile_inputs.channel_spacing_hz.value = 600000
        phy.profile_inputs.bitrate.value = 400000
        phy.profile_inputs.deviation.value = int(200000 / 6)
        phy.profile_inputs.preamble_length.value = 4 * 32  # phyFskPreambleLength 4-64 repetitions of the preamble pattern (which is 16 bits)
        phy.profile_inputs.rx_xtal_error_ppm.value = 40
        phy.profile_inputs.tx_xtal_error_ppm.value = 40
        phy.profile_inputs.crc_poly.value = model.vars.crc_poly.var_enum.BCH15_11
        phy.profile_inputs.crc_seed.value = 0xFF
        phy.profile_inputs.baudrate_tol_ppm.value = 0

        return phy