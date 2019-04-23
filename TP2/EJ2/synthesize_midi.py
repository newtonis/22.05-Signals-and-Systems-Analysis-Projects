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
    config_tracks=[]
    note_tracks=[]
    for index,track in enumerate(midi_file.tracks):
        for MetaMessage in track:
            if (MetaMessage.type == "set_tempo"):
                bpm = mido.tempo2bpm(MetaMessage.tempo)
                tempo = MetaMessage.tempo
            else:
                bpm = 130.1
                tempo = mido.bpm2tempo(bpm)

        aux_track=individual_track(ticks_per_beat,fs)
        aux_track.getNotes(track) # no hace nada si no hay note ons y off
        if aux_track.isNoteTrack():
            note_tracks.append(aux_track)
        else:
            config_tracks.append(aux_track)

    for i,nt_track in enumerate(note_tracks):
        channel = "channel" + str(1 + i)
        nt_track.function = tracks_synthesis[channel]
        nt_track.getAmpArr(bpm, tempo)

    list_of_amp_arr = []

    for index,track in enumerate(note_tracks):
        list_of_amp_arr.append(track.amp_arr)

    total_amp_arr=[sum(x) for x in zip(*list_of_amp_arr)]

    max = abs(amax(total_amp_arr))
    total_amp_arr = divide(total_amp_arr, max)
    total_t_arr = (0,len(total_amp_arr),fs)

    return total_t_arr,total_amp_arr

