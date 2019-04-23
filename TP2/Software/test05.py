from Systems import Ej5SystemB, Ej5SystemA
from ExpressPlot import ExpressPlot
import matplotlib.pyplot as plt
from util_python import Senial
from util_python import PlaySound
from Utils import FourierTransform
import numpy as np



fs = 44100

l = 10

t = np.arange(0, 10, 1/fs)
rl = 1

delta = [fs]
empty = (len(t)-1) * [0]

input = np.hstack([delta, empty])

#print(len(input))

plot = ExpressPlot.CombinedPlot()

b = [1]
c = ["b", "g", "r"]
caso = ["b = 1", "b = 0.5", "b = 0"]
for i in range(len(b)):
    w, H = Ej5SystemA.getSystem(1, l).freqresp()
    w = w / 2 / np.pi * fs / 1000

    #y = Ej5SystemB.processSystemB(input, 1, l, b[i])

    #ft = FourierTransform.fourierTransform(Senial.Senial(t, y))

    plot.addSignalPlot(
        Senial.Senial(w[1:], abs(H[1:])),
        color=c[i],
        name="Respuesta en frecuencia caso "+str(caso[i])
    )


plot.setXTitle("Frecuencia (Khz)")\
    .setTitle(
        "Respuesta en frecuencia"
    ).setYTitle("Amplitud")\
    .plotAndSave(
        "Output/caso2rtaFreq.png"
    )

plt.show()
