from util_python import Senial, SignalsReadWrite
from Utils import FourierTransform
from Etapas import LlaveAnalogica, SampleAndHold
from ExpressPlot import ExpressPlot
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


from Globals import config


def plotFunction(args):
    for i in np.arange(-3.5, 3.5, 1):
        xi = i * args["fs"]
        args["ax"].plot([xi, xi], [0, 0.2], color="black")


def SubniquistSpectrum(input, fs, filename):
    config.GetConfigData().setFs(fs)
    config.GetConfigData().setSampleCycle(5)

    inputSpectrum = FourierTransform.fourierTransform(input)

    output = SampleAndHold.getSampleAndHold().processInput(
        input,
        None,
        1
    )

    outputSpectrum = FourierTransform.fourierTransform(output)

    ExpressPlot.CombinedPlot()\
        .setTitle("Simulación espectro $f_s="+str(fs/1000)+"k$")\
        .setXTitle("Frecuencia (hz)")\
        .setYTitle("Potencia (% del total)") \
        .extraPlot(
         plotFunction,
         {"fs": fs}) \
        .addSignalPlot(
            signal=inputSpectrum,
            color="green",
            name="Entrada"
        )\
        .addSignalPlot(
            signal=outputSpectrum,
            color="orange",
            name="Salida sample and hold"
        ).plotAndSave(
            filename="ExpressOutput/"+filename
        )


def subniquistTest2():
    input = SignalsReadWrite.readSignal("Signals/AM_2.4kHz.xml")

    tot = [
        [3480, 1],
        [1940, 2],
        [1380, 3],
        [1068, 4]
    ]
    for i in tot:
        SubniquistSpectrum(
            input,
            i[0],
            "simulacionSH_N"+str(i[1])+".png"
        )

    plt.show()



