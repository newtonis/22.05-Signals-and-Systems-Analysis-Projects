from PyDynamic.misc import impinvar
from ExpressPlot.ExpressPlot import CombinedPlot
from util_python import Senial

from scipy.signal import butter, cheby1
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, log10, linspace


#### Codigo de https://github.com/eichstaedtPTB/PyDynamic/blob/master/PyDynamic/misc/impinvar.py #####

## LICENCIA ##
## Copyright (c) 2007 R.G.H. Eschauzier <reschauzier@yahoo.com>
# Copyright (c) 2011 Carnë Draug <carandraug+dev@gmail.com>
# Copyright (c) 2011 Juan Pablo Carbajal <carbajal@ifi.uzh.ch>
# Copyright (c) 2016 Sascha Eichstaedt <sascha.eichstaedt@ptb.de>
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, see <http://www.gnu.org/licenses/>.
## FIN LICENCIA ##

def impinvar_causal(*args, **kwargs):
	"""causal version of impinvar, h[0] == 0"""

	# polynomial.polysub is ordered from lowest to highest
	from numpy.polynomial.polynomial import polysub

	bz, az = impinvar(*args, **kwargs)

	h0 = bz[0] / az[0]
	bz = polysub(bz, h0 * az)
	return bz, az
### fin Código de https://github.com/eichstaedtPTB/PyDynamic/blob/master/PyDynamic/misc/impinvar.p ######



def calcularPlotImpinvar(f0, fs, mode = "butter", n = 4, filename="out.png", title="noTitle"):

	f0 = 100
	w0 = 2 * pi * f0

	if mode == "butter":
		b, a = signal.butter(n, w0, 'low', analog=True)
	elif mode == "cheby":
		b, a = signal.cheby1(n, 1, w0, 'low', analog=True)

	sys = signal.lti(b, a)

	w_range = linspace(0, fs, 100000)*2*pi

	w, h = signal.freqresp(sys, w_range)#signal.freqs(b, a, 100000)

	w_m2 = -1

	for i in range(len(w)):
		if 20*log10(abs(h[i])) <= -2 and w_m2 == -1:
			w_m2 = w[i]

	if mode == "butter":
		b, a = signal.butter(n, w0 * (w0/w_m2), 'low', analog=True)
	elif mode == "cheby":
		b, a = signal.cheby1(n, 1, w0 * (w0 / w_m2), 'low', analog=True)


	sys = signal.lti(b, a)

	w, h = signal.freqresp(sys, w_range)
	f = w / 2 / pi

	b2, a2 = impinvar_causal(b, a, fs = fs, tol = 0.0001)

	sys = signal.dlti(b2, a2)

	w2, h2 = signal.dfreqresp(sys, w_range/fs)

	factor = h[0] / h2[0]

	f2 = w2 / 2 / pi * fs

	CombinedPlot()\
	.setTitle(title)\
	.setXTitle("Frecuencia (hz)")\
	.setYTitle("Amplitud (Db)")\
	.addSignalPlot(
		signal=Senial.Senial(
			f, 20*log10(abs(h))
		),
		color="red",
		name="Analógica"
	).addSignalPlot(
		signal=Senial.Senial(
			f2, 20*log10(abs(h2) * factor)
		),
		color="blue",
		name="Digital método invariante al impulso"
	).plot().save("output/"+filename)

	#plt.plot(f, 20 * np.log10(abs(h)), color="blue")
	#plt.plot(f2, 20 * np.log10(abs(h2/h2[0])), color="red")

k = 1e3

fs = 10 * k
alpha = 5

for n in [2, 3, 4, 5, 6, 7, 8]:
	print("procesando n = ", n)
	calcularPlotImpinvar(
		f0=fs / alpha,
		fs=fs,
		mode="cheby",
		n=n,
		filename="cheby/alpha=5/cheby_n="+str(n)+".png",
		title="cheby n="+str(n)+" alpha="+str(alpha)
	)
	calcularPlotImpinvar(
		f0=fs / alpha,
		fs=fs,
		mode="butter",
		n=n,
		filename="butter/alpha=5/butter_n=" + str(n) + ".png",
		title="butter n=" + str(n) + " alpha=" + str(alpha)
	)

alpha = 8

for n in [2, 3, 4, 5, 6, 7, 8]:
	print("procesando n = ", n)
	calcularPlotImpinvar(
		f0=fs / alpha,
		fs=fs,
		mode="cheby",
		n=n,
		filename="cheby/alpha=8/cheby_n="+str(n)+".png",
		title="cheby n=" + str(n) + " alpha=" + str(alpha)
	)
	calcularPlotImpinvar(
		f0=fs / alpha,
		fs=fs,
		mode="butter",
		n=n,
		filename="butter/alpha=8/butter_n=" + str(n) + "_alpha=8.png",
		title="butter n=" + str(n) + " alpha=" + str(alpha)
	)

# plt.xscale('log')
# # plt.title('Butterworth filter frequency response')
# # plt.xlabel('Frequency [Hz]')
# # plt.ylabel('Amplitude [dB]')
# # plt.margins(0, 0.1)
# # plt.grid(which='both', axis='both')
# # plt.axvline(100, color='green') # cutoff frequency
# # plt.show()