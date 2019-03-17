from Etapas import SignalsReadWrite, FiltroLP, SampleAndHold, LlaveAnalogica
from Globals import PlotSignals


def processSignals(inputFile, modes):
    signal = SignalsReadWrite.readSignal(inputFile)

    PlotSignals.getSignalsData().setSignal("Entrada", signal)

    if modes["FAA"].get():
        signal = FiltroLP.getFiltroLP().processInput(signal)

        PlotSignals.getSignalsData().setSignal("FAA", signal)

    if modes["Sample and Hold"].get():
        signal = SampleAndHold.getSampleAndHold().processInput(signal)

        PlotSignals.getSignalsData().setSignal("Sample and Hold", signal)

    if modes["Llave analógica"].get():
        signal = LlaveAnalogica.getLlaveAnalogica().processInput(signal)

        PlotSignals.getSignalsData().setSignal("Llave analógica", signal)

    if modes["FR"].get():
        signal = FiltroLP.getFiltroLP().processInput(signal)

        PlotSignals.getSignalsData().setSignal("FR", signal)
