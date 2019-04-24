from numpy import sin, exp, pi, arange, hstack
import matplotlib.pyplot as plt


noise_duration_factor = 5


def sigmoid(x):
    return 1 / (1 + exp(-x))


def SintetizarGuitarraEE(vel, fc, duration, fs):
    noise_duration = int(noise_duration_factor / fc / fs)

    input_time = arange(0, duration + 0.5, fs)

    input_noise = sin(2*pi*fc*input_time[0:noise_duration])

    input_empty = 0 * input_time[noise_duration:]

    input = hstack([input_noise, input_empty])


