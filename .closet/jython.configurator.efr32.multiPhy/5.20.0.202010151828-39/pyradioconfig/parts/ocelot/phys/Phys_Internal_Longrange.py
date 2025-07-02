from pyradioconfig.calculator_model_framework.interfaces.iphy import IPhy
from pyradioconfig.parts.ocelot.phys.Phys_Studio_LongRange import PHYS_OQPSK_LoRa_Ocelot


class PHYS_Internal_Connect_Ocelot(IPhy):

    # Owner: Young-Joon Choi
    # Internal Testing PHY for Calculator Development
    def PHY_Internal_Longrange_915M_OQPSK_DSSS8_2p4kbps(self, model):
        phy = PHYS_OQPSK_LoRa_Ocelot().PHY_Longrange_490M_OQPSK_DSSS8_2p4kbps(model,
                                                                                   phy_name="PHY_Internal_Longrange_915M_OQPSK_DSSS8_2p4kbps")
        phy.profile_inputs.base_frequency_hz.value = 915000000
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
