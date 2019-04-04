from Etapas.SignalsReadWrite import readSignal
from Signals import SignalGenerator
from numpy import linspace, ceil, exp
from matplotlib import pyplot as plt

#signal = readSignal("Signals/sine.xml")

#print(signal.xvar, signal.values)

#SignalGenerator.GenerateSine(20000/12.0, 0, 0.005)
#SignalGenerator.GenerateCos(20000*12.0, 0, 0.005)

k = 1e3
f0 = 500
fexp = 10
fp = 1.5e3

SignalGenerator.GenerateCos(f0, 0, 100/f0, 2)
SignalGenerator.GenerateCos(2*f0, 0, 200/f0, 2)
# SignalGenerator.GenerateCos(f0, 0, 10/f0, 3)
#
# SignalGenerator.GenerateCos(f0, 0, 10/f0, 1)
# SignalGenerator.GenerateCos(1e3, 0, 30*10/1e3, 1)
# SignalGenerator.GenerateCos(100, 0, 10/100, 1)
#
# SignalGenerator.GenerateExp(fexp, 0, 10/fexp, 2)
#
# SignalGenerator.Generate32Sine(500, 0, 10/500, 1)
# SignalGenerator.Generate32Sine(100, 0, 10/100, 1)
#
# SignalGenerator.GenerateAM(2*f0, 0.2*f0, 0, 10/(0.2*f0), 1/2)
# SignalGenerator.GenerateAM(2*0.8*fp, 2*0.08*f0, 0, 10/(2*0.08*fp), 1/2)

# SignalGenerator.GenerateAM(2400, 240, 0, 10/(2*0.08*fp), 1/2)
# SignalGenerator.GenerateAM(360, 240, 0, 10/(2*0.08*fp), 1/2)
#SignalGenerator.GenerateAM(240, 0, 0, 10/(2*0.08*fp), 1/2)

#SignalGenerator.GenerateSquare(0.001, 0.002)

