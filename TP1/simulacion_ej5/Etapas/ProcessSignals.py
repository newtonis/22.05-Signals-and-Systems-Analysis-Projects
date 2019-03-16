from Etapas import SignalsReadWrite, FiltroLP
from Globals import PlotSignals


def processSignals(inputFile, modes):
    signal = SignalsReadWrite.readSignal(inputFile)

    PlotSignals.getSignalsData().setSignal("Entrada", signal)

    if modes["FAA"]:
        signal = FiltroLP.getFiltroLP().processInput(signal)

        PlotSignals.getSignalsData().setSignal("FAA", signal)

