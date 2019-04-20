from mido import MidiFile
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import simpleaudio as sa
import numpy as np


#importo las funciones de los intrumentos
from instruments_synth.campana import getBell
from instruments_synth.clarinete import getClarinet



def playSound(arr, fs=44100):
    arr *= 32767 / max(abs(arr))
    arr = arr.astype(np.int16)
    play_obj = sa.play_buffer(arr, 1, 2, fs)
    play_obj.wait_done()

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
    for channel, function in tracks_synthesis.items():
        for tick_val,tick_group in d.items():
            for index,nparam in enumerate(tick_group):
                yaux,duration = function(nparam.vel, nparam.note, fs)
                if not(tick_val in tick_arrs):
                    aux_ = np.arange(0,duration,1/fs)
                    tick_arrs[tick_val]=zeros(len(aux_))
                    if(tick_val==highest_tick):
                        last_arr_len = len(aux_)
                tick_arrs[tick_val]+=yaux


    #finalmente acá sumo todo segun su posicion en tiempo correspondiente
    # (la separacion de en el arreglo final es de 1/fs)

    total_time =  highest_tick*(1/fs)+last_arr_len*(1/fs)
    time_arr = arange(0, total_time, 1 / fs)

    amp_arr = zeros(len(time_arr))
    for tick,arr in tick_arrs.items():
        for i in range(len(arr)):
            amp_arr[tick+i]+=arr[i]

    return time_arr,amp_arr

fs = 44100

track_synthesis = {"channel1":getBell}
t,ytot = synthesize_midi("1hit.mid",track_synthesis,fs)
#plt.plot(t,ytot)
#plt.show()
playSound(ytot)