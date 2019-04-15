from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from math import pi


fs = 10000


rl = 1
l = 10

num = [0] * (l+2)
den = [0] * (l+2)

num[0] = 1/2
num[1] = -1/2

den[0] = 1
den[-2] = 1/2 * rl
den[-1] = 1/2 * rl

sys = signal.dlti(
    [0.5, 0.5],
    den,
    dt=1/fs
)


w_values = np.linspace(0, pi, 100000)

w, mag, pha = sys.bode(w_values)

f = [i/2/pi for i in w]
mag = [10**(i/20) for i in mag]

plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

plt.plot(f, mag)

plt.show()
