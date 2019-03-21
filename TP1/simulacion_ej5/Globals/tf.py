import sympy as sp
from Utils.utils import algebra
from scipy import signal
from math import pi
from Globals import config


class TF:
    tf = None

    def __init__(self):
        self.loaded = False

    def loadTf(self):
        s = sp.symbols("s")

        wp = 2 * pi * config.FAAfreq
        H = 1/72 * 1 / ( ((s/wp)**2 + 0.5548*(s/wp) + 0.2702) *\
            ((s/wp)**2 + 0.0918*(s/wp) + 0.9870) *\
            ((s/wp)**2 + 0.4284*(s/wp) + 0.5282) *\
            ((s/wp)**2 + 0.2650*(s/wp) + 0.8013) *\
            ((s/wp)**2 + 0.6344*(s/wp) + 0.1218) )

        self.tf = algebra.conseguir_tf(H, s)
        self.loaded = True

        return self.tf


tf = TF()


def getTf():
    if not tf.loaded:
        tf.loadTf()

    return tf.tf

