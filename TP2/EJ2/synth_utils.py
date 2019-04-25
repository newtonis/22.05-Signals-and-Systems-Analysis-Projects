import mido
from numpy import *

def normalize(arr):
    maxval = abs(amax(arr))
    minval = abs(amin(arr))
    tot_max = max(maxval, minval)
    total_amp_arr = divide(arr, tot_max)
    return total_amp_arr

def noteToFreq(note):
    a = 440 #frequency of A (coomon value is 440Hz)
    return (a / 32) * (2 ** ((note - 9) / 12))

class messageInfo:
    vel = None
    note = None
    time = None
    def __init__(self, vel_, note_, time_):
        self.vel = vel_
        self.note = note_
        self.time = time_

class noteParams:
    note = None
    v_on = None
    v_off = None
    time = None
    delta_t = None
    def __init__(self,note,v_on,v_off,time,delta_t):
        self.note = note
        self.v_on = v_on
        self.v_off = v_off
        self.time = time
        self.delta_t = delta_t


class individual_track:
    noteParams = None
    tempo = None
    ticks_per_beat = None
    bpm = None
    time_counter = None
    t_on = None
    t_off = None
    note_info = None
    fs = None
    function = None
    time_arr = None
    total_time = None
    amp_arr = None
    memory = None

    def __init__(self,ticks_per_beat_,bpm_,tempo_,total_time_, fs):
        self.tempo = tempo_
        self.ticks_per_beat = ticks_per_beat_
        self.bpm = bpm_
        self.time_counter = 0
        self.t_on = {}
        self.t_off = {}
        self.noteParams = None
        self.fs = fs
        self.function = None
        self.total_time = None
        self.amp_arr = None
        self.time_arr=None
        self.memory = {}
        self.note_info = {}
        self.total_time = total_time_

    def tick2sec(self,tick_):
        return mido.tick2second(tick_, self.ticks_per_beat, self.tempo)

    def tickintempo2tickinfs(self,time_tick):
        return int(floor(mido.tick2second(time_tick, self.ticks_per_beat, self.tempo) * (self.fs)))

    def isNoteTrack(self):
        return len(self.t_on) > 0

    def getNotes(self,track):
        for message in track:
            self.time_counter+=message.time
            if message.type == "note_on" and message.velocity != 0:
                if not message.note in self.t_on:
                    self.t_on[message.note] = []
                self.t_on[message.note].append(messageInfo(message.velocity,message.note,self.time_counter))
            if(message.type == "note_on" and message.velocity == 0) or (message.type == "note_off"):
                if not message.note in self.t_off:
                    self.t_off[message.note] = []
                self.t_off[message.note].append(messageInfo(message.velocity,message.note,self.time_counter))

        for note, messageInfo_arr in self.t_on.items():
            for i,message in enumerate(messageInfo_arr):
                time_on = self.tick2sec(self.t_on[note][i].time)
                time_off = self.tick2sec(self.t_off[note][i].time)
                delta_t= abs(time_on-time_off)
                note = self.t_on[note][i].note
                v_on = self.t_on[note][i].vel
                v_off = self.t_off[note][i].vel
                if not note in self.note_info:
                    self.note_info[note]=[]
                self.note_info[note].append(noteParams(note,v_on,v_off,self.t_on[note][i].time,delta_t))

    def getAmpArr(self):
        self.time_arr = arange(0, self.total_time, 1 / self.fs)
        self.amp_arr = zeros(len(self.time_arr))

        for notes, note_param_arr in self.note_info.items():
            for note_param in note_param_arr:
                freq = noteToFreq(note_param.note)
                v,f,dt = note_param.v_on,freq,note_param.delta_t
                y = []
                if not (v,f,dt) in self.memory:
                    y = self.function(v, f, dt, self.fs)
                    self.memory[(v,f,dt)]=y.copy()
                else:
                    y = self.memory[(v,f,dt)]
                dx = int(floor(mido.tick2second(note_param.time,self.ticks_per_beat,self.tempo)*(self.fs)))
                for j in range(len(y)):
                    if(j+dx == 7243426):
                        print("asd")
                    self.amp_arr[j+dx]+=y[j]

        self.amp_arr = normalize(self.amp_arr)

