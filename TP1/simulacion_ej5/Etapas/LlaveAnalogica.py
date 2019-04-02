from Etapas.Etapa import Etapa
from Etapas import Senial
from Globals import config


class LlaveAnalogica(Etapa):
    llaveAnalogica = None

    def __init__(self):
        pass

    def processInput(self, inputSignal, loadingModel, fraction):
        output = [0] * len(inputSignal.xvar)

        timePeriod = 1 / config.GetConfigData().fs
        cyclesPeriod = int(timePeriod / inputSignal.separation)

        toffCycles = int(config.GetConfigData().LLoff * cyclesPeriod)

        paso = fraction / len(inputSignal.xvar)
        aux = 0
        for ti in range(len(inputSignal.xvar)):
            if ti % cyclesPeriod >= toffCycles:
                output[ti] = inputSignal.values[ti]
            else:
                output[ti] = 0

            aux += paso
            if ti % 1000 == 0:
                if loadingModel:
                    loadingModel.update(aux)
                aux = 0
        if loadingModel:
            loadingModel.update(aux)

        return Senial.Senial(inputSignal.xvar, output)


def getLlaveAnalogica():
    if not LlaveAnalogica.llaveAnalogica:
        LlaveAnalogica.llaveAnalogica = LlaveAnalogica()

    return LlaveAnalogica.llaveAnalogica

