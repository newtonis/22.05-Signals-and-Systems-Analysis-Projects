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
    for channel,function in tracks_synthesis.items():
        for index,track in enumerate(midi_file.tracks):
            if(index == 0):
                track_list.append(individual_track(ticks_per_beat,function,fs)) #aca function no pincha ni corta
                track_list[0].setFirstTrack(track)
                bpm = track_list[0].bpm
                tempo = track_list[0].tempo
            if(index>0):
                track_list.append(individual_track(ticks_per_beat,function,fs))
                track_list[index].setTrack(track,bpm,tempo)

    # ACA FALTARIA SUMAR LOS TRACKLIST [i]
    return track_list[1].time_arr,track_list[1].amp_arr

