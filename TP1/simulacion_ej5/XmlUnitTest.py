from Etapas.SignalsReadWrite import readSignal
from Signals import SignalGenerator

signal = readSignal("Signals/sine.xml")

print(signal.xvar, signal.values)

SignalGenerator.GenerateSine(5000)
SignalGenerator.GenerateSquare(0.001, 0.002)

