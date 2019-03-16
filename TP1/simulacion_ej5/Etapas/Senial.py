

eps = 1E-5


class Senial:
    def __init__(self, xvar, values):
        self.xvar = xvar #arreglos de tiempo y valores
        self.values = values

        self.separation = -1
        for i in range(1, len(self.xvar)):
            if self.separation == -1:
                self.separation = self.xvar[i] - self.xvar[i - 1]
            else:
                if abs(self.xvar[i] - self.xvar[i-1] - self.separation) > eps:
                    raise Exception("separacion de tiempos no uniforme")

    def addSample(self, timeIndex, valuesIndex):
        self.xvar.append(timeIndex)
        self.values.append(valuesIndex)




