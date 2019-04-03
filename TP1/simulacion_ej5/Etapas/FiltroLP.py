from Etapas.Etapa import Etapa
from scipy import signal
from Globals import tf
from Globals import config
from Etapas.Senial import Senial
from numpy import multiply


class FiltroLP(Etapa):
    filtroLP = None

    def __init__(self):
        pass

    def processInput(self, inputSignal, loadingModel, fraction):

        actual = inputSignal
        tfList = tf.getTf()
        paso = fraction / len(tfList)
        for tfi in tfList:
            t, y, x = signal.lsim(tfi, actual.values, actual.xvar)
            actual = Senial(t, y)
            if loadingModel:
                loadingModel.update(paso)

        return actual

    def getBode(self, wAsked):
        return signal.bode(tf.getGeneralTf(), wAsked)


def getFiltroLP():
    if not FiltroLP.filtroLP:
        FiltroLP.filtroLP = FiltroLP()

    return FiltroLP.filtroLP
