from math import pi, sin
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
import matplotlib.patches as mpatches
import symbol as sp
from util_python import datacursor_easy
from MathUtils import *


def decimate(x, M): # s es la primera posicion
    y = []
    values = []

    s = x.xvar[0]
    e = x.xvar[-1] - 1
    #print(s)

    for i in range(-M, s-1, -M):
        y.append(x.yvar[i-s])
        values.append(i)

    y.reverse()
    values.reverse()

    for i in range(0, e+1, M):
        y.append(x.yvar[i-s])
        values.append(i)

    return seq(values, y)


def evaluateDTFT(inputSignal):
    pass


def plot_data():
    fig, ax1 = plt.subplots()
    #patches = []

    n_range = range(-50, 51)

    x1 = seq(n_range, [sin(2*pi * 0.25 * n) for n in n_range])
    y1 = decimate(x1, 4)

    x1dtft = mathUtils.dtft(x1)
    y1dtft = mathUtils.dtft(y1, 4)


    #tx = abs(fft(x)/Nx)# rafa
    # ty = abs(fft(y)/Ny)# rafa
    #
    # ax1.plot(rx, tx, color='blue')
    # ax1.plot(ry, ty, color='red')
    #

    patches = []
    patches.append(mpatches.Patch(color="blue", label="original"))
    patches.append(mpatches.Patch(color="tomato", label="downsampled"))



    plt.legend(handles=patches)
    ax1.plot(x1dtft.xvar, x1dtft.yvar, "blue")
    ax1.plot(y1dtft.xvar, y1dtft.yvar, "tomato")

    plt.xlabel("frecuencia (hz)")
    plt.ylabel("amplitud")


    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.show()

plot_data()