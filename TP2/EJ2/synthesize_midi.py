from mido import MidiFile
from synth_utils import *

# #importo las funciones de los intrumentos
from instruments_synth.campana import getBell
from instruments_synth.clarinete import getClarinet
from instruments_synth.guitarra import SitetizarGuitarraDistorsion
import threading

def synthesize_midi( midiFilename ,tracks_synthesis ,fs):
    midi_file = MidiFile(midiFilename)
    ticks_per_beat = midi_file.ticks_per_beat
    total_time = midi_file.length
    note_tracks = []
    tempo_list = []
    time_counter = 0
    for track in midi_file.tracks:
        for index, message in enumerate(track):
            time_counter += message.time
            if message.type == "set_tempo":
                tempo_list.append([time_counter,message.tempo])
        aux_track = individual_track(ticks_per_beat,total_time,fs)
        aux_track.getNotes(track)
        if aux_track.isNoteTrack():
            note_tracks.append(aux_track)
        time_counter=0

    tempo_list = getUniqAndSortedTempoList(tempo_list)

    for i,nt_track in enumerate(note_tracks):
            track_name = "track" + str(i)
            nt_track.name = track_name
            nt_track.function = tracks_synthesis[track_name]
            nt_track.tempo_list = tempo_list
            nt_track.getAmpArr()
            print(track_name+" no problem")

    total_amp_arr = sumAllTracks(note_tracks)
    total_amp_arr = normalize(total_amp_arr)
    return total_amp_arr

