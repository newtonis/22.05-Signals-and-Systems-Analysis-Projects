from mido import MidiFile
from synth_utils import *
import midi
# #importo las funciones de los intrumentos
from instruments_synth.campana import getBell
from instruments_synth.clarinete import getClarinet
from instruments_synth.guitarra import SitetizarGuitarraDistorsion
from instruments_synth.trombon import getBrassTone
import threading

def get_toff(t_on,t_v0,t_off):
    t_apagar=[]
    if len(t_on) == len(t_v0):
        t_apagar = t_v0
    elif len(t_on) == len(t_off):
        t_apagar = t_off
    else:
        if len(t_on) < len(t_v0):
            t_apagar = t_v0[0:len(t_on)]
            print("se recorto t_v0 por tener mas tamaño que t_on")
        elif len(t_on) < len(t_off):
            t_apagar = t_v0[0:len(t_on)]
            print("se recorto t_off por tener mas tamaño que t_on")
        print("Se ingreso un midi extraño, el resultado puede ser extraño")
    return t_apagar

def synthesize_midi(midiFilename ,tracks_synthesis ,fs):
    midi_file = MidiFile(midiFilename)
    #midi_file = midi.read_midifile(midiFilename)
    ticks_per_beat = midi_file.ticks_per_beat
    total_time = midi_file.length
    note_tracks = []
    tempo_list = []
    first_tempo_list = []
    for j, track in enumerate(midi_file.tracks):
        t_on = []
        t_off = []
        t_v0 = []
        time_counter = 0
        tempo_track = []

        for index, message in enumerate(track):
            time_counter += message.time
            if message.type == "set_tempo":
                tempo_list.append([time_counter, message.tempo])
                tempo_track.append([time_counter, message.tempo])
            if message.type == "note_on" and message.velocity != 0:
                t_on.append([time_counter, message.velocity, message.note])
            if message.type == "note_off":
                t_off.append([time_counter, message.velocity, message.note])
            if message.type == "note_on" and message.velocity == 0:
                t_v0.append([time_counter, message.velocity, message.note])

        t_apagar = get_toff(t_on, t_v0, t_off)

        aux_track = individual_track(ticks_per_beat, total_time, fs, t_on, t_apagar,tempo_track)

        if aux_track.isNoteTrack():
            note_tracks.append(aux_track)
        if j == 0:
            first_tempo_list = tempo_list.copy()

    Format = None
    if first_tempo_list == tempo_list:
        print("estoy en el formato 1, viene todo en el primero")
        Format = "first"
    else:
        print("estoy en el formato 2, viene todo segun cada track")
        Format = "second"

    tempo_list = getUniqAndSortedTempoList(tempo_list)

    total_amp_arr = zeros(int(ceil(total_time*fs)))

    for i,nt_track in enumerate(note_tracks):
        track_name = "track" + str(i)
        nt_track.name = track_name
        nt_track.function = tracks_synthesis[track_name]
        if Format == "first":
            nt_track.tempo_list = tempo_list
        elif Format == "second":
            nt_track.tempo_list = nt_track.this_track_tempo
        else:
            print("no hay formato, esto no deberia pasar")

        exceso = False
        for j in range(len(nt_track.t_on)):
            dx,y = nt_track.getAmpArr(j)
            for k in range(len(y)):
                if k+dx >= len(total_amp_arr):
                    if exceso == False:
                        print("fuera de rango",track_name," iteracion: ",k)
                        exceso = True
                else:
                    total_amp_arr[k + dx] += y[k]
        print(track_name+" no problem")

    #Todo list de mañana:
    # -CHUNK DE MEMORIA
    # -VER LO DE NORMALIZE

    total_amp_arr = normalize(total_amp_arr)

    return total_amp_arr

