from numpy import pi, log10, linspace
from scipy import signal
from numpy import exp
from ExpressPlot.ExpressPlot import CombinedPlot
from util_python import Senial


def calcularPlotMatchedZ(f0, fs, mode = "butter", n = 4, filename="out.png", title="noTitle"):
    f0 = 100
    w0 = 2 * pi * f0

    if mode == "butter":
        b, a = signal.butter(n, w0, 'low', analog=True)
    elif mode == "cheby":
        b, a = signal.cheby1(n, 1, w0, 'low', analog=True)

    sys = signal.lti(b, a)

    w_range = linspace(0, fs, 100000) * 2 * pi

    w, h = signal.freqresp(sys, w_range)  # signal.freqs(b, a, 100000)

    w_m2 = -1

    for i in range(len(w)):
        if 20 * log10(abs(h[i])) <= -2 and w_m2 == -1:
            w_m2 = w[i]

    if mode == "butter":
        b, a = signal.butter(n, w0 * (w0 / w_m2), 'low', analog=True)
    elif mode == "cheby":
        b, a = signal.cheby1(n, 1, w0 * (w0 / w_m2), 'low', analog=True)

    sys = signal.lti(b, a)
    w, h = signal.freqresp(sys, w_range)
    f = w / 2 / pi


    poles = sys.poles
    zeros = sys.zeros

    new_poles = exp(poles/fs)
    new_zeros = exp(zeros/fs)

    #print(new_poles, new_zeros)

    sys = signal.dlti(new_zeros, new_poles, 1)

    w2, h2 = signal.dfreqresp(sys, w_range/fs)
    f = w / 2 / pi

    factor = h[0] / h2[0]

    f2 = w2 / 2 / pi * fs

    CombinedPlot() \
        .setTitle(title) \
        .setXTitle("Frecuencia (hz)") \
        .setYTitle("Amplitud (Db)") \
        .addSignalPlot(
        signal=Senial.Senial(
            f, 20 * log10(abs(h))
        ),
        color="red",
        name="Analógica"
        )\
        .addSignalPlot(
        signal=Senial.Senial(
            f2, 20 * log10(abs(h2) * factor)
        ),
        color="blue",
        name="Digital método invariante al impulso"
        ).plot().save("output/" + filename)


k = 1e3

fs = 10 * k
alpha = 5

for n in [2, 3, 4, 5, 6, 7, 8]:
	print("procesando n = ", n)
	calcularPlotMatchedZ(
		f0=fs / alpha,
		fs=fs,
		mode="cheby",
		n=n,
		filename="cheby_matched_z/alpha=5/cheby_n="+str(n)+".png",
		title="cheby n="+str(n)+" alpha="+str(alpha)
	)
	calcularPlotMatchedZ(
		f0=fs / alpha,
		fs=fs,
		mode="butter",
		n=n,
		filename="butter_matched_z/alpha=5/butter_n=" + str(n) + ".png",
		title="butter n=" + str(n) + " alpha=" + str(alpha)
	)

alpha = 8

for n in [2, 3, 4, 5, 6, 7, 8]:
	print("procesando n = ", n)
	calcularPlotMatchedZ(
		f0=fs / alpha,
		fs=fs,
		mode="cheby",
		n=n,
		filename="cheby_matched_z/alpha=8/cheby_n="+str(n)+".png",
		title="cheby n=" + str(n) + " alpha=" + str(alpha)
	)
	calcularPlotMatchedZ(
		f0=fs / alpha,
		fs=fs,
		mode="butter",
		n=n,
		filename="butter_matched_z/alpha=8/butter_n=" + str(n) + "_alpha=8.png",
		title="butter n=" + str(n) + " alpha=" + str(alpha)
	)




