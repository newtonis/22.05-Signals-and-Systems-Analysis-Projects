from ExpressPlot.ExpressPlot import CombinedPlot
from util_python import Senial

from numpy import arange
import matplotlib.pylab as plt

fs = 44100


def plotSignals():
    x_file = open("output/x.txt").readlines()
    y_file = open("output/y.txt").readlines()

    x = [float(xi) for xi in x_file]
    y = [float(yi) for yi in y_file]

    t = [i/fs for i in range(len(x_file))]

    # CombinedPlot()\
    #     .setXTitle("Tiempo (s)")\
    #     .setYTitle("Amplitud")\
    #     .setTitle("Efectos")\
    #     .addSignalPlot(
    #         signal=Senial.Senial(t, x),
    #         color="blue",
    #         name="Entrada"
    #     )\
    #     .addSignalPlot(
    #         signal=Senial.Senial(t, y),
    #         color="red",
    #         name="Salida"
    #     ).plot().show()

    fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)

    ax1.set_title("Entrada")

    ax1.set_ylabel("Amplitud")

    ax2.set_title("Salida")
    ax2.set_xlabel("Tiempo (s)")

    #axarr[0].title = "Entrada"
    ax1.plot(t, x, color="blue")

    #axarr[1].title("Salida")
    ax2.plot(t, y, color="red")

    for ax in [ax1,ax2]:
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth=0.3, color='black')
        ax.grid(axis="both", which='minor', linestyle=':', linewidth=0.1, color='black')
        ax.tick_params(axis='both', which='minor', bottom=False)

    plt.show()

plotSignals()


