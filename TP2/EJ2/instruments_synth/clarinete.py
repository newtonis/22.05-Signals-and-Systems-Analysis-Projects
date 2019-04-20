from numpy import *
from math import *
from envelopes.woodEnv import *
from instruments_synth.fmModulation import *

def getClarinet(vel,fc,fs):
    #parámetros configurables para clarinete:
    #------------------------------------
    fm = (3 / 2) * fc
    alpha = -2
    beta = 4
    t_attack = 0.2
    t_sust = 0.1
    t_rel = 0.1
    #-------------------------------------

    y1, y2 = woodEnv(t_attack, t_sust, t_rel, fs)
    A = y1
    I = linScale(y2, alpha, beta)

    phi_m = -pi/2
    phi_c = -pi/2

    duration = t_attack+t_sust+t_rel

    x = fmModulation(A,I,fc,fm,phi_m,phi_c,duration,fs)



    return x,duration
