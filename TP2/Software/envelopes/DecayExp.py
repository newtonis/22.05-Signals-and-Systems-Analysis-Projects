from numpy import *


def DecayExp(A0,tau,duration,fs):
    t = arange(0, duration, 1/fs)
    A = zeros(len(t))
    for index, ti in enumerate(t):
        A[index] = A0*exp(-ti/tau)
    return A
