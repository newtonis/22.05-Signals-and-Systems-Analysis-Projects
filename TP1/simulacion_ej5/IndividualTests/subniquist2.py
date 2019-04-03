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
        args["ax"].plot([xi, xi], [0, 0.05], color="black")


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


def subniquistMediciones():
    entrada = SignalsReadWrite.readSignalCsv(
        "ExpressInput/Mediciones basicas/med_22.csv",
        "1"
    )
    signal = SignalsReadWrite.readSignalCsv(
        "ExpressInput/Mediciones basicas/med_22.csv",
        "2"
    )
    f_entrada = FourierTransform.fourierTransform(entrada)
    f_signal = FourierTransform.fourierTransform(signal)
    fs = 1070

    ExpressPlot.CombinedPlot()\
        .setTitle("Mediciones espectro $f_s=1.07k$")\
        .setXTitle("Frecuencia (Hz)")\
        .setYTitle("Amplitud (% del total)") \
        .extraPlot(
        plotFunction,
        {"fs": fs}) \
        .addSignalPlot(
            signal=f_entrada,
            color="green",
            name="Entrada"
        )\
        .addSignalPlot(
        signal=f_signal,
        color="orange",
        name="Medicion llave analógica")\
        .plotAndSave(
            filename="ExpressOutput/espectro_subniquist1.png"
        )

    plt.show()

    entrada = SignalsReadWrite.readSignalCsv(
        "ExpressInput/Mediciones basicas/med_23.csv",
        "1"
    )
    signal = SignalsReadWrite.readSignalCsv(
        "ExpressInput/Mediciones basicas/med_23.csv",
        "2"
    )
    f_entrada = FourierTransform.fourierTransform(entrada)
    f_signal = FourierTransform.fourierTransform(signal)
    fs = 1070

    ExpressPlot.CombinedPlot() \
        .setTitle("Mediciones espectro $f_s=1.07k$") \
        .setXTitle("Frecuencia (Hz)") \
        .setYTitle("Amplitud (% del total)") \
        .extraPlot(
        plotFunction,
        {"fs": fs}) \
        .addSignalPlot(
        signal=f_entrada,
        color="green",
        name="Entrada"
    ) \
        .addSignalPlot(
        signal=f_signal,
        color="orange",
        name="Medicion sample and hold") \
        .plotAndSave(
        filename="ExpressOutput/espectro_subniquist2.png"
    )

    plt.show()

