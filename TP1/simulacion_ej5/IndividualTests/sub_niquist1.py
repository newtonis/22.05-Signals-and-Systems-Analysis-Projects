from Etapas import Senial, SignalsReadWrite, LlaveAnalogica
from ExpressPlot.ExpressPlot import CombinedPlot
import matplotlib.pyplot as plt


def subniquistTest():
    #m = 3

    s1 = SignalsReadWrite.readSignal("Signals/AM_2.4Khz.xml")
    s2 = LlaveAnalogica.getLlaveAnalogica().processInput(s1, None, 1)
    s3 = SignalsReadWrite.readSignal("Signals/AM_0.36Khz.xml")

    CombinedPlot()\
        .addSignalPlot(s1, "orange", "Señal AM 2.4Khz")\
        .addSignalPlot(s2, "blue", "Salida LLave analogica")\
        .addSignalPlot(s3, "green", "señal subniquist")\
        .plotAndSave("IndividualTests/test_niquist.png")

    plt.show()
