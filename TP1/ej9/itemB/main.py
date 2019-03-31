from math import pi, sin, cos
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
import matplotlib.patches as mpatches
import symbol as sp
from util_python import datacursor_easy
from numpy import exp


class seq:
    def __init__(self, seq, values):
        self.seq = seq
        self.values = values

    def setCoef(self, coef):
        print(1/len(coef))
        self.coef = coef
        print(abs(self.coef))

    def fourierEvaluarReconstruccion(self, t, fs):
        t = t - self.values[0]
        sm = 0

        for k in range(len(self.coef)//2): #len(self.coef)):
            xk = self.coef[k]
            f = k*fs/len(self.coef)

            sm += 2 * abs(xk) * cos(2 * pi * t * f + np.angle(xk)) # * exp(1j*2*pi*t*f)

        return 1/len(self.coef) * sm




def decimate(x, M): # s es la primera posicion
    y = []
    values = []

    s = x.values[0]
    e = x.values[-1] - 1
    #print(s)

    for i in range(-M, s-1, -M):
        y.append(x.seq[i-s])
        values.append(i)
        #print(s+i)

    #print(values)

    y.reverse()
    values.reverse()

    for i in range(0, e+1, M):
        y.append(x.seq[i-s])
        values.append(i)
    #print(values)

    return seq(y, values)


def plot_data():
    fig, ax1 = plt.subplots()
    #patches = []

    n_range = range(-50, 51)

    T = int(1/0.25)

    x1 = seq([sin(2*pi * n / T) for n in n_range], n_range)
    #print(x1.seq[0:T])
    x1.setCoef(fft(x1.seq[0:T]))

    y1 = decimate(x1, 4)
    y1.setCoef(fft(y1.seq[0:T//4]))


    #tx = abs(fft(x)/Nx)# rafa
    # ty = abs(fft(y)/Ny)# rafa
    #
    # ax1.plot(rx, tx, color='blue')
    # ax1.plot(ry, ty, color='red')
    #
    patches = []

    patches.append(mpatches.Patch(color="green", label="muestras"))
    patches.append(mpatches.Patch(color="blue", label="reconstruida"))



    plt.legend(handles=patches)
    #ax1.plot(x1.values, x1.seq)
    #ax1.plot(y1.values, y1.seq)

    ax1.plot(y1.values, y1.seq, 'gx')
    t_range = np.linspace(-50, 50, 10000)
    #print(t_range)
    y1_values = [y1.fourierEvaluarReconstruccion(ti, 1) for ti in t_range]

    ax1.plot(t_range, y1_values, "blue")

    plt.xlabel("n")
    plt.ylabel("x(n)")
    ax1.set_ylim([-1, 1])

    plt.minorticks_on()

    plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
    plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    plt.title("Señal 2 reconstrucción")

    plt.show()


def spectrum():
    pass



plot_data()