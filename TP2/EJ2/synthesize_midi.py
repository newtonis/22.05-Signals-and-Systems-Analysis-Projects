from mido import MidiFile
from numpy import *
import mido
import matplotlib.pyplot as plt
import numpy as np

#importo las funciones de los intrumentos
from instruments_synth.campana import getBell
from instruments_synth.clarinete import getClarinet

def noteToFreq(note):
    a = 440 #frequency of A (coomon value is 440Hz)
    return (a / 32) * (2 ** ((note - 9) / 12))

class noteParams:
    vel = None
    note = None
    time = None
    delta_t = None
    def __init__(self,vel_=None,note_=None,time_ = None,delta_t_ = None):
        self.vel = vel_
        self.note = note_
        self.time = time_
        self.delta_t = delta_t_

def synthesize_midi( midiFilename ,tracks_synthesis ,fs):
    midi_file = MidiFile(midiFilename)
    bpm = 0
    ticks_per_beat = midi_file.ticks_per_beat
    tempo = 0
    t_on={}
    t_off={}
    time_counter = 0
    for track in midi_file.tracks:
        for MetaMessage in track:
            if(MetaMessage.type == "set_tempo"):
                bpm = mido.tempo2bpm(MetaMessage.tempo)
                tempo = MetaMessage.tempo
            #if(MetaMessage.type == "")
        for message in track:
            time_counter+=message.time
            if message.type == "note_on" and message.velocity != 0:
                #t_on = message.time
                if not message.note in t_on:
                    t_on[message.note] = []
                t_on[message.note].append(noteParams(message.velocity,message.note,time_counter))
            if(message.type == "note_on" and message.velocity == 0) or (message.type == "note_off"):
                if not message.note in t_off:
                    t_off[message.note] = []
                t_off[message.note].append(noteParams(message.velocity,message.note,time_counter))


    #ahora quiero obtener para cada nota un delta t dado por t_on y t_off

    for note,note_param_arr in t_on.items(): #note es la key del dict
        for i in range(len(note_param_arr)):
            note_param_arr[i].delta_t = mido.tick2second(abs(t_on[note][i].time-t_off[note][i].time),ticks_per_beat,tempo)

    #finalmente acá sumo todo segun su posicion en tiempo correspondiente

    time_arr = arange(0,mido.tick2second(time_counter,ticks_per_beat,tempo),1/fs)
    amp_arr = zeros(len(time_arr))

    segs_per_tick=mido.tick2second(1,ticks_per_beat,tempo)

    for channel, function in tracks_synthesis.items():
        for notes, note_param_arr in t_on.items():
            for nparam in note_param_arr:
                freq = noteToFreq(nparam.note)
                y = function(nparam.vel,freq,nparam.delta_t,fs)
                dx= int(floor(mido.tick2second(nparam.time,ticks_per_beat,tempo)*(fs)))
                for i in range(len(y)):
                    amp_arr[i+dx]+=y[i]

    max = abs(amax(amp_arr))
    amp_arr = divide(amp_arr,max)
    return time_arr,amp_arr
