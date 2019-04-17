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
    for i, track in enumerate(midi_file.tracks): #i es el nro de track
        for message in track:
            if(message.type == "note_on"):
                if not(message.time in d):
                    d[message.time]=[]
                d[message.time].append(noteParams(message.velocity, message.note))
                if(message.time>highest_tick):
                    highest_tick=message.time

# hasta aca tengo todos los ticks con velocidades y notas

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

fs = 44100
track_synthesis = {"channel1":getBell,"channel2":getClarinet}
t,ytot = synthesize_midi("mary.mid",track_synthesis,fs)
plt.plot(t,ytot)
plt.show()
