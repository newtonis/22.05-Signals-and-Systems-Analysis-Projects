from util_python import Senial
from Utils import FourierTransform
from ExpressPlot import ExpressPlot
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange, linspace

def joaco_spectrum2():
    fmuestra = 30000
    dmuestra = 1 / fmuestra

    xvar = arange(0, 2, dmuestra)
    print(xvar)
   # print(len(xvar))

    periodSegundos = 0.2

    period = periodSegundos / dmuestra

    fc = 1000
    fm = 200

    yvar = np.zeros(len(xvar))
    for i in range(len(yvar)):
        if i % period <= period*0.25:
            yvar[i]=1 #*np.sin(2*np.pi*fc)*np.sin(2*np.pi*fm)
        else:
            yvar[i]=0

    s1 = Senial.Senial(xvar, yvar)
    s1f = FourierTransform.fourierTransform(s1)

    xaux = s1f.xvar
    tau = period * 0.25
    print(1/periodSegundos)
    yaux = [abs(np.sinc(it * 0.25)) for it in xaux]
    lxvar = len(s1f.xvar)/2
    lxvar2 = len(xaux)/2
    ExpressPlot.CombinedPlot()\
        .setTitle("Espectro")\
        .setXTitle("Frecuencia (Hz)")\
        .setYTitle("Ampltiud (%)")\
        .addSignalPlot(
        signal=Senial.Senial(s1f.xvar, s1f.values), color="blue",name="espectro1")\
        .addSignalPlot(
            signal=Senial.Senial(xaux, yaux),
            color="orange",
            name="sinc"
        )\
        .plotAndSave("testjoaco.png")

   # plt.plot(xaux,yaux,color="orange")
    plt.show()