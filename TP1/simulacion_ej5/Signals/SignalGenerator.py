from numpy import linspace
from math import sin, pi
from Etapas import SignalsReadWrite, Senial


def GenerateSine(freq):
    #print(freq)
    times = linspace(0, 0.001, 100000)
    values = [sin(2*pi*freq*t) for t in times]

    SignalsReadWrite.writeSignal(
        Senial.Senial(times, values),
        "Signals/Seno_"+str(freq/1000)+"k.xml"
    )


def GenerateSquare(start, end):
    times = linspace(0, 0.005, 100000)

    values = [square(t, start, end) for t in times]

    SignalsReadWrite.writeSignal(
        Senial.Senial(times, values),
        "Signals/Sqaure_" + str(start / 1000) + "_" + str(end/1000) + "ms.xml"
    )


def square(t, start, end):
    if t < start:
        return 0
    elif t < end:
        return 1
    else:
        return 0
