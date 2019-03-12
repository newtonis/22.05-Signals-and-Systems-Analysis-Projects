from math import pi, sin
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
import matplotlib.patches as mpatches
import symbol as sp
from util_python import datacursor_easy


def plot_data():
    fig, ax1 = plt.subplots()
    patches = []

    x = []
    y = []

    M = 4

    x_range = range(-50, 50+1)
    y_range = range(-int(50/4), int(50/4)+1)

    rx = range(101)
    ry = range(0, 100, 4)

    Nx = len(x_range)
    Ny = len(y_range)

    x = [sin(2*pi * 0.25 * n) for n in x_range]

    y = [x[4*n] for n in y_range]

    tx = abs(fft(x)/Nx) # rafa
    ty = abs(fft(y)/Ny) # rafa

    ax1.plot(rx, tx, color='blue')
    ax1.plot(ry, ty, color='red')

    patches.append(mpatches.Patch(color="blue", label="original"))
    patches.append(mpatches.Patch(color="red", label="downsampled"))

    plt.legend(handles=patches)
    plt.xlabel("Armpónico (n)")
    plt.ylabel("Valor")

    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.show()



plot_data()