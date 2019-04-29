from math import *
from envelopes.BrassEnv import *
from instruments_synth.fmModulation import *
from envelopes.woodEnv import *
from audiolazy.lazy_midi import *
import matplotlib.pyplot as plt

def getBrassTone(vel,f0,duration,fs):
    #parámetros configurables para clarinete:
    #------------------------------------
    fm = f0
    fc = f0

    att = (1 / 6) * duration
    decay = (1 / 3 - 1 / 6) * duration
    sus = (1 - (1 / 6 + 1 / 3)) * duration
    rel = (1 / 6) * duration

    I = brassToneEnv(att, decay, sus, rel, fs)


    y1, y2 = woodEnv(att,decay+sus,rel, fs)

    A = y1

    phi_m = -pi/2
    phi_c = -pi/2

    x = fmModulation(A,I,fc,fm,phi_m,phi_c,duration,fs)
    return x
