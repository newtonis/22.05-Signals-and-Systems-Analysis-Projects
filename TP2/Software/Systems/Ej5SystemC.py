from scipy import signal
from numpy import cos, pi, convolve


def getSystem(rl, fc, fs=44100):
    l = int(fs / fc)
    a = l + 1 - fs/fc
    b = fs/fc - l

    num = [0] * (l + 2)
    den = [0] * (l + 2)

    num[0] = a
    num[1] = b

    den[0] = 1
    den[-2] = -1 / 2 * rl * b
    den[-1] = -1 / 2 * rl * b

    c = 1/(2*cos(2*pi*fc/fs)+1)

    num = convolve(num, [c, c, c])
    return signal.dlti(
        num,
        den,
        dt=1/fs
    )
