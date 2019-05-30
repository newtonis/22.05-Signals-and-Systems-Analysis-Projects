import sympy as sp
from numpy import pi, log10, linspace
from util_python import Senial
from scipy import signal
from numpy import pi
from util_python.utils import algebra
from ExpressPlot.ExpressPlot import CombinedPlot


s = sp.symbols("s")


f0 = 760
w0 = 2 * pi * f0
q = 0.54

t1 = w0**2 / (s**2 + w0/q + w0**2)

f0 = 960
w0 = 2 * pi * f0
q = 0.95

t2 = w0**2 / (s**2 + w0/q + w0**2)

f0 = 1110
w0 = 2 * pi * f0
q = 3.1

t3 = w0**2 / (s**2 + w0/q + w0**2)


t = t1 * t2 * t3

tf = algebra.conseguir_tf(t, s)

k = 1e3
fs = 20 * k

tf2 = signal.dlti(*signal.bilinear(tf.num, tf.den, fs))

w_range = linspace(0, fs, 100000) * 2 * pi

w, h = signal.freqresp(tf, w_range)

w2, h2 = signal.dfreqresp(tf2, w_range / fs)

f = w / 2 / pi
f2 = w2 / 2 / pi

CombinedPlot() \
        .setTitle("Legendre") \
        .setXTitle("Frecuencia (hz)") \
        .setYTitle("Amplitud (Db)") \
        .addSignalPlot(
        signal=Senial.Senial(
            f, 20 * log10(abs(h))
        ),
        color="red",
        name="Analógica"
    ) \
        .addSignalPlot(
        signal=Senial.Senial(
            f2, 20 * log10(abs(h2))
        ),
        color="blue",
        name="Digital método invariante al impulso"
    ).plot().show()#save("output/" + filename)






