from numpy import linspace, exp
from math import pi


class seq:
    def __init__(self, seq, values):
        self.seq = seq
        self.values = values

    def addSample(self, xvar, yvar):
        self.seq.append(xvar)
        self.values.append(yvar)


class MathUtils:
    def __init__(self):
        pass

    def dtft(self, sequence):
        f = linspace(-1/2, 1/2, 10000)

        output = seq(f, [0] * len(f))

        for fi in range(len(f)):
            suma = 0
            for i in range(len(sequence.values)):
                suma += sequence.values[i] * exp(- 2 * pi * f[fi] * i)

            output.values[fi] = suma

        return output


mathUtils = MathUtils()