from Etapas.Etapa import Etapa
from Etapas import Senial
from Globals import config


class LlaveAnalogica(Etapa):
    llaveAnalogica = None

    def __init__(self):
        self.syncSignal = None

    def setSyncSignal(self, syncSignal):
        self.syncSignal = syncSignal

    def processInput(self, inputSignal):
        if not self.syncSignal:
            raise Exception("No sync signal configured")

        if inputSignal.length() != self.syncSignal.length():
            raise Exception("Signals are of different length")

        output = []

        separation = 1 / config.SHfreq

        output.append(inputSignal.values[0])
        last = 0

        status = True

        for ti in range(1, len(inputSignal.xvar)):
            if abs(inputSignal.xvar[ti] - inputSignal.xvar[last]) > separation:
                status = not status
                last = ti

            if status:
                output.append(inputSignal.values[ti])
            else:
                output.append(0)

        return Senial.Senial(inputSignal.xvar, output)


def getLlaveAnalogica():
    if not LlaveAnalogica.llaveAnalogica:
        LlaveAnalogica.llaveAnalogica = LlaveAnalogica()

    return LlaveAnalogica.llaveAnalogica

