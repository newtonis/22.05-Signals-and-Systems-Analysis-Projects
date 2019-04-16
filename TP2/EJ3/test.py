from math import *
from numpy import *
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio
def synthesize(sampling_speed, wavetable, n_samples):
    """Synthesizes a new waveform from an existing wavetable."""
    samples = []
    current_sample = 0
    while len(samples) < n_samples:
        current_sample += sampling_speed
        current_sample = current_sample % wavetable.size
        samples.append(wavetable[current_sample])
        current_sample += 1
    return np.array(samples)

A = 1
I = 1
fc = 1e3
fm = 500
phi_m = -pi/2
phi_c = -pi/2

maxn = 100
freq = 10
t = linspace(0,1,freq)
x = zeros(len(t))
for index,ti in enumerate(t):
    x[index]=A*cos(2*pi*fc*ti+I*cos(2*pi*fm*ti+phi_m)+phi_c)
#    x[index]=sin(ti*440)


fs = 44100
Audio(x, rate=fs)
plt.plot(t,x)
plt.show()
fs = 8000
t = np.linspace(0, 1, num=fs)
wavetable = np.sin(np.sin(2 * np.pi * t))
sample1 = synthesize(220, wavetable, 2 * fs)
sample2 = synthesize(440, wavetable, 2 * fs)
Audio(sample1, rate=fs)