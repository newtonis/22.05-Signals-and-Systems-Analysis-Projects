from numpy import *


def fmModulation(A,I,fc,fm,phi_m,phi_c,duration,fs):
    t = arange(0,duration,1/fs)
    x = zeros(len(t))
    for index,ti in enumerate(t):
        x[index]=A[index]*cos(2*pi*fc*ti+I[index]*cos(2*pi*fm*ti+phi_m)+phi_c)
    return x
