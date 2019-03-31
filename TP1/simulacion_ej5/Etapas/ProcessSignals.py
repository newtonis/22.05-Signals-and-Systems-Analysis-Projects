from Etapas import SignalsReadWrite, FiltroLP, SampleAndHold, LlaveAnalogica
from Globals import PlotSignals


def processSignals(inputFile, modes, loadingModel):

    signal = SignalsReadWrite.readSignal(inputFile)

    PlotSignals.getSignalsData().setSignal("Entrada", signal)

    total = modes["FAA"].get() + \
            modes["Sample and Hold"].get() + \
            modes["Llave analógica"].get() + \
            modes["FR"].get()

    if total != 0:
        fraction = 100 / total
    else:
        fraction = 1

    print("processing")
    if modes["FAA"].get():
        signal = FiltroLP.getFiltroLP().processInput(signal, loadingModel, fraction)

        PlotSignals.getSignalsData().setSignal("FAA", signal)
        #loadingModel.update(fraction)
        print("A")

    if modes["Sample and Hold"].get():
        signal = SampleAndHold.getSampleAndHold().processInput(signal, loadingModel, fraction)

        PlotSignals.getSignalsData().setSignal("Sample and Hold", signal)
        #loadingModel.update(fraction)
        print("B")

    if modes["Llave analógica"].get():
        signal = LlaveAnalogica.getLlaveAnalogica().processInput(signal, loadingModel, fraction)

        PlotSignals.getSignalsData().setSignal("Llave analógica", signal)
        #loadingModel.update(fraction)
        print("C")

    if modes["FR"].get():
        signal = FiltroLP.getFiltroLP().processInput(signal, loadingModel, fraction)

        PlotSignals.getSignalsData().setSignal("FR", signal)
        #loadingModel.update(fraction)
        print("D")

    loadingModel.callOnFinished()
