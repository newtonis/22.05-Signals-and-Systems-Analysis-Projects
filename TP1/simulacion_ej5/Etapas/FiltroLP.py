from Etapas.Etapa import Etapa
from scipy import signal
from Globals import tf
from Etapas.Senial import Senial


class FiltroLP(Etapa):
    def __init__(self):
        pass

    def processInput(self, inputSignal):
        t, y, x = signal.lsim(tf.getTf(), inputSignal.time, inputSignal.values)

        return Senial(t, y)

