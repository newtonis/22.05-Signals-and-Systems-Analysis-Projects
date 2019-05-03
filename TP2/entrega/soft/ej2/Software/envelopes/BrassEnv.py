from numpy import *
import matplotlib.pyplot as plt


def brassToneEnv(duration, fs):
    att = (1 / 6) * duration
    decay = (1 / 3 - 1 / 6) * duration
    sus = (1 - (1 / 6 + 1 / 3)) * duration
    rel = (1 / 6) * duration

    t = arange(0, duration, 1 / fs)
    y = zeros(len(t))
    for i, ti in enumerate(t):
        if 0 <= ti and ti <= att:
            y[i] = ti / att
        if att < ti and ti <= att + decay:
            # quiero que en att+decay valga 0.75
            y[i] = 1 - (1 - 0.75) * ((ti - att) / decay)
        if att + decay < ti and ti <= att + decay + sus:
            # quiero que en att+decay+sus sea 0.6
            y[i] = 0.75 - (0.75 - 0.6) * ((ti - (att + decay)) / sus)
        if att + decay + sus < ti:
            y[i] = 0.6 - 0.6 * ((ti - (att + decay + sus)) / (rel))

    return y
