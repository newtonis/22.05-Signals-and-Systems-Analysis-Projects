from util_python import Senial
from ExpressPlot import ExpressPlot
import matplotlib.pyplot as plt
import mido
from IPython.display import Audio
import numpy as np
from numpy import cos, sin, pi
import simpleaudio as sa


def synthetize(fs, wavetable, nsamples):
    samples = []
    current_sample = 0

s1 = Senial.Senial().loadFromCSV(
    filename="Signals/cos_f_440.csv"
)

do = 261.626
dob = 277.1826
re = 293.665
reb = 311.1270
mi = 329.628
fa = 349.228
fab = 369.9944
sol = 391.99
solb = 415.3047
la = 440.000
si = 493.883

ExpressPlot.CombinedPlot()\
    .addSignalPlot(signal=s1, color="blue", name="cos 440hz")\
    .setXTitle("tiempo")\
    .setYTitle("valor")\
    .plotAndSave("Output/test_cos_f_440.png")
#plt.show()

fs = 44100
T = 1
times = np.linspace(0, T, T * fs)


y1 = cos(2*pi*mi*times) + cos(2*pi*do*times)
y2 = cos(2*pi*sol*times)+ cos(2*pi*mi*times)
y3 = cos(2*pi*do*times) + cos(2*pi*reb*times)
y4 = cos(2*pi*re*times) + cos(2*pi*fa*times)
y5 = cos(2*pi*mi*times) + cos(2*pi*sol*times)

y = np.hstack([y1, y2, y3, y4, y5])

y *= 32767 / max(abs(y))
y = y.astype(np.int16)
play_obj = sa.play_buffer(y, 1, 2, fs)

play_obj.wait_done()