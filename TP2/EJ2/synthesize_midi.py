from mido import MidiFile
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

#importo las funciones de los intrumentos
from instruments_synth.campana import getBell
from instruments_synth.clarinete import getClarinet

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

    # voy a guardar en d todos los ticks con las distintas velocidades y notas

    for i, track in enumerate(midi_file.tracks): #i es el nro de track
        for message in track:
            if(message.type == "note_on"):
                if not(message.time in d):
                    d[message.time]=[]
                d[message.time].append(noteParams(message.velocity, message.note))
                if(message.time>highest_tick):
                    highest_tick=message.time


    #aca voy a sumar todos los arreglos que corresponden al mismo tick

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


    #finalmente acá sumo todo segun su posicion en tiempo correspondiente
    # (la separacion de en el arreglo final es de 1/fs)

    total_time =  highest_tick*(1/fs)+len(ttot)*(1/fs)
    time_arr = arange(0, total_time, 1 / fs)
    amp_arr = zeros(len(time_arr))
    for tick,arr in tick_arrs.items():
        for i in range(len(arr)):
            amp_arr[tick+i]+=arr[i]

    return time_arr,amp_arr

fs = 44100
track_synthesis = {"channel1":getClarinet}
t,ytot = synthesize_midi("mary.mid",track_synthesis,fs)
plt.plot(t,ytot)
plt.show()
