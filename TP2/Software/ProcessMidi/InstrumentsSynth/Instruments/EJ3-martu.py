import time
from numpy import *
from math import *
from scipy import signal
from scipy.io import wavfile
from numpy import zeros
from scipy.interpolate import pchip
from scipy.signal import find_peaks
from scipy.fftpack import fft, fftfreq
import operator
import numpy as np


def env(dur, f, n, file, pd):
    sampFreq, sndd = wavfile.read(file, 'rb')

    snd = sndd[:, 0]

    # espectrograma

    freq, times, sx = signal.spectrogram(snd, fs=sampFreq, window='hanning', nperseg=int(round(sampFreq / (1+f))),
                                         detrend=False, scaling='spectrum')

    # calculo envolvente para cada armónico

    s = sx[int(n), :]

    index, value = max(enumerate(s), key=operator.itemgetter(1))

    s = s / s[index]

    peaks, dk = find_peaks(s, distance=int(np.round(len(snd) / pd)))

    si = np.concatenate(([0],s[peaks],[0]))
    t = np.concatenate(([0],times[peaks], [len(snd) / sampFreq]))

    pk = pchip(t, si)
    if( dur == 0):
        return [0]


    xnew = np.arange(0, t[len(t) - 1], t[len(t) - 1] / (dur * sampFreq))

    pnew = pk(xnew)

    pnew = (abs(pnew) + pnew) / 2

    return pnew


def expEnv(adsr, k, alpha, dur, A):
    fs = 44100
    stageDurations = [adsr[0], adsr[1], dur - adsr[0] - adsr[1] - adsr[3], adsr[3]]

    attack = round(stageDurations[0] * fs)  # number of samples per stage
    decay = round(stageDurations[1] * fs)
    sustain = round(stageDurations[2] * fs)
    release = round(stageDurations[3] * fs)

    Aprima = (k) * np.exp(-7 * adsr[1]) * A - alpha * stageDurations[2]
    if (Aprima < 0):
        Aprima = 0

    a = k * (1 - np.exp(-1 * linspace(0, adsr[0], attack) / (adsr[0] / 5)))
    c = linspace((k) * np.exp(-7 * adsr[1]), Aprima, int(sustain))
    b = (k) * np.exp(-7 * (linspace(0, adsr[1], decay)))
    d = Aprima * np.exp(-15 * (linspace(0, adsr[3], release)))

    envelope = np.concatenate((a, b, c, d))

    return envelope



def ffta(file, height, distance):
    sampFreq, sndd = wavfile.read(file, 'rb')

    snd = sndd[:, 0]

    N = len(snd)

    # le aplico fft
    yf = fft(snd)
    freqs = fftfreq(snd.size) * sampFreq

    index, value = max(enumerate(abs(yf)), key=operator.itemgetter(1))  # el valor máximo corresponde a la f0

    yf = yf / yf[index]

    # detecto los picos de la fft que son los que se corresponden con los armónicos
    peaks, dk = find_peaks(abs(yf[range(N // 2)]), distance=index - distance, height=height)

    # calculo cuales son los armónicos presentes
    harmonics = np.round(freqs[peaks] / freqs[index])

    # calculo las amplitudes para cada armónico
    amps = zeros(len(harmonics))
    for i in range(0, len(harmonics)):
        amps[i] = abs(yf[peaks[i]] / yf[index])


    # calulo las fases para cada armónico
    phase = zeros(len(harmonics))  # en radianes
    for i in range(0, len(harmonics)):
        phase[i] = np.angle(yf[peaks[i]])

    return amps, harmonics, phase


def getPiano(vel, frequency, duration, fs):
    # duration no incluye el tiempo de release
    file = 'ProcessMidi\InstrumentsSynth\Instruments\piano.wav'
    totaltime = np.arange(0, duration, 1 / fs)
    height = 0.01
    distance = 1
    pd = 3000
    amps, harmonics, phase = ffta(file, height, distance)
    x = np.zeros(len(totaltime))

    for i in range(0, len(harmonics)):
        envelope = env(duration , frequency, harmonics[i], file, pd)

        x += amps[i] * np.cos(2 * pi * frequency * harmonics[i] * totaltime + phase[i]) * envelope

    return x


def getSax(vel, frequency, duration, fs):
    # duration no incluye el tiempo de release
    file = 'ProcessMidi\InstrumentsSynth\Instruments\c4mforte.wav'
    trelease = 0.25
    tattack = 0.1
    tdecay = 0.15
    tsustain = duration - tattack - tdecay
    totaltime = np.arange(0, duration, 1 / fs)


    height = 0.005
    distance = 1
    k = 1.5  # maximum amplitud k*A
    alpha = 0.06 #pendient de sustain
    pd = 5000

    if (duration < tattack):
        tattack = duration
        tdecay = 0
        tsustain = 0
        # en release para que sea continuo la amplitud debería arrancar donde termina el attack y caer a 0.

    elif (duration > tattack) and (duration < tattack + tdecay):
        tdecay = duration - tattack
        tsustain = 0
        # ver que el release arranque donde termina el decay y caiga a 0

    adsr = [tattack, tdecay, tsustain, trelease]
    amps, harmonics, phase = ffta(file, height, distance)
    x = np.zeros(len(totaltime))


    for i in range(0, len(harmonics)):
        envelope = env(duration , frequency, harmonics[i], file, pd)
        # envelope = expEnv(adsr, k, alpha, duration+trelease, amplitude)

        x += amps[i] * np.cos(2 * pi * frequency * harmonics[i] * totaltime + phase[i]) * envelope

    return x


def getViolin(vel, frequency, duration, fs):

    file = 'ProcessMidi\InstrumentsSynth\Instruments/violin.wav'
    pd = 7000
    height = 0.001
    distance = 364
    totaltime = np.arange(0, duration, 1 / fs)
    amps, harmonics, phase = ffta(file, height, distance)
    x = np.zeros(len(totaltime))

    for i in range(0, len(harmonics)):
        envelope = env(duration, frequency, harmonics[i], file, pd)
        x += amps[i] * np.cos(2 * pi * frequency * harmonics[i] * totaltime + phase[i]) * envelope

    return x

def getTrombone(vel, frequency, duration, fs):
    file = 'ProcessMidi\InstrumentsSynth\Instruments/trombone.wav'
    pd = 3000
    height = 0.03
    distance = 1
    totaltime = np.arange(0, duration , 1 / fs)
    amps, harmonics, phase = ffta(file, height, distance)
    x = np.zeros(len(totaltime))
    for i in range(0, len(harmonics)):
        envelope = env(duration, frequency, harmonics[i], file, pd)

        x += amps[i] * np.cos(2 * pi * frequency * harmonics[i] * totaltime + phase[i]) * envelope

    return x
