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
from Utils.func_utils import *

noise_duration_factor = 0.5



def SintetizarGuitarra(vel, fc, duration, fs):
    noise_duration = noise_duration_factor * (1 / fc)

    input_time = arange(0, duration + 0.5, 1/fs)

    input = np.random.normal(0, 0.1, len(input_time)) * windsigmoid(input_time/noise_duration) # *  #sin(2*pi*fc*input_time) * windsigmoid(input_time/noise_duration)

    input = normalize(input)

    y = Ej5SystemC.systemC(
        x=input,
        fs=fs,
        fc=fc,
        rl=1
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
