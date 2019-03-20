from numpy import linspace, exp
from math import pi


class seq:
    def __init__(self, xvar, yvar):
        self.xvar = xvar
        self.yvar = yvar


class MathUtils:
    def __init__(self):
        pass

    def dtft(self, sequence, fmult = 1):
        ts = sequence.xvar[1] - sequence.xvar[0]
        #print("ts = ", ts)
        fs = 1 / ts

        f = linspace(-0.5 * fs * fmult, 0.5 * fs * fmult, 10000)

        output = seq(f, [0] * len(f))

        for fi in range(len(f)):
            suma = 0
            for i in range(len(sequence.xvar)):
                suma += sequence.yvar[i] * exp(- 2j * pi * f[fi] * i / fs)

            output.yvar[fi] = abs(suma)

        return output


mathUtils = MathUtils()