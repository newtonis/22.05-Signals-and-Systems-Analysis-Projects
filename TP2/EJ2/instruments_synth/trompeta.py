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


    A = brassToneEnv(duration, fs)

    y1, y2 = woodEnv(duration, fs)

    I = y2 * 3

    phi_m = -pi/2
    phi_c = -pi/2

    if len(A) != len(I):
        print("ayudaa")
        print(len(A))
        print(len(I))

    x = fmModulation(A,I,fc,fm,phi_m,phi_c,duration,fs)


    return x
