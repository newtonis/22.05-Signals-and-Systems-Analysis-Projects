from Etapas import Senial, SignalsReadWrite, LlaveAnalogica, SampleAndHold
from ExpressPlot.ExpressPlot import CombinedPlot
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    #print(low, high)
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def subniquistTest():
    #m = 3

    s1 = SignalsReadWrite.readSignal("Signals/AM_2.4Khz.xml")
    s2 = SampleAndHold.SampleAndHold().processInput(s1, None, 1)
    #s3 = SignalsReadWrite.readSignal("Signals/AM_0.36Khz.xml")

    fs = 2040

    lowcut = 2400-250
    highcut = 2400+250

    print(1/s1.separation)
    #print(s1.xvar[1] - s1.xvar[0])
    values = butter_bandpass_filter(s2.values, lowcut, highcut, 1/s1.separation, order=2)
    values = [v for v in values]
    s3 = Senial.Senial(s2.xvar, values)
    #print(s3.values)
    CombinedPlot() \
        .addSignalPlot(s1, "orange", "Señal AM 2.4Khz") \
        .addSignalPlot(s2, "blue", "Salida LLave analogica") \
        .addSignalPlot(s3, "green", "señal subniquist") \
        .plotAndSave("IndividualTests/test_niquist.png")

    plt.show()
