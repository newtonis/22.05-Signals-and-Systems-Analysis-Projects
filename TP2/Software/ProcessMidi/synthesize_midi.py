from mido import MidiFile
from ProcessMidi.synth_utils import *
from ProcessMidi import StatusInterface

# #importo las funciones de los intrumentos


def synthesize_midi(midiFilename, tracks_synthesis, fs, statusInterface = None, trackVolumes = None):
    if not statusInterface:
        statusInterface = StatusInterface.StatusInterface()

    print(trackVolumes)

    midi_file = MidiFile(midiFilename)
    ticks_per_beat = midi_file.ticks_per_beat
    total_time = midi_file.length
    note_tracks = []
    names = []
    tempo_list = []
    first_tempo_list = []

    if not trackVolumes:
        trackVolumes = dict()
        for track in tracks_synthesis:
            trackVolumes[track] = 100


    for j, track in enumerate(midi_file.tracks):
        t_on = []
        t_off = []
        t_v0 = []
        time_counter=0
        for index, message in enumerate(track):
            time_counter += message.time
            if message.type == "set_tempo":
                tempo_list.append([time_counter, message.tempo])
            if message.type == "note_on" and message.velocity != 0:
                t_on.append([time_counter, message.velocity, message.note])
            if message.type == "note_off":
                t_off.append([time_counter, message.velocity, message.note])
            if message.type == "note_on" and message.velocity == 0:
                t_v0.append([time_counter, message.velocity, message.note])

        t_apagar = []

        if len(t_on) == len(t_v0):
            t_apagar = t_v0
        elif len(t_on) == len(t_off):
            t_apagar = t_off
        else:
            statusInterface.addMessage("Se ingreso un midi extraño, el resultado puede ser extraño")

        aux_track = individual_track(ticks_per_beat, total_time, fs, t_on, t_apagar)
        if aux_track.isNoteTrack():
            note_tracks.append(aux_track)
            names.append(track)
        if j == 0:
            first_tempo_list = tempo_list #con esto seteo la lista del primer track

    if first_tempo_list == tempo_list:
        statusInterface.addMessage("Formato 1: viene todo en el primero")
    else:
        statusInterface.addMessage("Formato 2: viene todo segun cada track")

    tempo_list = getUniqAndSortedTempoList(tempo_list)

    total_amp_arr = zeros(int(ceil(total_time*fs)))

    #names = tracks_synthesis.keys()
    #print(tracks_synthesis.keys())

    length = 0
    for i, nt_track in enumerate(note_tracks):
        track_name = "Canal " + str(i)
        nt_track.name = track_name
        if track_name in tracks_synthesis:
            for j in range(len(nt_track.t_on)):
                length += 1
    #print("length = ", length)

    suma = 0
    for i, nt_track in enumerate(note_tracks):
        track_name = "Canal " + str(i)
        nt_track.name = track_name
        if track_name in tracks_synthesis:
            nt_track.function = tracks_synthesis[track_name]
            nt_track.tempo_list = tempo_list
            for j in range(len(nt_track.t_on)):
                dx,y = nt_track.getAmpArr(j)
                for k in range(len(y)):
                    if k+dx >= len(total_amp_arr):
                        pass
                    else:
                        total_amp_arr[k + dx] += y[k]
                suma += 1
                if length != 0:
                    percentaje = 0 + suma / length * 100
                else:
                    percentaje = 100
                #print(length, suma)

                statusInterface.callOnLoadUpdate(percentaje)
            statusInterface.addMessage(track_name+" ha sido procesado con exito")


    #total_amp_arr /= len(all_ticks_and_responses)
    #estaria bueno que las funciones devuelvan el arreglo normalizado directamente
    #quiza este normalize no sea lo mejor del mundo
    #Todo list de mañana:
    # -CHUNK DE MEMORIA
    # -FORMATO TIPO 2
    # -THREADS
    # -VER LO DE NORMALIZE

    total_amp_arr = normalize(total_amp_arr)

    statusInterface.addMessage("Sintetización completada")
    statusInterface.callOnSynthComplete(total_amp_arr)

    return total_amp_arr

