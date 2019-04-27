from numpy import sin, exp, pi, arange, hstack
from ExpressPlot import ExpressPlot
from util_python import Senial
from scipy import signal
import matplotlib.pyplot as plt
from Systems import Ej5SystemC
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


def SintetizarGuitarra(vel, fc, duration, fs):
    noise_duration = noise_duration_factor * (1 / fc)

    input_time = arange(0, duration + 0.5, 1/fs)

    input = np.random.normal(0, 0.1, len(input_time)) * windsigmoid(input_time/noise_duration) # *  #sin(2*pi*fc*input_time) * windsigmoid(input_time/noise_duration)

    input = normalize(input)

    # sys = Ej5SystemC.getSystem(
    #     rl=1,
    #     fc=fc,
    #     fs=fs
    # )
    y = Ej5SystemC.systemC(
        x=input,
        fs=fs,
        fc=fc,
        rl=1
    )

    y = normalize(y)
    y_simple = []
    for yi in y:
       y_simple.append(float(yi))
    y_simple = np.array(y_simple)

    window = sigmoidToEnd(input_time, duration)

    y = y_simple * window

    # ExpressPlot.CombinedPlot() \
    #         .addSignalPlot(
    #             signal=Senial.Senial(
    #                 input_time,
    #                 input
    #             ),
    #             color="blue",
    #             name="Entrada"
    #     ) \
    #     .addSignalPlot(
    #         signal=Senial.Senial(
    #             input_time,
    #             y
    #         ),
    #         color="red",
    #         name="Salida"
    #     ) \
    #     .addSignalPlot(
    #     signal=Senial.Senial(
    #         input_time,
    #         window
    #     ),
    #     color="green",
    #     name="Ventana"
    #     ) \
    #     .plot() \
    #     .show()
    return y * (vel/127)
    #print(len(y))
    #print(y[0])
    #y_simple = []
    #for yi in y:
    #    y_simple.append(float(yi))
    #y_simple = np.array(y_simple)

    # plt.specgram(y_simple, Fs=fs, NFFT=4096, noverlap=3500, cmap='Reds')
    #
    # f, t, Sxx = signal.spectrogram(y_simple, fs)
    # plt.pcolormesh(t, f, Sxx)
    # plt.ylabel('Frequency [Hz]')
    # plt.xlabel('Time [sec]')
    # plt.show()

fs = 44100

y = [0] * 12

total_sound = [0] * 44100 * 13
duration = 0.5


nota = [
    "A",
    "A#",
    "B",
    "A#",
    "B",
    "A#",
    "C"
]
for i in range(len(nota)):
    print(notas[nota[i]])
    freq = notas[nota[i]][0]

    y = SintetizarGuitarra(vel= 127, fc=freq, fs= fs, duration=duration)

    for j in range(len(y)):
        total_sound[int(j+duration*fs*i)] += y[j]

total_sound = np.array(total_sound)

PlaySound.playSound(total_sound, 44100)


