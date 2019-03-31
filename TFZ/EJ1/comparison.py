import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from cmath import *
from math import *

def h(A,ro,tita,n):
    return A*(n >= 1)*(ro**(n-1))*(sin(tita*(n-1)))
def diffEq(alpha, beta, x2, y1, y2):# output is y0
    return 0.5 * x2 + alpha * y1 + beta * y2



maxn = 30

[alpha,beta]=[1,-1/2]
#[alpha,beta]=[1/2,-1/8]
#[alpha,beta]=[5/4,-25/32]


#cargamos la respuesta al impulso en y (analitica)
#-------------------------------------------------
[z1, z1conj]=np.roots([1,-alpha,-beta])
A= 0.5/(z1.imag)
[tita,ro]= [atan2(z1.imag, z1.real),hypot(z1.real,z1.imag)]
y = np.linspace(1,maxn)
for i in range(0,len(y)):
    y[i]=h(A,ro,tita,i)
#-------------------------------------------------


# cargamos la respuesta al impulso en pulse (por simulacion)
#-------------------------------------------------
step = [0, 0]
pulse = [0, 0]
for i in range(0, maxn):
    step.append(diffEq(alpha, beta, 1, step[-1], step[-2]))
    pulse.append(diffEq(alpha, beta, i == 0, pulse[-1], pulse[-2]))
# -------------------------------------------------

#plt.plot(range(0,len(y)),y, label="analitico")

markerline, stemlines, baseline = plt.stem(range(0,len(y)),y, '-.',label="analitico")
# setting property of baseline with color red and linewidth 2
plt.setp(baseline, color='r', linewidth=0.5)

plt.plot(range(0,len(pulse)),pulse,'g^',label="simulado",color="orange")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
plt.xlim(1,maxn)

plt.ylabel("Respuesta al impulso(n)")
plt.xlabel("n")
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

plt.show()