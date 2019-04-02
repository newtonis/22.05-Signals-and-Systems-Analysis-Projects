import math
import cmath
import scipy.fftpack as fft
import matplotlib.pyplot as plt
import numpy


def sin32(t, T):
    t = abs(t)
    t2 = 3/2*T
    if t > t2:
        t -= (math.ceil(t / t2) - 1) * t2
    return math.sin(2*math.pi*t/T)


def exp_periodica(t):
    t = abs(t)
    if t > 5:
        t -= (math.ceil(t/10)-1)*10
        if t > 5:
            t -= 10
    return math.exp(-abs(t))


def coefFourierExp(n):
    T=10
    return 2/T * (1 - (-1)**n * math.exp(-T/2))/(1+(2*math.pi*n/T)**2)


def serieFourierExp(n, t):
    ans = coefFourierExp(0)
    T = 10
    for k in range(1, n+1):
        ans += coefFourierExp(k)*cmath.exp(1j*2*math.pi*k*t/T)
        ans += coefFourierExp(-k)*cmath.exp(-1j*2*math.pi*k*t/T)
    return ans


def an32Seno(n):
    if n == 0:
        return 2/3/math.pi
    else:
        return 12/math.pi/(9-4*n**2)


def serieFourier32Seno(n, t, T):
    ans = an32Seno(0)
    for k in range(1, n+1):
        ans += an32Seno(k)*math.cos(2*math.pi*k*t/(3/2*T))
    return ans

f0 = 500
T = 2/3/f0
n = 1000
t = numpy.arange(0, 3.1/f0, 1/1000/f0)
funcion = [sin32(tt, T) for tt in t]
potfft = fft.fft(funcion)/len(t)
potfourier = [(an32Seno(n)**2)/2 for n in range(0, n)]
potfourier[0] *= 2

for k in range(1, n):
    potfourier[k] += potfourier[k-1]

for k in range(n):
    potfourier[k] /= potfourier[n-1]

fourier3 = [serieFourier32Seno(3, tt, T) for tt in t]
plt.plot(t, funcion, t, fourier3)
#plt.bar(range(10), potfourier[0:10])
print(potfourier)

# T = 10
# n = 4999
# t = numpy.arange(0, 2.1*T, T/1000)
# funcion = [exp_periodica(tt) for tt in t]
# fourier = [serieFourierExp(n, tt) for tt in t]
# #plt.plot(t, funcion, t, fourier)
# potfft = fft.fft(funcion)/len(t)
# potfourier = [coefFourierExp(n)**2+coefFourierExp(-n)**2 for n in range(0, n)]
# potfourier[0] /= 2
# plt.bar(range(0, 20), potfourier)

plt.xlabel("Tiempo (s)")
plt.ylabel("Tensión (V)")
# plt.xlabel("Número de armónico (adimensional)")
# plt.ylabel("Potencia (W)")
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
plt.show()
