from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from math import pi


fs = 10000

noise = np.random.normal(0, 0.1, fs//10)
times = np.linspace(0, 1, fs//10)
rl = 1.01
l = 40

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

t, y = signal.dlsim(sys, noise, t=times)

plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

plt.plot(t, y)

plt.show()
