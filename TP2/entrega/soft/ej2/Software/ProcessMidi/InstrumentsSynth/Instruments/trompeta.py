from math import *
from envelopes.BrassEnv import *
#from instruments_synth.fmModulation import *
from ProcessMidi.InstrumentsSynth.Instruments.fmModulation import fmModulation
from envelopes.woodEnv import *
from audiolazy.lazy_midi import *
import numpy as np
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

def brassenv(duration,fs):
    t = arange(0,duration,1/fs)
    ytot = zeros(len(t))

    attackT = duration / 6
    sustainT1 = duration / 6
    sustainT2 = duration / 2
    releaseT = duration / 6

    atime=np.arange(0,attackT-1/fs, 1/fs)
    yatt= atime/attackT
    stime1=np.arange(0,sustainT1-1/fs,1/fs)
    ysus1=1-stime1/(4*sustainT1)
    stime2=np.arange(0,sustainT2-1/fs,1/fs)
    ysus2=0.75-stime2*3/(20*sustainT2)
    rtime=np.arange(0,releaseT-1/fs,1/fs)
    yrel=0.6-rtime*3/(5*releaseT)
    y=np.concatenate((yatt,ysus1,ysus2,yrel))
    min_len = min(len(y), len(ytot))
    for i in range(min_len):
        ytot[i] = y[i]

    return [ytot, ytot]

def getTrumpet(vel,f0,duration,fs):
    #parámetros configurables para clarinete:
    #------------------------------------
    fm = f0
    fc = f0

    [A,I]=brassenv(duration,fs)

    phi_m = -pi/2
    phi_c = -pi/2

    I = 10 * I
    # t = arange(0,duration,1/fs)
    # plt.plot(t,I)
    # plt.show()
    # #nicePlot(t,I,"orange","Tiempo(s)","I(t)","Gráfico de I(t) para el trombón")

    x = fmModulation(A,I,fc,fm,phi_m,phi_c,duration,fs)
    return x



