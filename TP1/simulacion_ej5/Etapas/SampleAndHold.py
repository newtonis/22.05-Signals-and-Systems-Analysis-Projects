from Etapas.Etapa import Etapa
from Globals import config
from Etapas import Senial


class SampleAndHold(Etapa):
    sampleAndHold = None

    def __init__(self):
        pass
        
    def processInput(self, inputSignal):

        timePeriod = 1 / config.SHfreq
        cyclesPeriod = int(timePeriod / inputSignal.separation)

        output = [0] * len(inputSignal.xvar)

        for i in range(len(inputSignal.xvar)):
            # tres casos

            fractionTime = i % cyclesPeriod

            if fractionTime < config.SHsample * cyclesPeriod:
                output[i] = inputSignal.values[i]
            elif fractionTime < (config.SHsample + config.SHhold) * cyclesPeriod:
                if i != 0:
                    output[i] = output[i-1]
                else:
                    output[i] = 0

        return Senial.Senial(inputSignal.xvar, output)


def getSampleAndHold():
    if not SampleAndHold.sampleAndHold:
        SampleAndHold.sampleAndHold = SampleAndHold()

    return SampleAndHold.sampleAndHold
