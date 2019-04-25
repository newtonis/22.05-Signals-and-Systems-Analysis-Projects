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
    tick_in_fs = None
    delta_t = None
    def __init__(self,note,v_on,v_off,time,delta_t,tick_in_fs):
        self.note = note
        self.v_on = v_on
        self.v_off = v_off
        self.time = time
        self.delta_t = delta_t
        self.tick_in_fs =tick_in_fs


class individual_track:
    name = None
    noteParams = None
    ticks_per_beat = None
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
    tempo_dict = None
    track = None
    tempo_list = None

    def __init__(self,ticks_per_beat_,total_time_, fs):
        self.ticks_per_beat = ticks_per_beat_
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
        self.tempo_dict = {}
        self.tempo_list = []

    def getTempo(self,t):
        last_tempo = None
        if(len(self.tempo_dict)>0):
            for tick_original in self.tempo_dict:
                if last_tempo == None:
                    last_tempo = self.tempo_dict[tick_original]
                if tick_original <= t:
                    last_tempo = self.tempo_dict[tick_original]
        else:
            last_tempo = 1000000000
            for tempo in self.tempo_list:
                last_tempo= min(last_tempo,tempo)

            print("hola")

        return last_tempo

    def tick2sec(self,tick,tempo):
        return mido.tick2second(tick, self.ticks_per_beat,tempo)

    def tickintempo2tickinfs(self,time_tick,tempo):
        return int(floor(mido.tick2second(time_tick, self.ticks_per_beat,tempo) * (self.fs)))

    def isNoteTrack(self):
        return len(self.t_on) > 0

    def getNotes(self,track):
        self.track = track
        for message in self.track:
            self.time_counter+=message.time
            if message.type == "set_tempo":
                self.tempo_dict[self.time_counter] = message.tempo
            if message.type == "note_on" and message.velocity != 0:
                if not message.note in self.t_on:
                    self.t_on[message.note] = []
                self.t_on[message.note].append(messageInfo(message.velocity, message.note,self.time_counter))
            if(message.type == "note_on" and message.velocity == 0) or (message.type == "note_off"):
                if not message.note in self.t_off:
                    self.t_off[message.note] = []
                self.t_off[message.note].append(messageInfo(message.velocity,message.note,self.time_counter))


    def groupNotes(self):
        for note, messageInfo_arr in self.t_on.items():
            for i, message in enumerate(messageInfo_arr):
                tick_on = self.t_on[note][i].time
                tick_off = self.t_off[note][i].time

                #aca falla porque hay veces que el track setea el tempo general
                # y no lo hace por cada track
                tempo_on = self.getTempo(tick_on) # por ahora solo tengo tempo_on

                time_on = self.tick2sec(tick_on, tempo_on)
                time_off = self.tick2sec(tick_off,tempo_on)

                delta_t = abs(time_on-time_off)
                note = self.t_on[note][i].note
                v_on = self.t_on[note][i].vel
                v_off = self.t_off[note][i].vel

                tick_on_in_fs = self.tickintempo2tickinfs(tick_on,tempo_on)

                if not note in self.note_info:
                    self.note_info[note]=[]
                self.note_info[note].append(noteParams(note, v_on, v_off, tick_on, delta_t,tick_on_in_fs))


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

                dx = note_param.tick_in_fs

                for j in range(len(y)):
                    self.amp_arr[j+dx]+=y[j]

        self.amp_arr = normalize(self.amp_arr)

