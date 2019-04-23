from Systems import Ej5SystemB
from ExpressPlot import ExpressPlot
import matplotlib.pyplot as plt
from util_python import Senial

import numpy as np

fs = 44100

l = 50

t = np.arange(0, 1, 1/fs)
noise = 2 * np.random.random_sample(l) - 1
empty = [0] * (len(t) - len(noise))
input = np.hstack([noise, empty])

rl = 1

y = Ej5SystemB.processSystemB(input, rl, l)

t *= 1000

ExpressPlot.CombinedPlot()\
    .addSignalPlot(
        Senial.Senial(t, y),
        color="blue",
        name="Rta a ruido gaussiano"
    )\
    .setTitle(
        "Respuesta a ruido uniforme longitud L=50"
    )\
    .setXTitle("Tiempo (ms)")\
    .setYTitle("Amplitud")\
    .plotAndSave(
        "Output/rtaRuidoGauss2.png"
    )\

plt.show()