from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from math import pi
import simpleaudio as sa
from util_python import PlaySound

fs = 44100
T = 5

rl = 1
l = 200

noise = np.random.normal(0, 1, l)
times = np.linspace(0, T, fs*T)
empty = [0] * (len(times) - len(noise))
input = np.hstack([noise, empty])


num = [0] * (l+2)
den = [0] * (l+2)

num[0] = 1/2
num[1] = 1/2

den[0] = 1
den[-2] = -1/2 * rl
den[-1] = -1/2 * rl

sys = signal.dlti(
    [0.5, 0.5],
    den,
    dt=1/fs
)

t, y = signal.dlsim(sys, input, t=times)

plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

playSound(y)

plt.plot(t, y)
plt.show()
