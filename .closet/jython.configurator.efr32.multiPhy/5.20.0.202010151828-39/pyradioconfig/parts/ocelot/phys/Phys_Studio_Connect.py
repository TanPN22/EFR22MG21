from pyradioconfig.parts.nixi.phys.Phys_connect import PHYS_connect_Nixi
from pyradioconfig.calculator_model_framework.Utils.LogMgr import LogMgr
from py_2_and_3_compatibility import *

class PHYS_connect_Ocelot(PHYS_connect_Nixi):
    # inherit from Nixi (Jumbo)

    def Connect_base(self, phy, model):

        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.dsss_chipping_code.value = long(0)
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.FSK2
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 0.5
        phy.profile_inputs.symbol_encoding.value = model.vars.symbol_encoding.var_enum.NRZ
        phy.profile_inputs.xtal_frequency_hz.value = 39000000
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.MSB_FIRST
        phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.MSB_FIRST
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 32
        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.syncword_0.value = long(11732)
        phy.profile_inputs.syncword_1.value = long(0)
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.white_poly.value = model.vars.white_poly.var_enum.PN9

    # Omit any 2.4GHz PHYs
    def PHY_Connect_2_4GHz_OQPSK_2Mcps_250kbps(self, model, phy_name=None):
        pass

    def PHY_Connect_915MHz_2GFSK_500kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Connect, 'US FCC 915, Brazil 915', readable_name="Connect 915MHz 2GFSK 500kbps")

        # : Common base funtion for all connect PHYs
        self.Connect_base(phy, model)
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.tx_xtal_error_ppm.value = 20
        phy.profile_inputs.deviation.value = 175000
        phy.profile_inputs.base_frequency_hz.value = 915000000
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.preamble_length.value = 40
        phy.profile_inputs.syncword_tx_skip.value = False
        phy.profile_inputs.asynchronous_rx_enable.value = False
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_LOCK_AT_PREAMBLE_DETECT
        phy.profile_inputs.channel_spacing_hz.value = 400000
        phy.profile_inputs.test_ber.value = False
        phy.profile_inputs.fec_en.value = model.vars.fec_en.var_enum.NONE
        phy.profile_inputs.manchester_mapping.value = model.vars.manchester_mapping.var_enum.Default

        return phy


    def PHY_Connect_915MHz_2GFSK_500kbps_bcr_antdiv(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Connect, 'US FCC 915, Brazil 915', readable_name="PHY_Connect_915MHz 2GFSK 500kbps BCR antdiv")

        # : Common base funtion for all connect PHYs
        self.Connect_base(phy, model)
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.tx_xtal_error_ppm.value = 20
        phy.profile_inputs.deviation.value = 250000#175000
        phy.profile_inputs.base_frequency_hz.value = 915000000
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.preamble_length.value = 64
        phy.profile_inputs.syncword_tx_skip.value = False
        phy.profile_inputs.asynchronous_rx_enable.value = False
        phy.profile_inputs.channel_spacing_hz.value = 400000
        phy.profile_inputs.test_ber.value = False
        phy.profile_inputs.fec_en.value = model.vars.fec_en.var_enum.NONE
        phy.profile_inputs.manchester_mapping.value = model.vars.manchester_mapping.var_enum.Default

        phy.profile_inputs.antdivmode.value = model.vars.antdivmode.var_enum.PHDEMODANTDIV


        return phy

    def PHY_Connect_902MHz_2GFSK_200kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Connect, phy_description='US FCC 902, Brazil 902',
                            readable_name="Connect 902MHz 2GFSK 200kbps", phy_name=phy_name)

        # : Common base funtion for all connect PHYs
        self.Connect_base(phy, model)
        phy.profile_inputs.agc_period.value = 0
        phy.profile_inputs.base_frequency_hz.value = long(902000000)
        phy.profile_inputs.bitrate.value = 200000
        phy.profile_inputs.deviation.value = 50000
        phy.profile_inputs.channel_spacing_hz.value = 400000
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.symbols_in_timing_window.value = 14
        phy.profile_inputs.tx_xtal_error_ppm.value = 20
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_LOCK_AT_PREAMBLE_DETECT

        return phy

    def PHY_Connect_434MHz_2GFSK_200kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Connect, phy_description='US FCC 434',
                            readable_name="Connect 434MHz 2GFSK 200kbps", phy_name=phy_name)

        # : Common base funtion for all connect PHYs
        self.Connect_base(phy, model)
        phy.profile_inputs.agc_period.value = 0
        phy.profile_inputs.bandwidth_hz.value = 400000
        phy.profile_inputs.base_frequency_hz.value = long(434000000)
        phy.profile_inputs.bitrate.value = 200000
        phy.profile_inputs.deviation.value = 100000
        phy.profile_inputs.channel_spacing_hz.value = 500000
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.symbols_in_timing_window.value = 14
        phy.profile_inputs.tx_xtal_error_ppm.value = 20
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_LOCK_AT_PREAMBLE_DETECT

        return phy

    def PHY_Connect_863MHz_2GFSK_100kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Connect, phy_description='Europe 868',
                            readable_name="Connect 863MHz 2GFSK 100kbps", phy_name=phy_name)

        # : Common base funtion for all connect PHYs
        self.Connect_base(phy, model)
        phy.profile_inputs.agc_period.value = 0
        phy.profile_inputs.bandwidth_hz.value = 200000
        phy.profile_inputs.base_frequency_hz.value = long(863000000)
        phy.profile_inputs.bitrate.value = 100000
        phy.profile_inputs.deviation.value = 50000
        phy.profile_inputs.channel_spacing_hz.value = 400000
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.symbols_in_timing_window.value = 14
        phy.profile_inputs.tx_xtal_error_ppm.value = 20
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_LOCK_AT_PREAMBLE_DETECT

        return phy

    def PHY_Connect_169MHz_2GFSK_4p8kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Connect, phy_description='Europe 169',
                            readable_name="Connect 169MHz 2GFSK 4.8kbps", phy_name=phy_name)

        # : Common base funtion for all connect PHYs
        self.Connect_base(phy, model)
        phy.profile_inputs.agc_period.value = 0
        phy.profile_inputs.base_frequency_hz.value = long(169000000)
        phy.profile_inputs.bitrate.value = 4800
        phy.profile_inputs.deviation.value = 1200
        phy.profile_inputs.channel_spacing_hz.value = 12500
        phy.profile_inputs.number_of_timing_windows.value = 2
        phy.profile_inputs.rx_xtal_error_ppm.value = 7
        phy.profile_inputs.symbols_in_timing_window.value = 6
        phy.profile_inputs.timing_detection_threshold.value = 10
        phy.profile_inputs.tx_xtal_error_ppm.value = 7
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_LOCK_AT_PREAMBLE_DETECT

        return phy

    def PHY_Connect_490MHz_2GFSK_10kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Connect, 'China 490', readable_name="Connect 490MHz 2GFSK 10kbps")

        # : Common base funtion for all connect PHYs
        self.Connect_base(phy, model)
        phy.profile_inputs.agc_period.value = 0
        phy.profile_inputs.base_frequency_hz.value = long(490000000)
        phy.profile_inputs.bitrate.value = 10000
        phy.profile_inputs.deviation.value = 25000
        phy.profile_inputs.channel_spacing_hz.value = 200000
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.symbols_in_timing_window.value = 28
        phy.profile_inputs.tx_xtal_error_ppm.value = 20
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        #phy.profile_inputs.target_osr.value = 32

        return phy

    def PHY_Connect_920MHz_2GFSK_100kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Connect, phy_description='Japan 915',
                            readable_name="Connect 920MHz 2GFSK 100kbps", phy_name=phy_name)

        # : Common base funtion for all connect PHYs
        self.Connect_base(phy, model)
        phy.profile_inputs.agc_period.value = 0
        phy.profile_inputs.bandwidth_hz.value = 198000
        phy.profile_inputs.base_frequency_hz.value = long(920000000)
        phy.profile_inputs.bitrate.value = 100000
        phy.profile_inputs.deviation.value = 50000
        phy.profile_inputs.channel_spacing_hz.value = 400000
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.symbols_in_timing_window.value = 14
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_LOCK_AT_PREAMBLE_DETECT

        return phy

    def PHY_Connect_424MHz_2GFSK_4p8kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Connect, phy_description='Korea 424',
                            readable_name="Connect 424MHz 2GFSK 4.8kbps", phy_name=phy_name)

        # : Common base funtion for all connect PHYs
        self.Connect_base(phy, model)
        phy.profile_inputs.agc_period.value = 0
        phy.profile_inputs.bandwidth_hz.value = 12000
        phy.profile_inputs.base_frequency_hz.value = long(424700000)
        phy.profile_inputs.bitrate.value = 4800
        phy.profile_inputs.deviation.value = 2400
        phy.profile_inputs.channel_spacing_hz.value = 12500
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.symbols_in_timing_window.value = 14
        phy.profile_inputs.tx_xtal_error_ppm.value = 20
        phy.profile_inputs.freq_offset_hz.value = 1450
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_LOCK_AT_PREAMBLE_DETECT
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian

        return phy

    def PHY_Connect_447MHz_2GFSK_4p8kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Connect, phy_description='Korea 447',
                            readable_name="Connect 447MHz 2GFSK 4.8kbps", phy_name=phy_name)

        # : Common base funtion for all connect PHYs
        self.Connect_base(phy, model)
        phy.profile_inputs.agc_period.value = 0
        phy.profile_inputs.bandwidth_hz.value = 12000
        phy.profile_inputs.base_frequency_hz.value = long(447000000)
        phy.profile_inputs.bitrate.value = 4800
        phy.profile_inputs.deviation.value = 2400
        phy.profile_inputs.channel_spacing_hz.value = 12500
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.symbols_in_timing_window.value = 14
        phy.profile_inputs.tx_xtal_error_ppm.value = 20
        phy.profile_inputs.freq_offset_hz.value = 1450
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_LOCK_AT_PREAMBLE_DETECT
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian

        return phy

    def PHY_Connect_917MHz_2GFSK_4p8kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Connect, phy_description='Korea 915',
                            readable_name="Connect 917MHz 2GFSK 4.8kbps", phy_name=phy_name)

        # : Common base funtion for all connect PHYs
        self.Connect_base(phy, model)
        phy.profile_inputs.agc_period.value = 0
        phy.profile_inputs.base_frequency_hz.value = long(917100000)
        phy.profile_inputs.bitrate.value = 4800
        phy.profile_inputs.deviation.value = 2400
        phy.profile_inputs.channel_spacing_hz.value = 200000
        phy.profile_inputs.number_of_timing_windows.value = 10
        phy.profile_inputs.rx_xtal_error_ppm.value = 2
        phy.profile_inputs.symbols_in_timing_window.value = 1
        phy.profile_inputs.tx_xtal_error_ppm.value = 3
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.NONE
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_LOCK_AT_PREAMBLE_DETECT

        return phy

    # Owner: Young-Joon Choi
    # Jira Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-141
    def PHY_Studio_Connect_915MHz_OQPSK_500kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Connect, phy_description='DSSS 500',
                            readable_name="Connect 915MHz OQPSK 500Kbps", phy_name=phy_name)

        # : Common base funtion for all connect PHYs
        self.Connect_base(phy, model)

        """ Channel and Bandwidth Settings """
        phy.profile_inputs.base_frequency_hz.value = long(915000000)
        phy.profile_inputs.deviation.value = 250000
        phy.profile_inputs.channel_spacing_hz.value = 400000
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.baudrate_tol_ppm.value = 0

        """ Modulation Type """
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.OQPSK

        """ Symbol Mapping and Encoding """
        phy.profile_inputs.symbol_encoding.value = model.vars.symbol_encoding.var_enum.DSSS

        """ DSSS Parameters """
        phy.profile_inputs.dsss_chipping_code.value = 31433
        phy.profile_inputs.dsss_len.value = 16
        phy.profile_inputs.dsss_spreading_factor.value = 4

        """ Shaping Filter Parameters """
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Custom_OQPSK
        phy.profile_inputs.shaping_filter_param.value = 0.5

        """ Preamble Parameters """
        phy.profile_inputs.preamble_pattern_len.value = 4
        phy.profile_inputs.preamble_length.value = 40
        phy.profile_inputs.preamble_pattern.value = 0

        """ Syncword Parameters """
        phy.profile_inputs.syncword_0.value = long(167)
        phy.profile_inputs.syncword_1.value = long(0)
        phy.profile_inputs.syncword_length.value = 8
        phy.profile_inputs.syncword_tx_skip.value = False

        """ XO Parameters """
        phy.profile_inputs.rx_xtal_error_ppm.value = 10
        phy.profile_inputs.tx_xtal_error_ppm.value = 10

        """ Frame Configurations """
        # Packet Inputs
        phy.profile_inputs.asynchronous_rx_enable.value = False
        return phy

    # Owner: Young-Joon Choi
    # Jira Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-143
    def PHY_Studio_Connect_915mhz_oqpsk_800kcps_100kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Connect, phy_description='DSSS 100',
                            readable_name="Connect 915MHz OQPSK 800kcps 100kbps", phy_name=phy_name)

        # : Common base funtion for all connect PHYs
        self.Connect_base(phy, model)

        """ Channel and Bandwidth Settings """
        phy.profile_inputs.base_frequency_hz.value = 915000000
        phy.profile_inputs.deviation.value = 200000
        phy.profile_inputs.channel_spacing_hz.value = 2000000
        phy.profile_inputs.bitrate.value = 100000
        phy.profile_inputs.baudrate_tol_ppm.value = 4000

        """ Modulation Type """
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.OQPSK

        """ Symbol Mapping and Encoding """
        phy.profile_inputs.symbol_encoding.value = model.vars.symbol_encoding.var_enum.DSSS

        """ DSSS Parameters """
        phy.profile_inputs.dsss_chipping_code.value = long(1951056795)
        phy.profile_inputs.dsss_len.value = 32
        phy.profile_inputs.dsss_spreading_factor.value = 8

        """ Shaping Filter Parameters """
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Custom_OQPSK
        phy.profile_inputs.shaping_filter_param.value = 0.5

        """ Preamble Parameters """
        phy.profile_inputs.preamble_pattern_len.value = 4
        phy.profile_inputs.preamble_length.value = 32
        phy.profile_inputs.preamble_pattern.value = 0

        """ Syncword Parameters """
        phy.profile_inputs.syncword_0.value = long(167)
        phy.profile_inputs.syncword_1.value = long(0)
        phy.profile_inputs.syncword_length.value = 8
        phy.profile_inputs.syncword_tx_skip.value = False

        """ XO Parameters """
        phy.profile_inputs.rx_xtal_error_ppm.value = 10
        phy.profile_inputs.tx_xtal_error_ppm.value = 10

        """ Frame Configurations """
        # Packet Inputs
        phy.profile_inputs.asynchronous_rx_enable.value = False
        phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.LSB_FIRST
        phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.LSB_FIRST
        return phy

    # Owner: Young-Joon Choi
    # Jira Link: https://jira.silabs.com/browse/PGOCELOTVALTEST-996
    def PHY_Studio_Connect_915mhz_oqpsk_2Mcps_250kbps(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Connect, phy_description='DSSS 250', readable_name="Connect 915MHz OQPSK 2Mcps 250kbps", phy_name=phy_name)

        # : Common base funtion for all connect PHYs
        self.Connect_base(phy, model)

        """ Channel and Bandwidth Settings """
        phy.profile_inputs.base_frequency_hz.value = long(915000000)
        phy.profile_inputs.deviation.value = 500000
        phy.profile_inputs.channel_spacing_hz.value = 2000000
        phy.profile_inputs.bitrate.value = 250000
        phy.profile_inputs.baudrate_tol_ppm.value = 4000

        """ Modulation Type """
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.OQPSK

        """ Symbol Mapping and Encoding """
        phy.profile_inputs.symbol_encoding.value = model.vars.symbol_encoding.var_enum.DSSS

        """ DSSS Parameters """
        phy.profile_inputs.dsss_chipping_code.value = 1951056795
        phy.profile_inputs.dsss_len.value = 32
        phy.profile_inputs.dsss_spreading_factor.value = 8

        """ Shaping Filter Parameters """
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Custom_OQPSK
        phy.profile_inputs.shaping_filter_param.value = 0.5

        """ Preamble Parameters """
        phy.profile_inputs.preamble_pattern_len.value = 4
        phy.profile_inputs.preamble_length.value = 32
        phy.profile_inputs.preamble_pattern.value = 0

        """ Syncword Parameters """
        phy.profile_inputs.syncword_0.value = long(167)
        phy.profile_inputs.syncword_1.value = long(0)
        phy.profile_inputs.syncword_length.value = 8
        phy.profile_inputs.syncword_tx_skip.value = False

        """ XO Parameters """
        phy.profile_inputs.rx_xtal_error_ppm.value = 10
        phy.profile_inputs.tx_xtal_error_ppm.value = 10

        """ Frame Configurations """
        # Packet Inputs
        phy.profile_inputs.crc_byte_endian.value = model.vars.crc_byte_endian.var_enum.LSB_FIRST
        phy.profile_inputs.crc_bit_endian.value = model.vars.crc_bit_endian.var_enum.LSB_FIRST
        phy.profile_inputs.white_poly.value = model.vars.white_poly.var_enum.NONE
        phy.profile_inputs.asynchronous_rx_enable.value = False
        return phy

    # : Renamed to PHY_Studio_Connect_915MHz_OQPSK_500kbps
    def PHY_Connect_915MHz_OQPSK_500kbps(self, model, phy_name=None):
        pass
    
    # : Renamed to PHY_Studio_Connect_915mhz_oqpsk_2Mcps_250kbps
    def PHY_Connect_915mhz_oqpsk_2Mcps_250kbps(self, model, phy_name=None):
        pass

    # : Renamed to PHY_Studio_Connect_915mhz_oqpsk_800kcps_100kbps
    def PHY_Connect_915mhz_oqpsk_800kcps_100kbps(self, model, phy_name=None):
        pass

    def PHY_Connect_915MHz_2GFSK_500kbps_tre_antdiv(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Connect, 'US FCC 915, Brazil 915', readable_name="PHY_Connect_915MHz 2GFSK 500kbps TRECS antdiv")

        # : Common base funtion for all connect PHYs
        self.Connect_base(phy, model)
        phy.profile_inputs.rx_xtal_error_ppm.value = 20
        phy.profile_inputs.tx_xtal_error_ppm.value = 20
        phy.profile_inputs.deviation.value = 250000#175000
        phy.profile_inputs.base_frequency_hz.value = 915000000
        phy.profile_inputs.bitrate.value = 500000
        phy.profile_inputs.preamble_length.value = 64
        phy.profile_inputs.syncword_tx_skip.value = False
        phy.profile_inputs.asynchronous_rx_enable.value = False
        phy.profile_inputs.channel_spacing_hz.value = 400000
        phy.profile_inputs.test_ber.value = False
        phy.profile_inputs.fec_en.value = model.vars.fec_en.var_enum.NONE
        phy.profile_inputs.manchester_mapping.value = model.vars.manchester_mapping.var_enum.Default

        phy.profile_inputs.antdivmode.value = model.vars.antdivmode.var_enum.PHDEMODANTDIV


        return phy
