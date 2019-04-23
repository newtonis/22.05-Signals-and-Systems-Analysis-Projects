from scipy import signal


def getSystem(rl, l, fs=44100, b = 1):
    num = [0] * (l + 2)
    den = [0] * (l + 2)

    num[0] = 1 / 2 * b
    num[1] = 1 / 2 * b

    den[0] = 1
    den[-2] = -1 / 2 * rl * b
    den[-1] = -1 / 2 * rl * b

    return signal.dlti(
        num,
        den,
        dt=1/fs
    )
