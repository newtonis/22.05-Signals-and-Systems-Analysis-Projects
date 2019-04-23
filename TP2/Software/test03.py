from Systems import Ej5SystemA

from scipy import signal
from ExpressPlot import ExpressPlot
import matplotlib.pyplot as plt
import numpy as np
from util_python import Senial
import simpleaudio as sa
from numpy import sin

sys = Ej5SystemA.getSystem(
    rl = 1,
    l = 10
)
fs = 44100

#print(sys.zeros)
# ExpressPlot.CombinedPlot()\
#     .addPolarPlotFromComplex(
#         sys.poles,
#         "x",
#         "r",
#         "Polos"
#     )\
#     .addPolarPlotFromComplex(
#         sys.zeros,
#         "o",
#         "b",
#         "Ceros"
#     )\
#     .setFs(44100)\
#     .plotAndSave(
#     "Output/polosSysA.png"
#     )



w, H = sys.freqresp()

w = w/2/np.pi * fs/1000



ExpressPlot.CombinedPlot()\
    .addSignalPlot(
        Senial.Senial(w, H),
        color="blue",
        name="Magnitud"
    )\
    .setTitle("Respuesta en frecuencia")\
    .setXTitle("Frecuencia (kHz)")\
    .setYTitle("Amplitud (veces)")\
    .plotAndSave(
        "Output/rtaFreq.png"
    )

sys = Ej5SystemA.getSystem(
    rl = 1,
    l = 100
)

t = np.linspace(0, 4, 100000)
t2, y = sys.impulse(t=t)
t2 *= 1000

# ExpressPlot.CombinedPlot()\
#     .addSignalPlot(
#         Senial.Senial(t2, y[0]),
#         color="blue",
#          name="Rta al impulso"
#     )\
#     .setTitle(
#         "Respuesta al impulso"
#     )\
#     .setXTitle("Tiempo (ms)")\
#     .setYTitle("Amplitud")\
#     .plotAndSave(
#         "Output/rtaImpulsoA.png"
#     )
# y = y[0]
# y *= 32767 / max(abs(y))
# y = y.astype(np.int16)
# play_obj = sa.play_buffer(y, 1, 2, fs)
#
# play_obj.wait_done()
# plt.show()

fs = 44100

sys = Ej5SystemA.getSystem(
    rl=1,
    l=50
)


T = 4

tu = np.arange(0, 0.01, 1/fs)

noise = sin(2*np.pi*44100/(50+1/2)*tu) ##np.random.normal(0, 1, 50)
times = np.linspace(0, T, fs*T)
empty = [0] * (len(times) - len(noise))
input = np.hstack([noise, empty])


t = np.linspace(0, T, T*fs)
t, y = signal.dlsim(sys, input, t=times)

t *= 1000


ExpressPlot.CombinedPlot()\
    .addSignalPlot(
        Senial.Senial(t, y),
        color="blue",
        name="Rta a ruido uniforme"
    )\
    .setTitle(
        "Respuesta a ruido uniforme longitud L=50"
    )\
    .setXTitle("Tiempo (ms)")\
    .setYTitle("Amplitud")\
    .plotAndSave(
        "Output/rtaRuidoAleatorio.png"
    )\

y *= 32767 / max(abs(y))
y = y.astype(np.int16)
play_obj = sa.play_buffer(y, 1, 2, fs)

play_obj.wait_done()
plt.show()




