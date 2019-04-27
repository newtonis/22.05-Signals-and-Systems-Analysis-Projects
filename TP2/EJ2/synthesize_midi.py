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
    first_tempo_list = []
    for j,track in enumerate(midi_file.tracks):
        t_on = []
        t_off = []
        time_counter=0
        for index, message in enumerate(track):
            time_counter += message.time
            if message.type == "set_tempo":
                tempo_list.append([time_counter,message.tempo])
            if message.type == "note_on" and message.velocity != 0:
                t_on.append([time_counter, message.velocity, message.note])
            if (message.type == "note_on" and message.velocity == 0) or (message.type == "note_off"):
                t_off.append([time_counter, message.velocity, message.note])

        aux_track = individual_track(ticks_per_beat, total_time, fs, t_on, t_off)
        if aux_track.isNoteTrack():
            note_tracks.append(aux_track)
        if j==0:
            first_tempo_list=tempo_list #con esto seteo la lista del primer track

    if first_tempo_list==tempo_list:
        print("estoy en el formato 1, viene todo en el primero")
    else:
        print("estoy en el formato 2, viene todo segun cada track")

    tempo_list = getUniqAndSortedTempoList(tempo_list)

    all_ticks_and_responses = []
    for i,nt_track in enumerate(note_tracks):
            track_name = "track" + str(i)
            nt_track.name = track_name
            nt_track.function = tracks_synthesis[track_name]
            nt_track.tempo_list = tempo_list
            all_ticks_and_responses+=nt_track.getAmpArr()
            print(track_name+" no problem")

    total_amp_arr = zeros(int(ceil(total_time*fs)))

    for tick in all_ticks_and_responses:
        for i in range(len(tick.y)):
            total_amp_arr[i+tick.fs_tick] += tick.y[i]

    #total_amp_arr /= len(all_ticks_and_responses)
    #estaria bueno que las funciones devuelvan el arreglo normalizado directamente
    #quiza este normalize no sea lo mejor del mundo
    #Todo list de mañana:
    # -CHUNK DE MEMORIA
    # -FORMATO TIPO 2
    # -THREADS
    # -VER LO DE NORMALIZE

    total_amp_arr = normalize(total_amp_arr)

    return total_amp_arr

