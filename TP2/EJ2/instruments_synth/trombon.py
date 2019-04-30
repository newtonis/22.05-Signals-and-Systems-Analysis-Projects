from math import *
from envelopes.BrassEnv import *
from instruments_synth.fmModulation import *
from envelopes.woodEnv import *
from audiolazy.lazy_midi import *
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

def getBrassTone(vel,f0,duration,fs):
    #parámetros configurables para clarinete:
    #------------------------------------
    fm = f0
    fc = f0

    A = brassToneEnv(duration, fs)

    y1, y2 = woodEnv(duration, fs)

    alpha = -2
    beta = 4

    #I = linScale(y2, alpha, beta)
    I = y1
    I *= 3
    phi_m = -pi/2
    phi_c = -pi/2

    # t = arange(0,duration,1/fs)
    # nicePlot(t,I,"orange","Tiempo(s)","I(t)","Gráfico de I(t) para el trombón")

    x = fmModulation(A,I,fc,fm,phi_m,phi_c,duration,fs)
    return x
