from math import *
from envelopes.woodEnv import *
from ProcessMidi.InstrumentsSynth.Instruments.fmModulation import fmModulation
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


def getClarinet(vel,f0,duration,fs):
    #parámetros configurables para clarinete:
    #------------------------------------
    fm = 3 * f0
    fc = 2 * f0
    #-------------------------------------


    alpha = -2
    beta = 4
    y1, y2 = woodEnv(duration, fs)

    A = y1

    I = linScale(y2, alpha, beta)

    phi_m = -pi/2
    phi_c = -pi/2

    # t = arange(0, duration, 1 / fs)
    # nicePlot(t, I, "orange", "Tiempo(s)", "I(t)", "Gráfico de I(t) para el clarinete")

    x = fmModulation(A,I,fc,fm,phi_m,phi_c,duration,fs)
    return x
