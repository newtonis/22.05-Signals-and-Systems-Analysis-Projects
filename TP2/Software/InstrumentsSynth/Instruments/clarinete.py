from math import *
from envelopes.woodEnv import *
from InstrumentsSynth.Instruments.fmModulation import *


def getClarinet(vel,f0,duration,fs):
    #parámetros configurables para clarinete:
    #------------------------------------
    fm = 3 * f0
    fc = 2 * f0

    t_attack = (1/9)*duration
    t_sust = (7/9)*duration
    t_rel = (2/9)*duration

    #-------------------------------------


    alpha = -2
    beta = 4
    y1, y2 = woodEnv(t_attack, t_sust, t_rel, fs)
    A = y1
    I = linScale(y2, alpha, beta)
    phi_m = -pi/2
    phi_c = -pi/2
    x = fmModulation(A,I,fc,fm,phi_m,phi_c,duration,fs)
    return x
