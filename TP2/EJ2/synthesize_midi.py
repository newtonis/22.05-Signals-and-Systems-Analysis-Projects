import numpy as np
import mido
from mido import MidiFile

from math import *
from numpy import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio

#  donde te pasan, para cada canal una funcion de sintesis que vos en tu programa llamas
#  con dos parametros  nota y velocidad  y esas funciones te devuelven un arreglo
#  de numeros vos basicamente combinas todos los arreglos de numeros en los distintos
#  instantes donde suenan los instrumentos en un unico arreglo (o sea usando linealidad)
#  y retornas un super arreglo con toda la cancion

class noteParams:
    vel = None
    note = None
    def __init__(self,vel_=None,note_=None):
        self.vel = vel_
        self.note = note_

def synthesize_midi( midiFilename ,tracks_synthesis ,fs):
    midi_file = MidiFile(midiFilename)
    d = {}
    highest_tick = 0
    for i, track in enumerate(midi_file.tracks): #i es el nro de track
        for message in track:
            if(message.type == "note_on"):
                if not(message.time in d):
                    d[message.time]=[]
                d[message.time].append(noteParams(message.velocity, message.note))
                if(message.time>highest_tick):
                    highest_tick=message.time

# hasta aca tengo todos los ticks con velocidades y notas
#IMPORTANTE : ------------------------------------------------------------------
# cuanto es un tick en tiempos de fs?
# como definir la longitud temporal de los arreglos? (es decir la duracion)
#------------------------------------------------------------------------------

    tick_arrs={}
    ttot = np.linspace(0,1,fs)
    for channel, function in tracks_synthesis.items():
        for tick_val,tick_group in d.items():
            for index,nparam in enumerate(tick_group): #  tick_group[index] es un nparam
                vel = nparam.vel
                note = nparam.note
                if not(tick_val in tick_arrs):
                    tick_arrs[tick_val]=np.zeros(len(ttot))
                yaux=function(vel,note,fs)
                tick_arrs[tick_val]+=yaux


    # la separacion de en el arreglo final es de 1/fs

    total_time =  highest_tick*(1/fs)+len(ttot)*(1/fs)
    time_arr = arange(0, total_time, 1 / fs)
    amp_arr = zeros(len(time_arr))
    for tick,arr in tick_arrs.items():
        for i in range(len(arr)):
            amp_arr[tick+i]+=arr[i]

    return time_arr,amp_arr

def getBell(A0,fm,fs):
    tau = 0.2
    fc = 2 * fm
    deltaf = (fc - fm) / 2
    I0 = deltaf / fm
    phi_m = -pi/2
    phi_c = -pi/2
    t = np.linspace(0, 1, num=fs)
    A = zeros(len(t))
    I = zeros(len(t))
    x = zeros(len(t))
    for index,ti in enumerate(t):
      A[index]=A0*exp(-ti/tau)
      I[index]=I0*exp(-ti/tau)
      x[index]=A[index]*cos(2*pi*fc*ti+I[index]*cos(2*pi*fm*ti+phi_m)+phi_c)

    return x

track_synthesis = {"channel1":getBell}
t,ytot = synthesize_midi("mary.mid",track_synthesis,44100)

plt.plot(t,ytot)
plt.show()
