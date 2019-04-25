from util_python import Senial
from Systems import Ej5SystemC
from ExpressPlot import ExpressPlot
from numpy import pi

fs = 44100

sys = Ej5SystemC.getSystem(
    rl=1,
    fc=250,
    fs=fs
)

w, H = sys.freqresp()

w = w / 2 / pi * fs

ExpressPlot.CombinedPlot()\
    .setXTitle("Frecuencia (Hz)")\
    .setYTitle("Amplitud (veces)")\
    .addSignalPlot(
        signal=Senial.Senial(w, abs(H)),
        color="blue",
        name="Amplitud"
    )\
    .plot()\
    .show()

