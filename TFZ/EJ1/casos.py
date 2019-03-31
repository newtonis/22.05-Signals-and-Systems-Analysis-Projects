import numpy as np
import matplotlib.pyplot as plt
from cmath import *
from math import *

maxn = 30

#[alpha,beta]=[1,-1/2]
#[alpha,beta]=[1/2,-1/8]
[alpha,beta]=[5/4,-25/32]


[z1, z1conj]=np.roots([1,-alpha,-beta])
[tita,ro]= [atan2(z1.imag, z1.real),hypot(z1.real,z1.imag)]

arr = np.linspace(1,maxn)
for i in range(1,len(arr)):
    if(i == 1):
        arr[i]=0
    else:
        arr[i] = arr[i-1] + sin( (tita)*(i-1)) * (ro)**(i-1)

plt.plot(range(0,len(arr)),arr)
plt.xlim(1,maxn)

plt.show()