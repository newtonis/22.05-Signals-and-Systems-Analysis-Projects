

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
        self.shift = 0
        self.xvarStart = 0
        self.xvarEnd = None
        self.mode = "no-filter"

    def setMode(self, mode):
        self.mode = mode

    def setShowStartXvar(self, xvar):
        self.xvarStart = xvar

    def setShowEndXvar(self, xvar):
        self.xvarEnd = xvar

    def setShift(self, shift):
        self.shift = shift

    def addSample(self, timeIndex, valuesIndex):
        self.xvar.append(timeIndex)
        self.values.append(valuesIndex)

    def getSamplesBetweenLimits(self):
        xvar = []
        yvar = []
        index = 0
        for x in self.xvar:
            if not self.xvarEnd or self.xvarStart < x < self.xvarEnd:
                xvar.append(x)
                yvar.append(self.values[index])

            index += 1

        return xvar, yvar

    def getSamplesChangeXvar(self):
        xvar = []
        yvar = []

        currentTime = self.xvarStart
        index = 0

        advance = 0

        while index < len(self.xvar)-1 and advance < self.shift:
            advance += self.xvar[index+1] - self.xvar[index]
            index += 1

        while index < len(self.xvar)-1 and (not self.xvarEnd or currentTime < self.xvarEnd):

            xvar.append(currentTime)
            yvar.append(self.values[index])

            currentTime += self.xvar[index+1] - self.xvar[index]

            index += 1

        return xvar, yvar



