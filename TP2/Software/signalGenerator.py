from math import cos, pi
import numpy as np
from util_python import Senial

# 0.0022
# 0.00002 ok

f = 440
xvar = np.linspace(0, 2, 100000)
yvar = [cos(2*pi*f*x) for x in xvar]

Senial.Senial(xvar, yvar).writeCSV(
    "Signals/cos_f_440.csv"
)

#s2 = Senial.Senial().loadFromCSV(
#    "Signals/cos_f_440.csv"
#)

