from math import *
from envelopes.woodEnv import *
from instruments_synth.fmModulation import *
from audiolazy.lazy_midi import *

def getClarinet(vel,f0,duration,fs):
    #parámetros configurables para clarinete:
    #------------------------------------
    # fm = (3 / 2) * fc
    # fm = 3*f0
    # fc = 2*f0
    fm = 3 * f0
    fc = 2 * f0

    alpha = -2
    beta = 4

    t_attack = 0.05*duration
    t_sust = 0.65*duration
    t_rel = 0.30*duration

    #-------------------------------------

    y1, y2 = woodEnv(t_attack, t_sust, t_rel, fs)
    A = y1
    I = linScale(y2, alpha, beta)

    phi_m = -pi/2
    phi_c = -pi/2

    x = fmModulation(A,I,fc,fm,phi_m,phi_c,duration,fs)
    return x
