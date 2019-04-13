from Etapas import FiltroLP
from numpy import logspace
from ExpressPlot import ExpressPlot
from util_python import Senial
from numpy import pi
from matplotlib import pyplot as plt
from Globals import config

def makeBodes():
    config.GetConfigData().FAAfreq = 1600

    f = logspace(2.3, 3.5, 200000)
    wrange = [fi * 2 * pi for fi in f]
    w, mag, pha = FiltroLP.getFiltroLP().getBode(wrange)
    frange = [wi / 2 / pi for wi in w]

    senialTeorica = Senial.Senial(frange, mag)

    ExpressPlot.CombinedPlot()\
        .setTitle("Respuesta en frecuencia")\
        .setXTitle("Frecuencia (Hz)")\
        .setYTitle("Amplitud (dB)")\
        .setLogarithmic()\
        .addSignalPlot(
            signal=senialTeorica,
            color="blue",
            name="Teórica"
        )\
        .addSpiceBodePlot(
            filename="ExpressInput/SimulacionV2/bode_Modulo_Sim.txt",
            color="red",
            name="Simulación",
            mode=ExpressPlot.MAG
        )\
        .addCSVQuotient(
            filename="ExpressInput/Mediciones/Filtro FAA/bode_moduloFAA.csv",
            fieldX="Frequency (Hz)",
            fieldA="Channel 1 Magnitude (dB)",
            fieldB="Channel 2 Magnitude (dB)",
            color="green",
            name="Medición FR",
        )\
        .plotAndSave(filename="ExpressOutput/bodeFiltrosCaso3.png")

    plt.show()
