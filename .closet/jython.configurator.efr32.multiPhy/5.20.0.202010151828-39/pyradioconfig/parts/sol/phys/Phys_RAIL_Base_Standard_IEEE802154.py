from pyradioconfig.parts.ocelot.phys.Phys_RAIL_Base_Standard_IEEE802154 import PHYS_IEEE802154_Ocelot

class Phys_IEEE802154_Sol(PHYS_IEEE802154_Ocelot):

    def PHY_IEEE802154_780MHz_OQPSK(self, model):
        pass

    def PHY_IEEE802154_868MHz_BPSK(self, model):
        pass

    def PHY_IEEE802154_868MHz_BPSK_coh(self, model):
        pass

    def PHY_IEEE802154_868MHz_OQPSK(self, model):
        pass

    #def PHY_IEEE802154_868MHz_OQPSK_coh(self, model):
        #pass

    def PHY_IEEE802154_915MHz_OQPSK(self, model):
        pass

    #def PHY_IEEE802154_915MHz_OQPSK_coh(self, model):
        #pass

    def PHY_IEEE802154_RSGFSK_868MHz_500kbps_mi0p76(self, model):
        pass

    def PHY_IEEE802154_2p4GHz_cohdsa(self, model, phy_name=None):
        pass

    def PHY_IEEE802154_2p4GHz_cohdsa_diversity(self, model, phy_name=None):
        pass

    def PHY_IEEE802154_2p4GHz_diversity(self, model,phy_name=None):
        pass

    def PHY_IEEE802154_2p4GHz(self, model,phy_name=None):
        pass

    def PHY_IEEE802154_2p4GHz_prod(self, model,phy_name=None):
        pass

    def PHY_IEEE802154_SUN_OFDM_OPT1(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='IEEE 802.15.4 SUN OFDM OPTION 1', phy_name=phy_name)

        # updated for OFDM
        phy.profile_inputs.ofdm_option.value = 1
        phy.profile_inputs.bitrate.value = 2400000  # set to the highest rate for given option # up to 2400 with MCS6
        phy.profile_inputs.channel_spacing_hz.value = 1200000
        phy.profile_inputs.bandwidth_hz.value = 1376000
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.OFDM
        phy.profile_inputs.demod_select.value = model.vars.demod_select.var_enum.OFDM
        phy.profile_inputs.adc_rate_mode.value = model.vars.adc_rate_mode.var_enum.FULLRATE
        phy.profile_inputs.xtal_frequency_hz.value = 40000000
        phy.profile_inputs.base_frequency_hz.value = 868000000

        # place holders for now
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.deviation.value = 0
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_2500KHz
        phy.profile_inputs.preamble_length.value = 2
        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 0.5
        phy.profile_inputs.symbol_encoding.value = model.vars.symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_0.value = 0
        phy.profile_inputs.syncword_1.value = 0
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.target_osr.value = 4
        phy.profile_inputs.if_frequency_hz.value = 0

        phy.profile_outputs.FEFILT1_CF_DEC0.override = 5
        phy.profile_outputs.FEFILT1_CF_DEC1.override = 0
        phy.profile_outputs.FEFILT1_CF_DEC2.override = 0
        phy.profile_outputs.FEFILT1_SRCCHF_SRCRATIO2.override = 24576
        phy.profile_outputs.FEFILT1_CHFCOE00_SET0COEFF0.override = 21
        phy.profile_outputs.FEFILT1_CHFCOE00_SET0COEFF1.override = 80
        phy.profile_outputs.FEFILT1_CHFCOE00_SET0COEFF2.override = 173
        phy.profile_outputs.FEFILT1_CHFCOE01_SET0COEFF3.override = 256
        phy.profile_outputs.FEFILT1_CHFCOE01_SET0COEFF4.override = 230
        phy.profile_outputs.FEFILT1_CHFCOE02_SET0COEFF5.override = 7
        phy.profile_outputs.FEFILT1_CHFCOE02_SET0COEFF6.override = -420
        phy.profile_outputs.FEFILT1_CHFCOE03_SET0COEFF7.override = -890
        phy.profile_outputs.FEFILT1_CHFCOE03_SET0COEFF8.override = -1082
        phy.profile_outputs.FEFILT1_CHFCOE04_SET0COEFF9.override = -629
        phy.profile_outputs.FEFILT1_CHFCOE04_SET0COEFF10.override = 675
        phy.profile_outputs.FEFILT1_CHFCOE05_SET0COEFF11.override = 2704
        phy.profile_outputs.FEFILT1_CHFCOE05_SET0COEFF12.override = 4961
        phy.profile_outputs.FEFILT1_CHFCOE06_SET0COEFF13.override = 6736
        phy.profile_outputs.FEFILT1_CHFCOE06_SET0COEFF14.override = 7409

        return phy
    
    def PHY_IEEE802154_SUN_OFDM_OPT2(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='IEEE 802.15.4 SUN OFDM OPTION 2', phy_name=phy_name)

        # updated for OFDM
        phy.profile_inputs.ofdm_option.value = 2
        phy.profile_inputs.bitrate.value = 1200000
        phy.profile_inputs.channel_spacing_hz.value = 800000
        phy.profile_inputs.bandwidth_hz.value = 688000
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.OFDM
        phy.profile_inputs.demod_select.value = model.vars.demod_select.var_enum.OFDM
        phy.profile_inputs.adc_rate_mode.value = model.vars.adc_rate_mode.var_enum.FULLRATE
        phy.profile_inputs.xtal_frequency_hz.value = 40000000
        phy.profile_inputs.base_frequency_hz.value = 868000000

        # place holders for now
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.deviation.value = 0
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_2500KHz
        phy.profile_inputs.preamble_length.value = 2
        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 0.5
        phy.profile_inputs.symbol_encoding.value = model.vars.symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_0.value = 0
        phy.profile_inputs.syncword_1.value = 0
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.target_osr.value = 4
        phy.profile_inputs.if_frequency_hz.value = 0

        phy.profile_outputs.FEFILT1_CF_DEC0.override = 5
        phy.profile_outputs.FEFILT1_CF_DEC1.override = 1
        phy.profile_outputs.FEFILT1_CF_DEC2.override = 0
        phy.profile_outputs.FEFILT1_SRCCHF_SRCRATIO2.override = 24576
        phy.profile_outputs.FEFILT1_CHFCOE00_SET0COEFF0.override = 21
        phy.profile_outputs.FEFILT1_CHFCOE00_SET0COEFF1.override = 80
        phy.profile_outputs.FEFILT1_CHFCOE00_SET0COEFF2.override = 173
        phy.profile_outputs.FEFILT1_CHFCOE01_SET0COEFF3.override = 256
        phy.profile_outputs.FEFILT1_CHFCOE01_SET0COEFF4.override = 230
        phy.profile_outputs.FEFILT1_CHFCOE02_SET0COEFF5.override = 7
        phy.profile_outputs.FEFILT1_CHFCOE02_SET0COEFF6.override = -420
        phy.profile_outputs.FEFILT1_CHFCOE03_SET0COEFF7.override = -890
        phy.profile_outputs.FEFILT1_CHFCOE03_SET0COEFF8.override = -1082
        phy.profile_outputs.FEFILT1_CHFCOE04_SET0COEFF9.override = -629
        phy.profile_outputs.FEFILT1_CHFCOE04_SET0COEFF10.override = 675
        phy.profile_outputs.FEFILT1_CHFCOE05_SET0COEFF11.override = 2704
        phy.profile_outputs.FEFILT1_CHFCOE05_SET0COEFF12.override = 4961
        phy.profile_outputs.FEFILT1_CHFCOE06_SET0COEFF13.override = 6736
        phy.profile_outputs.FEFILT1_CHFCOE06_SET0COEFF14.override = 7409

        return phy

    def PHY_IEEE802154_SUN_OFDM_OPT3(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='IEEE 802.15.4 SUN OFDM OPTION 3', phy_name=phy_name)

        # updated for OFDM
        phy.profile_inputs.ofdm_option.value = 3
        phy.profile_inputs.bitrate.value = 600000
        phy.profile_inputs.channel_spacing_hz.value = 400000
        phy.profile_inputs.bandwidth_hz.value = 400000
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.OFDM
        phy.profile_inputs.demod_select.value = model.vars.demod_select.var_enum.OFDM
        phy.profile_inputs.adc_rate_mode.value = model.vars.adc_rate_mode.var_enum.FULLRATE
        phy.profile_inputs.xtal_frequency_hz.value = 40000000
        phy.profile_inputs.base_frequency_hz.value = 868000000

        # place holders for now
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.deviation.value = 0
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_2500KHz
        phy.profile_inputs.preamble_length.value = 2
        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 0.5
        phy.profile_inputs.symbol_encoding.value = model.vars.symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_0.value = 0
        phy.profile_inputs.syncword_1.value = 0
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.target_osr.value = 4
        phy.profile_inputs.if_frequency_hz.value = 0

        phy.profile_outputs.FEFILT1_CF_DEC0.override = 2
        phy.profile_outputs.FEFILT1_CF_DEC1.override = 4
        phy.profile_outputs.FEFILT1_CF_DEC2.override = 0
        phy.profile_outputs.FEFILT1_SRCCHF_SRCRATIO2.override = 24576
        phy.profile_outputs.FEFILT1_CHFCOE00_SET0COEFF0.override = -11
        phy.profile_outputs.FEFILT1_CHFCOE00_SET0COEFF1.override = -36
        phy.profile_outputs.FEFILT1_CHFCOE00_SET0COEFF2.override = -48
        phy.profile_outputs.FEFILT1_CHFCOE01_SET0COEFF3.override = 11
        phy.profile_outputs.FEFILT1_CHFCOE01_SET0COEFF4.override = 175
        phy.profile_outputs.FEFILT1_CHFCOE02_SET0COEFF5.override = 349
        phy.profile_outputs.FEFILT1_CHFCOE02_SET0COEFF6.override = 302
        phy.profile_outputs.FEFILT1_CHFCOE03_SET0COEFF7.override = -165
        phy.profile_outputs.FEFILT1_CHFCOE03_SET0COEFF8.override = -925
        phy.profile_outputs.FEFILT1_CHFCOE04_SET0COEFF9.override = -1375
        phy.profile_outputs.FEFILT1_CHFCOE04_SET0COEFF10.override = -690
        phy.profile_outputs.FEFILT1_CHFCOE05_SET0COEFF11.override = 1558
        phy.profile_outputs.FEFILT1_CHFCOE05_SET0COEFF12.override = 4869
        phy.profile_outputs.FEFILT1_CHFCOE06_SET0COEFF13.override = 7872
        phy.profile_outputs.FEFILT1_CHFCOE06_SET0COEFF14.override = 9085

        return phy

    def PHY_IEEE802154_SUN_OFDM_OPT4(self, model, phy_name=None):
        phy = self._makePhy(model, model.profiles.Base, readable_name='IEEE 802.15.4 SUN OFDM OPTION 4', phy_name=phy_name)

        # updated for OFDM
        phy.profile_inputs.ofdm_option.value = 4
        phy.profile_inputs.bitrate.value = 300000
        phy.profile_inputs.channel_spacing_hz.value = 200000
        phy.profile_inputs.bandwidth_hz.value = 200000
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.OFDM
        phy.profile_inputs.demod_select.value = model.vars.demod_select.var_enum.OFDM
        phy.profile_inputs.adc_rate_mode.value = model.vars.adc_rate_mode.var_enum.FULLRATE
        phy.profile_inputs.xtal_frequency_hz.value = 40000000
        phy.profile_inputs.base_frequency_hz.value = 868000000

        # place holders for now
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.deviation.value = 0
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsss_chipping_code.value = 0
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.pll_bandwidth_tx.value = model.vars.pll_bandwidth_tx.var_enum.BW_2500KHz
        phy.profile_inputs.preamble_length.value = 2
        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Gaussian
        phy.profile_inputs.shaping_filter_param.value = 0.5
        phy.profile_inputs.symbol_encoding.value = model.vars.symbol_encoding.var_enum.NRZ
        phy.profile_inputs.syncword_0.value = 0
        phy.profile_inputs.syncword_1.value = 0
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.target_osr.value = 4
        phy.profile_inputs.if_frequency_hz.value = 0

        phy.profile_outputs.FEFILT1_CF_DEC0.override = 0
        phy.profile_outputs.FEFILT1_CF_DEC1.override = 12
        phy.profile_outputs.FEFILT1_CF_DEC2.override = 0
        phy.profile_outputs.FEFILT1_SRCCHF_SRCRATIO2.override = 25206
        phy.profile_outputs.FEFILT1_CHFCOE00_SET0COEFF0.override = -11
        phy.profile_outputs.FEFILT1_CHFCOE00_SET0COEFF1.override = -36
        phy.profile_outputs.FEFILT1_CHFCOE00_SET0COEFF2.override = -48
        phy.profile_outputs.FEFILT1_CHFCOE01_SET0COEFF3.override = 11
        phy.profile_outputs.FEFILT1_CHFCOE01_SET0COEFF4.override = 175
        phy.profile_outputs.FEFILT1_CHFCOE02_SET0COEFF5.override = 349
        phy.profile_outputs.FEFILT1_CHFCOE02_SET0COEFF6.override = 302
        phy.profile_outputs.FEFILT1_CHFCOE03_SET0COEFF7.override = -165
        phy.profile_outputs.FEFILT1_CHFCOE03_SET0COEFF8.override = -925
        phy.profile_outputs.FEFILT1_CHFCOE04_SET0COEFF9.override = -1375
        phy.profile_outputs.FEFILT1_CHFCOE04_SET0COEFF10.override = -690
        phy.profile_outputs.FEFILT1_CHFCOE05_SET0COEFF11.override = 1558
        phy.profile_outputs.FEFILT1_CHFCOE05_SET0COEFF12.override = 4869
        phy.profile_outputs.FEFILT1_CHFCOE06_SET0COEFF13.override = 7872
        phy.profile_outputs.FEFILT1_CHFCOE06_SET0COEFF14.override = 9085

        return phy