from Etapas.Etapa import Etapa
from scipy import signal
from Globals import tf
from Etapas.Senial import Senial


class FiltroLP(Etapa):
    filtroLP = None

    def __init__(self):
        pass

    def processInput(self, inputSignal):
        t, y, x = signal.lsim(tf.getTf(), inputSignal.values, inputSignal.xvar)

        return Senial(t, y)


def getFiltroLP():
    if not FiltroLP.filtroLP:
        FiltroLP.filtroLP = FiltroLP()

    return FiltroLP.filtroLP
