from Etapas import SignalsReadWrite
from Globals import PlotSignals


def processSignals(inputFile, modes):
    signal = SignalsReadWrite.readSignal(inputFile)

    PlotSignals.getSignalsData().setSignal("Entrada", signal)

