from Etapas.Etapa import Etapa
from Etapas import Senial
from Globals import config


class LlaveAnalogica(Etapa):
    llaveAnalogica = None

    def __init__(self):
        pass

    def processInput(self, inputSignal):
        output = [0] * len(inputSignal.xvar)

        timePeriod = 1 / config.SHfreq
        cyclesPeriod = int(timePeriod / inputSignal.separation)

        toffCycles = int(config.LLoff * cyclesPeriod)

        for ti in range(len(inputSignal.xvar)):
            if ti % cyclesPeriod >= toffCycles:
                output[ti] = inputSignal.values[ti]
            else:
                output[ti] = 0

        return Senial.Senial(inputSignal.xvar, output)


def getLlaveAnalogica():
    if not LlaveAnalogica.llaveAnalogica:
        LlaveAnalogica.llaveAnalogica = LlaveAnalogica()

    return LlaveAnalogica.llaveAnalogica

