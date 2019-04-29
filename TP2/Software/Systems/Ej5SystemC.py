from scipy import signal
from numpy import cos, pi, convolve
import numpy as np

def getSystem(rl, fc, fs=44100):
    l = int(fs / fc)
    a = l + 1 - fs/fc
    b = fs/fc - l

    num = [0] * (l + 2)
    den = [0] * (l + 2)

    num[0] = a
    num[1] = b

    den[0] = 1
    den[-2] = -a * rl
    den[-1] = -b * rl

    #c = 1/(2*cos(2*pi*fc/fs)+1)

    # num2 = [c, c, c]
    # num3 = convolve(num, num2)
    #
    # den2 = [2, 0, 0]
    #
    # den3 = convolve(den, den2)

    return signal.dlti(
        num,
        den,
        dt=1/fs
    )


def systemC(x, fs, fc, rl=1):
    l = int(fs / fc)
    a = l + 1 - fs / fc
    b = fs / fc - l


    y = [0] * len(x)

    for n in range(len(x)):

        if n >= l+1:
            y[n] = (x[n] + x[n-1] + y[n-l]*a*rl + y[n-l-1]*b*rl)
        else:
            x_last = x[n-1] if n >= 1 else 0
            y_last_l = y[n-l] if n >= l else 0
            y_last_l_1 = y[n-l-1] if n >= l+1 else 0

            y[n] = (x[n] + x_last + y_last_l*a*rl + y_last_l_1*b*rl)

    z = [0] * len(y)

    for n in range(len(y)):
        if n >= 1:
            z[n] = y[n] - y[n - 1] + 0.9999 * z[n - 1]
        else:
            z[n] = y[n]

    return np.array(z)


def lowPass(x, fs, fc):

    y = [0] * len(x)

    a = 1 / abs(2*cos(2*pi*fc/fs) + 1)

    for n in range(len(x)):
        x_last = x[n-1] if n >= 1 else 0
        x_last_2 = x[n-2] if n >= 2 else 0
        y[n] = a * (x[n] + x_last + x_last_2)

    return y

