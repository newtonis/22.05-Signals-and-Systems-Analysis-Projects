from numpy import sin, exp, pi, arange, hstack
from ExpressPlot import ExpressPlot
from util_python import Senial
import matplotlib.pyplot as plt


noise_duration_factor = 5


def processInput(input):
    pass


def sigmoid(x):
    return 1 / (1 + exp(-x))


def windsigmoid(x):
    return 1 - sigmoid((x-5) * 10)


def SintetizarGuitarraEE(vel, fc, duration, fs):
    noise_duration = noise_duration_factor * (1 / fc)

    input_time = arange(0, duration + 0.5, 1/fs)

    input = sin(2*pi*fc*input_time) * windsigmoid(input_time/noise_duration)

    ExpressPlot.CombinedPlot()\
        .addSignalPlot(
            signal=Senial.Senial(
                input_time,
                input
            ),
            color="blue",
            name="entrada"
        )\
        .plot()\
        .show()

SintetizarGuitarraEE(127, 440, 4, 44100)
