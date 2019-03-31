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


#cargamos la respuesta al escalon en y (analitica)
#-------------------------------------------------
[z1, z1conj]=np.roots([1,-alpha,-beta])
A= 0.5/(z1.imag)
[tita,ro]= [atan2(z1.imag, z1.real),hypot(z1.real,z1.imag)]

(auxro,auxtita)= polar(1-z1)
(auxro2,auxtita)= polar(-1-z1)

#C D E son los coef de fracciones simples
E = 0.5/(auxro**2)
C = -E
D = -E*(beta)

y = np.linspace(1,maxn)
for i in range(0,len(y)):
    y[i]=(C/0.5)*h(A,ro,tita,i+1)+(D/0.5)*h(A,ro,tita,i)+E


# cargamos la respuesta al escalon en pulse (por simulacion)
#-------------------------------------------------
step = [0, 0]
pulse = [0, 0]
for i in range(0, maxn):
    step.append(diffEq(alpha, beta, 1, step[-1], step[-2]))
    pulse.append(diffEq(alpha, beta, i == 0, pulse[-1], pulse[-2]))
# -------------------------------------------------

markerline, stemlines, baseline = plt.stem(range(0,len(y)),y, '-.',label="analitico")
plt.setp(baseline, color='r', linewidth=0.5)
plt.plot(range(0,len(step)),step,'g^',label="simulado",color="orange")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
#------------------------
plt.xlim(1,maxn)
plt.ylabel("Respuesta al escalón(n)")
plt.xlabel("n")
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
plt.show()