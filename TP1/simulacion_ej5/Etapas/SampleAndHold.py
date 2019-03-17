from Etapas.Etapa import Etapa
from Globals import config
from Etapas import Senial


class SampleAndHold(Etapa):
    sampleAndHold = None

    def __init__(self):
        pass

    def processInput(self, inputSignal):

        output = []

        separation = 1 / config.SHfreq

        output.append(inputSignal.values[0])
        last = 0

        for ti in range(1, len(inputSignal.xvar)):
            if abs(inputSignal.xvar[ti] - inputSignal.xvar[last]) > separation:
                last = ti

            output.append(inputSignal.values[last])

        return Senial.Senial(inputSignal.xvar, output)


def getSampleAndHold():
    if not SampleAndHold.sampleAndHold:
        SampleAndHold.sampleAndHold = SampleAndHold()

    return SampleAndHold.sampleAndHold
