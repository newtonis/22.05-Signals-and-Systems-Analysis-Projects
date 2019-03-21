from Etapas import Senial
from Globals import config

class SyncSignals:
    syncSignals = None

    def __init__(self):
        pass

    def getSyncSignal(self, samplePeriod, period, toff, length):
        senial = Senial.Senial([], [])

        integerPeriod = period * samplePeriod
        integerToff = integerPeriod * toff
        for ti in range(len(length)):
            cycle = ti % integerPeriod
            senial.addSample(samplePeriod * ti, cycle >= integerToff)

        return senial


def SyncSignals():
    if not SyncSignals.syncSignals:
        SyncSignals.syncSignals = SyncSignals()
    return SyncSignals.syncSignals


def getSyncSignal(inputSignal):
    samplePeriod = inputSignal.separation
    length = len(inputSignal.xvar)

    return SyncSignals().getSyncSignal(
        samplePeriod,
        config.SHfreq,
        config.SHhold,
        length
    )
