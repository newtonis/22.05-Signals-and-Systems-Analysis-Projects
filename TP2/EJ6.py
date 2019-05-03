import numpy as np
from math import *
from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
import soundfile as sf

def getGamma(eta, Lgamma):
    gamma = np.zeros(Lgamma)
    gamma[0]=1
    for n in range(1, Lgamma): #va de 0 a Lgamma-1 en vez de 1 a Lgamma
        gamma[n] = gamma[n-1]+eta
    return gamma


def tsf (n, gamma, Lgamma,Lw, Lx):
    istart = 0 
    ostart = 0
    iend = floor(gamma[Lgamma-1]+Lw/2)
    
    Yn =  (n*Lx)/iend #mapeo
    return Yn

    
def getSigma(Lgamma, gamma, Lw, Lx):
    sigma = np.zeros(Lgamma)
    for n in range(0, Lgamma):
        sigma[n] = tsf(gamma[n], gamma, Lgamma, Lw, Lx ) #tsf es la time stretch function, es monótona creciente
   
    return sigma

def mult(x , w):
    Loutput = min (x.size, w.size)
    output = np.zeros(Loutput)
    
    for i in range (0, Loutput):
        output[i] = x[i] * w[i]
    return output
    

def sampleSynthesis(duration, x, sampFreq):
        
    Lx = len(x)
    
    plt.plot(np.arange(len(x)) / sampFreq, x)
    plt.show()

    Ly = int(duration*sampFreq)
    y = np.zeros(Ly) #señal de salida
    ov = 0.5 #ov es el porcentaje de overlapping
    Lw = int(sampFreq/20) #20Hz es la menor frecuencia audible, tiene que entrar como mínimo un periodo de la señal
    window = np.hanning(Lw)
    eta = (1-ov)*Lw #distance between adyacent windows
    Lgamma = ceil(Ly/eta)
    gamma = getGamma(eta, Lgamma) #vector de window positions in output
    sigma = getSigma(Lgamma, gamma, Lw, Lx) #vector of input window positions
    
    low = ceil((Lw-1) / 2)
    high = ceil(Lw / 2)
    
    for n in range(1, Lgamma-1):
        
        slotinput = mult(window , x [int( sigma[n]) - low  : int( sigma[n]) + high ])
        if(len(slotinput)!= Lw):
                slotinput=np.concatenate((slotinput, np.zeros(int(Lw-len(slotinput))))) 

        y[int(gamma[n]) - low : int(gamma[n]) + high] =  y[int(gamma[n]) - low : int(gamma[n]) + high] + slotinput
       
    
    return  y

        
sampFreq=44100 #frecuencia de sampleo
duration = 0.5
sampFreq, xx = wavfile.read('MBNT.wav')
x = xx[:,0]  #x es la señal de audio de entrad

y = sampleSynthesis(duration, x, sampFreq)

y = y/np.amax(y)

t = np.arange(0, duration, 1 / sampFreq)

plt.plot(t, y)
plt.show()
sf.write('test.wav', y, sampFreq)
