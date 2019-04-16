import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
#import math
from numpy import *
from math import *
def woodenv(att,sus,rel,fs):
    #att = attack time es como 5tau
    tau_att = att/5
    tau_rel = rel/5
    # = > t_att = 1-exp(-t/tau)
    total_t = att+sus+rel
    t = np.linspace(0, total_t, num=fs)
    y1 = np.zeros(len(t))
    y2 = np.zeros(len(t))
    for index,ti in enumerate(t):
        if(ti<=att):
            t2 = att
            alpha = (math.log(2))/t2
            y1[index] = np.exp(alpha*ti)-1
            y2[index] = np.exp(alpha*ti)-1
        elif( att<ti and ti<att+sus ):
            y1[index] = 1
            y2[index] = 1
        elif(ti>=att+sus and ti<att+sus+rel/2):
            tau = (rel/2)*(1/(5-math.log(2)))
            taux = ti-(att+sus)
            taux2 = rel/2-taux  # taux2 hace que el tiempo vaya de rel/2 a 0
            taux2 = (5*tau-rel/2)+taux2 # y ahora hacemos que vaya de 5tau a t2=ln(2)tau
            y1[index]=1-np.exp(-(taux2)/tau)
            y2[index] = 1
        elif(ti>=att+sus+rel/2):
            tau = (rel/2)/5
            y1[index] = (1/2)*np.exp(-(ti-(att+sus+rel/2))/(tau))
            y2[index] = 1
    return t,y1,y2
def scale(t,ynorm,alpha,beta):
    y = alpha*ynorm + beta
    return t,y
def getClarinet(A,I,fc,fm,fs):
  phi_m = -pi/2
  phi_c = -pi/2
  t = np.linspace(0, 1, num=fs)
  x = zeros(len(t))
  for index,ti in enumerate(t):
    x[index]=A[index]*cos(2*pi*fc*ti+I[index]*cos(2*pi*fm*ti+phi_m)+phi_c)
  return x

fs = 8000
t,y1,y2 = woodenv(0.2,0.1,0.1,fs)
fc = 1000
fm = (3/2)*fc
alpha = -2
beta = 4
A = y1
t,I = scale(t,y2,alpha,beta)
x = getClarinet(A,I,fc,fm,fs)

Audio(x, rate=fs)