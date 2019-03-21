from Etapas.SignalsReadWrite import readSignal
from Signals import SignalGenerator

#signal = readSignal("Signals/sine.xml")

#print(signal.xvar, signal.values)

#SignalGenerator.GenerateSine(20000/12.0, 0, 0.005)
#SignalGenerator.GenerateCos(20000*12.0, 0, 0.005)

k = 1e3

SignalGenerator.GenerateCos(500, 0, 0.05)
SignalGenerator.Generate32Sine(500, 0, 0.05)


#SignalGenerator.GenerateSquare(0.001, 0.002)

