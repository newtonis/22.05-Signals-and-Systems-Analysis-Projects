import math
import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy


def coefFourierExp(n):
    T=10
    return 2/T * (1 - (-1)**n * math.exp(-T/2))/(1+(2*math.pi*n/T)**2)


def coefFourier32Seno(n):
    return (math.exp(-3*math.pi*n)+1)/(2*math.pi*n**2 + 2*math.pi)


def funcion(t):
    t = abs(t)
    if t > 5:
        t = t - (math.ceil(t/5)-1)*5
    return math.exp(-t)


# samples = 1000 # tiene que ser multiplo de 10!!
# x = [funcion(t/samples*10) for t in range(-samples//2, samples//2)]
# p1 = abs(fft.fft(x))/10
# p1 = p1/samples
# p2 = [potencia(n) for n in range(p1.size)]
#
# print(p1)
# print(p2)

n = 100
acumpot = [coefFourier32Seno(n)**2 for n in range(n)]
for i in range(1, n):
    acumpot[i] = acumpot[i-1]+acumpot[i]

for i in range(1, n):
    acumpot[i] = acumpot[i]/acumpot[n-1]

print(acumpot[0:2])
plt.plot(range(0, 2), acumpot[0:2])
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
plt.show()