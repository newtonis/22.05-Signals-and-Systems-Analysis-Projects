import mido
from numpy import *

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

class individual_track:
    noteParams = None
    tempo = None
    ticks_per_beat = None
    bpm = None
    time_counter = None
    t_on = None
    t_off = None
    fs = None
    function = None
    time_arr = None
    total_time = None
    amp_arr = None
    def __init__(self,ticks_per_beat_, fs):
        self.tempo = None
        self.ticks_per_beat = ticks_per_beat_
        self.bpm = None
        self.time_counter = 0
        self.t_on = {}
        self.t_off = {}
        self.noteParams = None
        self.fs = fs
        self.function = None
        self.total_time = None
        self.amp_arr = None
        self.time_arr=None

    def getNotes(self,track):
        for message in track:
            self.time_counter+=message.time
            if message.type == "note_on" and message.velocity != 0:
                if not message.note in self.t_on:
                    self.t_on[message.note] = []
                self.t_on[message.note].append(noteParams(message.velocity,message.note,self.time_counter))
            if(message.type == "note_on" and message.velocity == 0) or (message.type == "note_off"):
                if not message.note in self.t_off:
                    self.t_off[message.note] = []
                self.t_off[message.note].append(noteParams(message.velocity,message.note,self.time_counter))

    def getAmpArr(self,bpm,tempo):
        self.bpm = bpm
        self.tempo = tempo
        # ahora quiero obtener para cada nota un delta t dado por t_on y t_off
        for note, note_param_arr in self.t_on.items():  # note es la key del dict
            for i in range(len(note_param_arr)):
                note_param_arr[i].delta_t = mido.tick2second(abs(self.t_on[note][i].time - self.t_off[note][i].time),
                                                             self.ticks_per_beat, self.tempo)

        self.total_time = mido.tick2second(self.time_counter,self.ticks_per_beat,self.tempo)
        self.time_arr = arange(0, self.total_time, 1 / self.fs)
        self.amp_arr = zeros(len(self.time_arr))

        for notes, note_param_arr in self.t_on.items():
            for nparam in note_param_arr:
                freq = noteToFreq(nparam.note)
                y = self.function(nparam.vel,freq,nparam.delta_t,self.fs)
                dx= int(floor(mido.tick2second(nparam.time,self.ticks_per_beat,self.tempo)*(self.fs)))
                for i in range(len(y)):
                    self.amp_arr[i+dx]+=y[i]

        max = abs(amax(self.amp_arr))
        self.amp_arr = divide(self.amp_arr, max)


