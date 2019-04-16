from scipy import signal


def getSystem(rl, l, fs=44100):
    num = [0] * (l + 2)
    den = [0] * (l + 2)

    num[0] = 1 / 2
    num[1] = 1 / 2

    den[0] = 1
    den[-2] = -1 / 2 * rl
    den[-1] = -1 / 2 * rl

    return signal.dlti(
        num,
        den,
        dt=1/fs
    )
