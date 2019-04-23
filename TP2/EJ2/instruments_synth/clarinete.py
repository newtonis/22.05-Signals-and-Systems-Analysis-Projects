from numpy import *
from math import *
from envelopes.woodEnv import *
from instruments_synth.fmModulation import *

def getClarinet(vel,fc,duration,fs):
    #parámetros configurables para clarinete:
    #------------------------------------
    fm = (3 / 2) * fc
    alpha = -2
    beta = 4
    t_attack = 0.3*duration
    t_sust = 0.5*duration
    t_rel = 0.2*duration
    #-------------------------------------

    y1, y2 = woodEnv(t_attack, t_sust, t_rel, fs)
    A = y1
    I = linScale(y2, alpha, beta)

    phi_m = -pi/2
    phi_c = -pi/2

    x = fmModulation(A,I,fc,fm,phi_m,phi_c,duration,fs)
    return x
