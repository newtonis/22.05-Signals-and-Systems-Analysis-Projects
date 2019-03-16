

class Senial:
    def __init__(self, time, values):
        self.time = time #arreglos de tiempo y valores
        self.values = values

    def addSample(self, timeIndex, valuesIndex):
        self.time.append(timeIndex)
        self.values.append(valuesIndex)
