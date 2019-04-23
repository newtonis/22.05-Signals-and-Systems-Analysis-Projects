from mido import MidiFile
from numpy import *
import mido
from synth_utils import *

#importo las funciones de los intrumentos
from instruments_synth.campana import getBell
from instruments_synth.clarinete import getClarinet


def synthesize_midi( midiFilename ,tracks_synthesis ,fs):
    midi_file = MidiFile(midiFilename)
    ticks_per_beat = midi_file.ticks_per_beat
    bpm = 0
    tempo = 0
    track_list=[]
    for index,track in enumerate(midi_file.tracks):
        for MetaMessage in track:
            if (MetaMessage.type == "set_tempo"):
                bpm = mido.tempo2bpm(MetaMessage.tempo)
                tempo = MetaMessage.tempo
            else:
                bpm = 130.1
                tempo = mido.bpm2tempo(bpm)

        track_list.append(individual_track(ticks_per_beat,fs))
        track_list[index].getNotes(track) # no hace nada si no hay note ons y off
        if(len(track_list[index].t_on)>0):
            channel = "channel"+str(index)
            track_list[index].function=tracks_synthesis[channel]


    for track_el in track_list:
        if(len(track_el.t_on)>0): #esto significa que hay al menos una nota
            track_el.getAmpArr(bpm,tempo)

    total_t_arr = 0
    total_amp_arr = 0
    j = 0
    for index,track_el in enumerate(track_list):
        if (len(track_el.t_on) > 0):  # esto significa que hay al menos una nota
            if(j==0):
                total_amp_arr = track_el.amp_arr.copy()
                total_t_arr = track_el.time_arr
                j+=1
            else:
                total_amp_arr+=track_el.amp_arr
                j+=1

    max = abs(amax(total_amp_arr))
    total_amp_arr = divide(total_amp_arr, max)
    # ACA FALTARIA SUMAR LOS TRACKLIST [i]
    return total_t_arr,total_amp_arr

