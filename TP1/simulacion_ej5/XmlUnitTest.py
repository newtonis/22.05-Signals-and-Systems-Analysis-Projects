from Etapas.SignalsReadWrite import readSignal
from Signals import SignalGenerator

signal = readSignal("Signals/sine.xml")

print(signal.time, signal.values)

SignalGenerator.GenerateSine(10000)
