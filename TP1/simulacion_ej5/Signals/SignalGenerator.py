from numpy import linspace
from math import sin, cos, pi
from Etapas import SignalsReadWrite, Senial


def GenerateSine(freq, a, b):
    #print(freq)
    times = linspace(a, b, 100000)
    values = [sin(2*pi*freq*t) for t in times]

    SignalsReadWrite.writeSignal(
        Senial.Senial(times, values),
        "Signals/Seno_"+str(freq/1000)+"k.xml"
    )


def GenerateCos(freq, a, b):
    #print(freq)
    times = linspace(a, b, 100000)
    values = [cos(2*pi*freq*t) for t in times]

    SignalsReadWrite.writeSignal(
        Senial.Senial(times, values),
        "Signals/Coseno_"+str(freq/1000)+"k.xml"
    )


def Generate32Sine(freq, a, b):
    times = linspace(a, b, 100000)
    values = [Sine32(2*pi*freq*t) for t in times]

    SignalsReadWrite.writeSignal(
        Senial.Senial(times, values),
        "Signals/Sine32_" + str(freq / 1000) + "k.xml"
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


def Sine32(t):
    dec = t / 3 / pi

    dec = int(dec)
    dec = dec % 2
    if dec == 0:
        return sin(t)
    else:
        return -sin(t)
