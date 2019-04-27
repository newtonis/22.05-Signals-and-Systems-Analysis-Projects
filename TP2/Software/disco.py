from numpy import sin, exp, pi, arange, hstack, linspace
from ExpressPlot import ExpressPlot
from util_python import Senial
from scipy import signal
import matplotlib.pyplot as plt
from Systems import Ej5SystemC, Ej5SystemD, Ej5SystemE
import numpy as np
from util_python import PlaySound
from numpy import sqrt
from Utils.notas import notas
from Utils.func_utils import *
from Utils import notas

noise_duration_factor = 2


def casis(x):
    return np.array([1 if xi < 1 else 0 for xi in x])


def SitetizarTambor(vel, fc, duration, fs, pb=1):
    noise_duration = noise_duration_factor * (1 / fc)

    input_time = arange(0, duration , 1/fs)

    input = (np.random.normal(0, 1, len(input_time))) * casis(input_time/noise_duration)

    input = normalize(input)

    # input = Ej5SystemC.lowPass(
    #     input,
    #     fs=fs,
    #     fc=fc
    # )
    # sys = Ej5SystemC.getSystem(
    #     rl=1,
    #     fc=fc,
    #     fs=fs
    # )
    y = Ej5SystemE.systemE(
        x=input,
        fs=fs,
        l = 1000,
        pb=pb
    )

    # y = Ej5SystemC.lowPass(
    #     x=y,
    #     fs=fs,
    #     fc=fc
    # )

    y = normalize(y)
    y_simple = simplify(y)

    window = sigmoidToEnd(input_time, duration)

    y = y_simple * window

    #print(len(y))
    #print(y[0])
    # y_simple = []
    # for yi in y:
    #    y_simple.append(float(yi))
    # y_simple = np.array(y_simple)
    #
    # plt.specgram(y_simple, Fs=fs)
    #
    # f, t, Sxx = signal.spectrogram(y_simple, fs)
    # plt.pcolormesh(t, f, Sxx)
    # plt.ylabel('Frequency [Hz]')
    # plt.xlabel('Time [sec]')
    # plt.show()

    # ExpressPlot.CombinedPlot() \
    #     .setTitle("Ejemplo percusión b=" + str(pb)) \
    #     .addSignalPlot(
    #     signal=Senial.Senial(
    #         input_time,
    #         y
    #     ),
    #     color="red",
    #     name="Salida"
    # ) \
    #     .addSignalPlot(
    #     signal=Senial.Senial(
    #         input_time,
    #         input
    #     ),
    #     color="green",
    #     name="Entrada"
    # ) \
    #     .plot() \
    #     .show()
    f, t, Sxx = signal.spectrogram(y, fs)
    plt.title("Espectograma percusión")
    plt.pcolormesh(t, f, Sxx)
    plt.ylabel('Frequency [Hz]')


    return y * (vel / 127)


fs = 44100

for pb in [0.5]:
    #print("pb = ", pb)
    y = SitetizarTambor(
        vel=127,
        fc=100,
        fs=fs,
        duration=0.5,
        pb=pb
    )

    y_simple = simplify(y)

    input_time = np.arange(0, 3.5, 1/fs)
    window = sigmoidToEnd(input_time, 3)
    window = simplify(window)
    input_time = simplify(input_time)

    #print(window, input_time)

    #print(len(window))

    PlaySound.playSound(y)
