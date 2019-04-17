from math import *
from numpy import *
import numpy as np
def getBell(A0,tau,fm,fs):
    A0 = 1
    tau = 0.2
    fc = 2 * fm
    deltaf = (fc - fm) / 2
    I0 = deltaf / fm
    phi_m = -pi/2
    phi_c = -pi/2
    t = np.linspace(0, 1, num=fs)
    A = zeros(len(t))
    I = zeros(len(t))
    x = zeros(len(t))
    for index,ti in enumerate(t):
      A[index]=A0*exp(-ti/tau)
      I[index]=I0*exp(-ti/tau)
      x[index]=A[index]*cos(2*pi*fc*ti+I[index]*cos(2*pi*fm*ti+phi_m)+phi_c)
    return x