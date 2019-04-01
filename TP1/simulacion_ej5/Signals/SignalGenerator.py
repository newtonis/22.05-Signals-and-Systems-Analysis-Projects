from numpy import linspace
from math import sin, cos, pi, ceil, exp
from Etapas import SignalsReadWrite, Senial


def GenerateSine(freq, a, b, vp):
    #print(freq)
    times = linspace(a, b, 100000)
    values = [vp*sin(2*pi*freq*t) for t in times]

    SignalsReadWrite.writeSignal(
        Senial.Senial(times, values),
        "Signals/Seno_"+str(freq/1000)+"k.xml"
    )


def GenerateCos(freq, a, b, vp):
    #print(freq)
    times = linspace(a, b, 100000)
    values = [vp*cos(2*pi*freq*t) for t in times]

    SignalsReadWrite.writeSignal(
        Senial.Senial(times, values),
        "Signals/Coseno_"+str(freq/1000)+"k_"+str(vp)+"Vp.xml"
    )


def Generate32Sine(freq, a, b, vp):
    times = linspace(a, b, 100000)
    values = [vp*Sine32(2*pi*freq*t) for t in times]

    SignalsReadWrite.writeSignal(
        Senial.Senial(times, values),
        "Signals/Sine32_" + str(freq / 1000) + "k.xml"
    )


def GenerateSquare(start, end, vp):
    times = linspace(0, 0.005, 100000)

    values = [vp*square(t, start, end) for t in times]

    SignalsReadWrite.writeSignal(
        Senial.Senial(times, values),
        "Signals/Sqaure_" + str(start / 1000) + "_" + str(end/1000) + "ms.xml"
    )


def GenerateExp(f, t0, tf, vp):
    times = linspace(t0, tf, 100000)
    values = []

    for t in times:
        t = abs(t)
        T = 1/f
        if t > T/2:
            t -= (ceil(t/T)-1)*T
            if t > T/2:
                t -= T
        values.append(vp * exp(-abs(t * (10 * f))))

    SignalsReadWrite.writeSignal(
        Senial.Senial(times, values),
        "Signals/Exp_" + str(f) + "Hz.xml"
    )


def GenerateAM(fp, fm, t0, tf, vp):
    times = linspace(t0, tf, 100000)
    values = [vp*(cos(2*pi*fp*t) + cos(2*pi*(fp-fm)*t)/2 + cos(2*pi*(fp+fm)*t)/2) for t in times]
    SignalsReadWrite.writeSignal(
        Senial.Senial(times, values),
        "Signals/AM_" + str(fp / 1000) + "kHz.xml"
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
