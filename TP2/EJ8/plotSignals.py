from ExpressPlot.ExpressPlot import CombinedPlot
from util_python import Senial

from numpy import arange

fs = 44100


def plotSignals():
    x_file = open("output/x.txt").readlines()
    y_file = open("output/y.txt").readlines()

    x = [float(xi) for xi in x_file]
    y = [float(yi) for yi in y_file]

    t = [i/fs for i in range(len(x_file))]

    CombinedPlot()\
        .setXTitle("Tiempo (s)")\
        .setYTitle("Amplitud")\
        .setTitle("Efectos")\
        .addSignalPlot(
            signal=Senial.Senial(t, x),
            color="blue",
            name="Entrada"
        )\
        .addSignalPlot(
            signal=Senial.Senial(t, y),
            color="red",
            name="Salida"
        ).plot().show()


plotSignals()


