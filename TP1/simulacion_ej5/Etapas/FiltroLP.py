from Etapas.Etapa import Etapa
from scipy import signal
from Globals import tf
from Globals import config
from Etapas.Senial import Senial


class FiltroLP(Etapa):
    filtroLP = None

    def __init__(self):
        pass

    def processInput(self, inputSignal):

        actual = inputSignal
        tfList = tf.getTf()

        for tfi in tfList:
            t, y, x = signal.lsim(tfi, actual.values, actual.xvar)
            actual = Senial(t, y)

        return actual


def getFiltroLP():
    if not FiltroLP.filtroLP:
        FiltroLP.filtroLP = FiltroLP()

    return FiltroLP.filtroLP
