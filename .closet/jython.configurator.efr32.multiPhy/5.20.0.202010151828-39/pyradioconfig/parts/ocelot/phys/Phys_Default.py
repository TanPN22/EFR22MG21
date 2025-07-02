from pyradioconfig.parts.common.phys.default_phys import DefaultPhys, ModelDefaultPhy

class DefaultPhys_ocelot(DefaultPhys):

    def build(self, model):
        """
        Assigns default PHYs.  There must be one default phy defined here for every profile defined
        """
        model.profiles.Base.default_phys.append(ModelDefaultPhy(model.phys.PHY_Datasheet_868M_2GFSK_500Kbps_125K))
        model.profiles.Connect.default_phys.append(ModelDefaultPhy(model.phys.PHY_Connect_902MHz_2GFSK_200kbps))
        model.profiles.Mbus.default_phys.append(ModelDefaultPhy(model.phys.PHY_wMbus_ModeS_32p768k_frameA))