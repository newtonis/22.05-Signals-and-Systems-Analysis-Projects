from math import pi, sin
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
import matplotlib.patches as mpatches
import symbol as sp
from util_python import datacursor_easy


class seq:
    def __init__(self, seq, values):
        self.seq = seq
        self.values = values


def decimate(x, M): # s es la primera posicion
    y = []
    values = []

    s = x.values[0]
    e = x.values[-1] - 1
    #print(s)

    for i in range(-M, s-1, -M):
        y.append(x.seq[i-s])
        values.append(i)
        print(s+i)

    #print(values)

    y.reverse()
    values.reverse()

    for i in range(0, e+1, M):
        y.append(x.seq[i-s])
        values.append(i)
    #print(values)

    return seq(y, values)


def plot_data():
    fig, ax1 = plt.subplots()
    #patches = []

    n_range = range(-50, 51)

    x1 = seq([sin(2*pi * 0.125 / 2 * n) for n in n_range], n_range)
    y1 = decimate(x1, 4)


    #tx = abs(fft(x)/Nx)# rafa
    # ty = abs(fft(y)/Ny)# rafa
    #
    # ax1.plot(rx, tx, color='blue')
    # ax1.plot(ry, ty, color='red')
    #
    # patches.append(mpatches.Patch(color="blue", label="original"))
    # patches.append(mpatches.Patch(color="red", label="downsampled"))



    #plt.legend(handles=patches)
    ax1.plot(x1.values, x1.seq)
    ax1.plot(y1.values, y1.seq)

    plt.xlabel("n")
    plt.ylabel("x(n)")


    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.show()


def spectrum():
    pass



plot_data()