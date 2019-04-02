from util_python import Senial, SignalsReadWrite
from Globals import config
from ExpressPlot import ExpressPlot
from Utils import FourierTransform
import numpy as np
import matplotlib.pyplot as plt

def plotFunction(args):
    for i in np.arange(-3.5, 3.5, 1):
        xi = i * args["fs"]
        args["ax"].plot([xi, xi], [0, 0.05], color="black")



def joaco_spectrum():

    fs = 1000
    #config.GetConfigData().setFs(fs)
    #config.GetConfigData().setSampleCycle(5)

    input = SignalsReadWrite.readSignalCsv(
        "ExpressInput/Mediciones basicas/med_09.csv",
        "B"
    )

    inputSpectrum = FourierTransform.fourierTransform(input)

    ExpressPlot.CombinedPlot() \
        .setTitle("Simulación espectro $f_s=" + str(fs / 1000) + "k$") \
        .setXTitle("Frecuencia (hz)") \
        .setYTitle("Potencia (% del total)") \
        .extraPlot(
        plotFunction,
        {"fs": fs}) \
        .addSignalPlot(
        signal=inputSpectrum,
        color="green",
        name="Salida llave analógica"
    ).plotAndSave(
        filename="ExpressOutput/espectro_09"
    )
    plt.show()