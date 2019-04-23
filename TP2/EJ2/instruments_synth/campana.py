from math import *
from numpy import *
from envelopes.DecayExp import *
from instruments_synth.fmModulation import *

import matplotlib.pyplot as plt

def getBell(vel, fm, duration, fs):

    fm = 220
    A0 = 1
    tau = duration/5
    fc = 2 * fm
    deltaf = (fc - fm) / 2
    I0 = deltaf / fm
    phi_m = -pi/2
    phi_c = -pi/2

    t = arange(0, duration, 1 / fs)
    A = DecayExp(A0,tau,duration,fs)
    I = DecayExp(I0,tau,duration,fs)

    x = fmModulation(A,I,fc,fm,phi_m,phi_c,duration,fs)
    return x
