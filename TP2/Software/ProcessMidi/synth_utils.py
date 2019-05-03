import mido
from numpy import *



def getUniqAndSortedTempoList(tempo_list):
    tempo_list.sort(key=lambda x: x[0])
    final_list = []
    for num in tempo_list:
        if num not in final_list:
            final_list.append(num)
    return final_list

def normalize(arr):
    auxarr = arr.copy()
    auxarr = auxarr-mean(auxarr) #pongo valor medio 0
    maxval = abs(amax(auxarr))
    minval = abs(amin(auxarr))
    tot_max = max(maxval, minval)
    total_amp_arr = divide(auxarr, tot_max)
    return total_amp_arr

def noteToFreq(note):
    a = 440 #frequency of A (coomon value is 440Hz)
    return (a / 32) * (2 ** ((note - 9) / 12))


class individual_track:
    name = None
    ticks_per_beat = None
    time_counter = None
    t_on = None
    t_off = None
    fs = None
    function = None
    total_time = None
    amp_arr = None
    memory = None
    tempo_list = None
    t_on_in_secs = None
    this_track_tempo = None
    track_volumes = None

    def __init__(self,ticks_per_beat_,total_time_, fs, t_on, t_off,tempo_track):
        self.ticks_per_beat = ticks_per_beat_
        self.time_counter = 0
        self.t_on = t_on
        self.t_off = t_off
        self.fs = fs
        self.function = None
        self.amp_arr = None
        self.memory = {}
        self.total_time = total_time_
        self.tempo_list = []
        self.this_track_tempo = tempo_track
        self.t_on_in_secs = None

    def tick2sec(self,tick,tempo):
        return mido.tick2second(tick, self.ticks_per_beat,tempo)

    def time2tickinfs(self,delta_t):
        #return int(floor(delta_t*self.fs))
        return int(delta_t * self.fs)

    def isNoteTrack(self):
        return len(self.t_on) > 0

    def checkIfInMemory(self,v,f,dt):
        y = []
        if not (v, f, dt) in self.memory:
            y = self.function(v, f, dt, self.fs)
            self.memory[(v, f, dt)] = y.copy()
        else:
            y = self.memory[(v, f, dt)]
        return y

    def getDelta(self, tick_on):
        delta_t = 0
        tempos_recorridos = []
        for tc, tempo_tc in self.tempo_list:
            if tc <= tick_on:
                tempos_recorridos.append([tc, tempo_tc])

        last_tc = tempos_recorridos[0][0]
        last_tempo = tempos_recorridos[0][1]
        for tc, tempo_tc in tempos_recorridos:
            delta_t += self.tick2sec(tc - last_tc, last_tempo)
            last_tc = tc
            last_tempo = tempo_tc

        last_delta_t = self.tick2sec(tick_on - last_tc, last_tempo)
        delta_t += last_delta_t

        return delta_t

    def getDeltaTHastaTick(self):
        t_on_in_secs = {}

        for i in range(len(self.t_on)):  # t_on[i]->[tick_on, vel,note]
            tick_on, tick_off = self.t_on[i][0], self.t_off[i][0]
            delta_t_on = self.getDelta(tick_on)
            delta_t_off = self.getDelta(tick_off)

            duration = abs(delta_t_off - delta_t_on)
            t_on_in_secs[tick_on] = [delta_t_on, duration]

        self.t_on_in_secs = t_on_in_secs

    def getAmpArr(self,i):
        tick_on = self.t_on[i][0]
        vel_on = self.t_on[i][1]
        note = self.t_on[i][2]

        freq = noteToFreq(note)
        time_on = self.t_on_in_secs[tick_on][0]
        delta_t = self.t_on_in_secs[tick_on][1]

        if delta_t < (1/self.fs):
            return None, []

        tick_on_in_fs = self.time2tickinfs(time_on)

        v, f, dt = vel_on, freq, delta_t
        y = self.checkIfInMemory(v, f, dt)

        if self.name in self.track_volumes:
            track_vol = self.track_volumes[self.name]

        y *= track_vol / 100

        return tick_on_in_fs, y
