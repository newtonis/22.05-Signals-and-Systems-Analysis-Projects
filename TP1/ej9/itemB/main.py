from math import pi, sin
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
import symbol as sp

x = []
y = []

M = 4

x_range = range(-50, 50+1)
y_range = range(-int(50/4), int(50/4+1))

Nx = len(x_range)
Ny = len(y_range)

x = [sin(2 * pi * 0.125 / 2.0 * n) for n in x_range]

y = [x[n*4] for n in y_range]


tx = abs(fft(x)/Nx) # rafa
ty = abs(fft(y)/Ny) # rafa

print(tx)

int_tx = [int(i) for i in ty]



plt.plot(x_range, tx, color='blue')
plt.plot(y_range, ty, color='red')



plt.show()