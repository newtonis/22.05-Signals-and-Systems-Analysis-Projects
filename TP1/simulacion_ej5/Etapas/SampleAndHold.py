from Etapas.Etapa import Etapa
from Globals import config
from Etapas import Senial


class SampleAndHold(Etapa):
    sampleAndHold = None

    def __init__(self):
        pass
        
    def processInput(self, inputSignal, loadingModel, fraction):

        timePeriod = 1 / config.GetConfigData().fs
        cyclesPeriod = int(timePeriod / inputSignal.separation)

        output = [0] * len(inputSignal.xvar)
        paso = fraction / len(inputSignal.xvar)
        aux = 0
        for i in range(len(inputSignal.xvar)):
            # tres casos

            fractionTime = i % cyclesPeriod

            if fractionTime < config.GetConfigData().SHsample * cyclesPeriod:
                output[i] = inputSignal.values[i]
            elif fractionTime < (config.GetConfigData().SHsample + config.GetConfigData().SHhold) * cyclesPeriod:
                if i != 0:
                    output[i] = output[i-1]
                else:
                    output[i] = 0
            aux += paso
            if i % 1000 == 0:
                if loadingModel:
                    loadingModel.update(aux)
                    aux = 0
        if loadingModel:
            loadingModel.update(aux)

        return Senial.Senial(inputSignal.xvar, output)


def getSampleAndHold():
    if not SampleAndHold.sampleAndHold:
        SampleAndHold.sampleAndHold = SampleAndHold()

    return SampleAndHold.sampleAndHold
