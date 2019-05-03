from scipy import signal
from numpy import cos, pi, convolve
import numpy as np
from numpy import exp


def sigmoid(x):
    if x > 1:
        return 2/3
    elif x < -1:
        return -2/3
    else:
        return x - x**3/3

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


    return np.array(input)


def systemD(x, fs, fc, rl=1):
    l = int(fs / fc)
    a = l + 1 - fs / fc
    b = fs / fc - l


    y = [0] * len(x)
    #inv = -1
    #print("rl = ", rl)

    x = normalize(x)
    #print(x)

    for n in range(len(x)):

        if n >= l+1:
            y[n] = x[n] + x[n-1] + y[n-l]*a*rl + y[n-l-1]*b*rl
        else:
            x_last = x[n-1] if n >= 1 else 0
            y_last_l = y[n-l] if n >= l else 0
            y_last_l_1 = y[n-l-1] if n >= l+1 else 0

            y[n] = x[n] + x_last + y_last_l*a*rl + y_last_l_1*b*rl

        y[n] = sigmoid(y[n])
    z = [0] * len(y)

    for n in range(len(y)):
        if n >= 1:
            z[n] = y[n] - y[n-1] + 0.9999 * z[n-1]
        else:
            z[n] = y[n]

    return np.array(z)

