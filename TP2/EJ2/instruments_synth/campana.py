from math import *
from envelopes.DecayExp import *
from instruments_synth.fmModulation import *

import matplotlib.pyplot as plt
def nicePlot(x,y,color,xlabel,ylabel, title):
    plt.plot(x, y, color=color)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth=0.2, color='black')
    plt.grid(which='minor', linestyle=':', linewidth=0.15, color='black')
    plt.show()


def getBell(vel, fm, duration, fs):

    A0 = 1
    tau = duration/5
    fc = 2 * fm
    deltaf = (fc - fm) / 2
    I0 = deltaf / fm
    phi_m = -pi/2
    phi_c = -pi/2

    A = DecayExp(A0,tau,duration,fs)
    I = DecayExp(I0,tau,duration,fs)

    # t = arange(0, duration, 1 / fs)
    # nicePlot(t,A, "red", "Tiempo(s)", "A(t)", "Gráfico de A(t) para la campana")

    x = fmModulation(A,I,fc,fm,phi_m,phi_c,duration,fs)
    return x
