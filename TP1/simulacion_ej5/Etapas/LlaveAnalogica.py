from Etapas.Etapa import Etapa
from Etapas import Senial
from Globals import config


class LlaveAnalogica(Etapa):
    llaveAnalogica = None

    def __init__(self):
        pass

    def processInput(self, inputSignal):
        output = []

        separation = 1 / config.LLfreq

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

