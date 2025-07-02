from pyradioconfig.parts.common.calculators.calc_fec import CALC_FEC
from pycalcmodel.core.variable import ModelVariableFormat, CreateModelVariableEnum
from enum import Enum

class CALC_FEC_Ocelot(CALC_FEC):

    def __init__(self):
        #Call init of parent class
        super().__init__()

    def _build_fec_var(self, model):
        # This function adds the fec_en enumerated variable. It is a separate method to allow overwriting in future parts.

        var = self._addModelVariable(model, 'fec_en', Enum, ModelVariableFormat.DECIMAL,
                                     'List of supported FEC Configurations')
        member_data = [
            ['NONE', 0, 'No FEC'],
            ['FEC_154G_NRNSC_INTERLEAVING',  1, '15.4G FEC settings with NRNSC and interleaving'],
            ['FEC_154G_RSC_INTERLEAVING', 2, '15.4G FEC settings with RSC and interleaving'],
            ['FEC_154G_RSC_NO_INTERLEAVING', 3, '15.4G FEC settings with RSC and no interleaving'],
        ]
        var.var_enum = CreateModelVariableEnum(
            'FECEnum',
            'List of supported FEC Configurations',
            member_data)

    def calc_fec(self, model):
        """calc_fec

        Args:
            model (ModelRoot) : Data model to read and write variables from
        """

        model.vars.fec_en.value = model.vars.fec_en.var_enum.NONE  # Calculate a default value for Profiles where this is an advanced input

        # Always initialize FEC regs to these values
        self._calc_init(model)

        # IF FEC is enabled then write the 802.15.4g base values
        if model.vars.fec_en.value != model.vars.fec_en.var_enum.NONE:
            self._FEC_154G_Base(model)

        model.vars.fec_enabled.value = int(model.vars.FRC_FECCTRL_CONVMODE.value != 0)

    def calc_feccrl_interleavemode_reg(self, model):
        # This function calculates the FRC_FECCTRL_INTERLEAVEMODE reg field

        # Read in model variables
        fec_en = model.vars.fec_en.value

        if (fec_en == model.vars.fec_en.var_enum.FEC_154G_NRNSC_INTERLEAVING) or \
                (fec_en == model.vars.fec_en.var_enum.FEC_154G_RSC_INTERLEAVING):
            interleavemode = 1
        else:
            interleavemode = 0

        # Load value into register
        self._reg_write(model.vars.FRC_FECCTRL_INTERLEAVEMODE, interleavemode)