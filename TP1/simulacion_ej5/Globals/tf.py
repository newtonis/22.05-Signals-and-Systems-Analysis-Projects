import sympy as sp
from Utils.utils import algebra
from scipy import signal
from math import pi
from Globals import config


class TF:
    def __init__(self):
        self.tf = []

    def loadTf(self):
        s = sp.symbols("s")

        wp = 2 * pi * config.GetConfigData().FAAfreq
        self.addTf(1 / ((s/wp)**2 + 0.5548*(s/wp) + 0.2702), s)
        self.addTf(1 / ((s/wp)**2 + 0.0918*(s/wp) + 0.9870), s)
        self.addTf(1 / ((s/wp)**2 + 0.4284*(s/wp) + 0.5282), s)
        self.addTf(1 / ((s/wp)**2 + 0.2650*(s/wp) + 0.8013), s)
        self.addTf(1 / (72*((s/wp)**2 + 0.6344*(s/wp) + 0.1218)), s)

        return self.tf

    def addTf(self, exp, s):
        self.tf.append(algebra.conseguir_tf(exp, s))


tf = None


def getTf():
    global tf
    if not tf:
        tf = TF()
        tf.loadTf()

    return tf.tf
