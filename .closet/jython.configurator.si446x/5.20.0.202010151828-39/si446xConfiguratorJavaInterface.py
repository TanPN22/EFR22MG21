# This is a python adapter that adapts to the IModemCalculator java interface
from ChipConfiguratorJavaInterface import ChipConfiguratorJavaInterface
from siradiocfg import ConfiguratorFacade

__all__ = ["si446xConfiguratorJavaInterface"]
class si446xConfiguratorJavaInterface(ChipConfiguratorJavaInterface):

    def __init__ (self):
        self.configurator = ConfiguratorFacade()
