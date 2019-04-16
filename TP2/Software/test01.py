from util_python import Senial
from ExpressPlot import ExpressPlot
import matplotlib.pyplot as plt

s1 = Senial.Senial().loadFromCSV(
    filename="Signals/cos_f_440.csv"
)

ExpressPlot.CombinedPlot()\
    .addSignalPlot(signal=s1, color="blue", name="cos 440hz")\
    .setXTitle("tiempo")\
    .setYTitle("valor")\
    .plotAndSave("Output/test_cos_f_440.png")

plt.show()
