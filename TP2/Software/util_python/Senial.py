from numpy import cos, angle, pi
from scipy.fftpack import fft
import numpy as np
import csv

eps = 1E-5


class Senial:
    def __init__(self, xvar = [], values = []):
        self.xvar = xvar #arreglos de tiempo y valores
        self.values = values

        self.separation = -1
        self.uniforme = True
        for i in range(1, len(self.xvar)):
            if self.separation == -1:
                self.separation = self.xvar[i] - self.xvar[i - 1]
            else:
                if abs(self.xvar[i] - self.xvar[i-1] - self.separation) > eps:
                    #print("Warning: separacion de tiempos no uniforme")
                    self.uniforme = False

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


    def fourierEvaluarReconstruccion(self, t, fs = 1):
        self.coef = fft(self.values)

        t = t - self.xvar[0]
        sm = 0

        for k in range(len(self.coef)//2): #len(self.coef)):
            xk = self.coef[k]
            f = k*fs/len(self.coef)

            sm += 2 * abs(xk) * cos(2 * pi * t * f + np.angle(xk)) # * exp(1j*2*pi*t*f)

        return 1/len(self.coef) * sm

    def writeCSV(self, filename, fieldA = "x", fieldB = "y"):
        row = [fieldA, fieldB]

        data = dict()
        data[fieldA] = self.xvar
        data[fieldB] = self.values

        with open(filename) as csvFile:
            fields = [fieldA, fieldB]
            writer = csv.DictWriter(csvFile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

        csvFile.close()


    def loadFromCSV(self, filename, fieldA = "x", fieldB = "y"):
        self.xvar = []
        self.values = []

        with open(filename, 'r') as csvFile:
            reader = csv.reader(csvFile)
            firstRow = False
            content = dict()
            for row in reader:
                if firstRow:
                    keys = row
                else:
                    for i in row:
                        if not content.has_key(keys[i]):
                            content[keys[i]] = []

                        content[keys[i]].append(i)
                self.xvar = content[fieldA]
                self.values = content[fieldB]
