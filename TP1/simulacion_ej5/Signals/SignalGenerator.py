from numpy import linspace
from math import sin, pi
from Etapas import SignalsReadWrite, Senial


def GenerateSine(freq):

    times = linspace(0, 2, 10000)
    values = [sin(2*pi*freq*t) for t in times]

    SignalsReadWrite.writeSignal(
        Senial.Senial(times, values),
        "Signals/Seno_"+str(freq/1000)+"k.xml"
    )
