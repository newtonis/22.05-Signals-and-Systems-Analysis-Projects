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

    y = Ej5SystemE.systemE(
        x=input,
        fs=fs,
        l = 1000,
        pb=pb
    )

    #y = normalize(y)
    y -= np.mean(y)
    max_y = max(abs(np.amax(y)), abs(np.amin(y)))
    y /= max_y

    y_simple = simplify(y)

    window = sigmoidToEnd(input_time, duration)

    y = y_simple * window

    y -= np.mean(y)
    max_y = max(abs(np.amax(y)), abs(np.amin(y)))
    y /= max_y

    return y * (vel / 127)
    #return y

