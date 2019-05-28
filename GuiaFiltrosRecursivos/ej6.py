from PyDynamic.misc import impinvar
from scipy.signal import butter, cheby1
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
from numpy import log10

def impinvar_causal(*args, **kwargs):
	"""causal version of impinvar, h[0] == 0"""

	# polynomial.polysub is ordered from lowest to highest
	from numpy.polynomial.polynomial import polysub

	bz, az = impinvar(*args, **kwargs)

	h0 = bz[0] / az[0]
	bz = polysub(bz, h0 * az)
	return bz, az


f0 = 100
w0 = 2 * pi * f0

b, a = signal.butter(4, w0 , 'low', analog=True)
w, h = signal.freqs(b, a, 100000)

w_m2 = -1

for i in range(len(w)):
    if 20*log10(abs(h[i])) <= -2 and w_m2 == -1:
        w_m2 = w[i]

b, a = signal.butter(4, w0 * (w0/w_m2), 'low', analog=True)
w, h = signal.freqs(b, a, 100000)
f = w / 2 / pi

print(b, a)
fs = 44100

b2, a2 = impinvar_causal(b, a, fs = fs, tol = 0.000000001)
print(b2, a2)

w2, h2 = signal.freqz(b2, a2, 100000)


f2 = w2 / 2 / pi * fs

plt.plot(f, 20 * np.log10(abs(h)), color="blue")
plt.plot(f2, 20 * np.log10(abs(h2/h2[0])), color="red")

plt.xscale('log')
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='green') # cutoff frequency
plt.show()