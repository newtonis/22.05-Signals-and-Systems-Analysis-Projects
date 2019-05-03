from numpy import sin, exp, pi, arange, hstack
from ExpressPlot import ExpressPlot
from util_python import Senial
from scipy import signal
import matplotlib.pyplot as plt
from Systems import Ej5SystemC, Ej5SystemD
import numpy as np
from util_python import PlaySound
from numpy import sqrt
from Utils.notas import notas

noise_duration_factor = 0.5


def processInput(input):
    pass


def sigmoid(x):
    return 1 / (1 + exp(-x))


def windsigmoid(x):
    return 1 - sigmoid((x-5)*10)


def sigmoidToEnd(x, end):
    return 1 - sigmoid( (x-end)*50 )


def normalize(input):
    maxval = 0

    for vi in input:
        maxval = max(maxval , abs(vi))

    for i in range(len(input)):
        input[i] /= maxval

    suma = 0
    for vi in input:
        suma += vi
    suma /= len(input)
    for i in range(len(input)):
        input[i] -= suma


    return input


def SitetizarGuitarraDistorsion(vel, fc, duration, fs, distorsion=1.05):
    noise_duration = noise_duration_factor * (1 / fc)

    input_time = arange(0, duration , 1/fs)

    input = (np.random.normal(0, 1, len(input_time)) * sin(2*pi*fc*input_time)) * windsigmoid(input_time/noise_duration)

    input = normalize(input)

    input = Ej5SystemC.lowPass(
        input,
        fs=fs,
        fc=fc
    )
    # sys = Ej5SystemC.getSystem(
    #     rl=1,
    #     fc=fc,
    #     fs=fs
    # )
    y = Ej5SystemD.systemD(
        x=input,
        fs=fs,
        fc=fc,
        rl=distorsion
    )

    y = Ej5SystemC.lowPass(
        x=y,
        fs=fs,
        fc=fc
    )

    #y = normalize(y)
    y -= np.mean(y)
    max_y = max(abs(np.amax(y)), abs(np.amin(y)))
    y /= max_y


    y_simple = []
    for yi in y:
       y_simple.append(float(yi))
    y_simple = np.array(y_simple)

    window = sigmoidToEnd(input_time, duration)

    y = y_simple * window

    #y = normalize(y)
    y -= np.mean(y)
    max_y = max(abs(np.amax(y)), abs(np.amin(y)))
    y /= max_y

    return y * (vel / 127)
    #return y
