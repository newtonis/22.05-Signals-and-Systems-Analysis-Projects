from scipy.fftpack import fft
import numpy as np
from Etapas import Senial


def fourierTransform(senial):
    # Hacemos una aproximacion discreta muy buena de la transformada de fourier bilateral de la senial

    frecuencyStep = 1 / ((len(senial.xvar)-1) * senial.separation)#la senial debe estar mostrada de manera equiespaciada

    fftOutput = 1/len(senial.values) * abs(fft(senial.values))

    iValsPositive = []
    ampPositive = []
    iValsNegative = []
    ampNegative = []

    for i in range(len(fftOutput)//20):
        iValsPositive.append(i)
        ampPositive.append(fftOutput[i])

    i = -1
    while len(iValsNegative) + len(iValsPositive) < len(fftOutput)//10:
        iValsNegative.append(i)
        ampNegative.append(fftOutput[i])
        i = i - 1

    iValsNegative.reverse()
    ampNegative.reverse()

    iVals = iValsNegative + iValsPositive
    amplitud = ampNegative + ampPositive

    frecuencies = [frecuencyStep * i for i in iVals]

    return Senial.Senial(frecuencies, amplitud)
