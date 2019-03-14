from numpy import logspace, linspace
from math import sin, pi, log10
import matplotlib.pyplot as plt


def get_yn(alpha, beta, xn, y1, y2):
    return 0.5 * xn + alpha * y1 + beta * y2


def computar_recurrencia(x, alpha, beta):
    y = [0] * len(x)

    for n in range(len(x)):
        if n == 0:
            y[n] = get_yn(alpha, beta, x[n], 0, 0)
        elif n == 1:
            y[n] = get_yn(alpha, beta, x[n], y[n-1], 0)
        else:
            y[n] = get_yn(alpha, beta, x[n], y[n-1], y[n-2])

    return y


def get_max(arr):
    max_val = 0
    for v in arr:
        max_val = max(max_val, v)

    return max_val


alpha = 1
beta = -1/4

f_range = linspace(-1/2, 1/2, 10000)

amp_values = 10000 * [0]

n_range = range(100)

i = 0

for f in f_range:
    x = [sin(2*pi*f*n) for n in n_range]
    y = computar_recurrencia(x, alpha, beta)
    print(get_max(y))
    amplitud = 20 * log10( get_max(y) )
    amp_values[i] = amplitud

    i = i + 1

plt.plot(f_range , amp_values)
plt.show()
