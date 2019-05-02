from mido import MidiFile
from ProcessMidi.synth_utils import *
from ProcessMidi import StatusInterface

# #importo las funciones de los intrumentos

def sumTrack2TotalSinThreads(total_amp_arr,nt_track,suma,length,status):
    exceso = False
    for j in range(len(nt_track.t_on)):
        dx, y = nt_track.getAmpArr(j)
        for k in range(len(y)):
            if k + dx >= len(total_amp_arr):
                if exceso == False:
                    print("fuera de rango", nt_track.name, " iteracion: ", k)
                    exceso = True
            else:
                total_amp_arr[k + dx] += y[k]
        suma[0] += 1
        if length[0] != 0:
            percentaje = 0 + suma[0] / length[0] * 100
        else:
            percentaje = 100

        status.callOnLoadUpdate(percentaje)
    status.addMessage(nt_track.name + " ha sido procesado con exito")


def synthesize_midi(midiFilename, tracks_synthesis, fs, statusInterface = None, trackVolumes = None):
    if not statusInterface:
        statusInterface = StatusInterface.StatusInterface()

    #print(trackVolumes)

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

    # --------------------------------------------------------
    ticks_per_beat = midi_file.ticks_per_beat
    total_time = midi_file.length
    note_tracks = []
    tempo_list = []
    first_tempo_list = []
    # obtengo toda la info de los midis y los guardo en note_tracks
    tempoIsAlreadySet = False
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
                if tempoIsAlreadySet == False:
                    first_tempo_list.append([time_counter, message.tempo])
            if message.type == "note_on" and message.velocity != 0:
                t_on.append([time_counter, message.velocity, message.note])
            # solo si ya hay un note_on agrego note_off o note_on con v=0
            # if (len(t_on)-1) == len(t_off):
            if message.type == "note_off":
                if len(t_off) < len(t_on):
                    t_off.append([time_counter, message.velocity, message.note])
            if message.type == "note_on" and message.velocity == 0:
                if len(t_v0) < len(t_on):
                    t_v0.append([time_counter, message.velocity, message.note])

        if len(first_tempo_list) > 0:
            tempoIsAlreadySet = True
        t_apagar,strange = get_toff(t_on, t_v0, t_off)
        if strange == True :
            statusInterface.addMessage("Se ingreso un midi extraño, el resultado puede ser extraño")

        aux_track = individual_track(ticks_per_beat, total_time, fs, t_on, t_apagar, tempo_track)

        if aux_track.isNoteTrack():
            note_tracks.append(aux_track)

    format = None
    # me fijo que formato es
    if first_tempo_list == tempo_list:
        statusInterface.addMessage("Formato 1: viene todo en el primero")
        format = "first"
    else:
        statusInterface.addMessage("Formato 2: viene todo segun cada track")
        format = "second"

    total_amp_arr = zeros(int(ceil(total_time*fs)))

    length = 0
    for i,nt_track in enumerate(note_tracks):
        track_name = "Canal " + str(i)
        nt_track.name = track_name
        if track_name in tracks_synthesis:
            for j in range(len(nt_track.t_on)):
                length += 1

    length = [length]

    suma = [0]
    for i, nt_track in enumerate(note_tracks):
        track_name = "Canal " + str(i)
        nt_track.name = track_name
        if track_name in tracks_synthesis:
            nt_track.function = tracks_synthesis[track_name]
            if format == "first":
                nt_track.tempo_list = first_tempo_list
            elif format == "second":
                nt_track.tempo_list = nt_track.this_track_tempo

            nt_track.track_volumes = trackVolumes

            sumTrack2TotalSinThreads(total_amp_arr, nt_track, suma, length, statusInterface)

    total_amp_arr = normalize(total_amp_arr)

    statusInterface.addMessage("Sintetización completada")
    statusInterface.callOnSynthComplete(total_amp_arr)

    return total_amp_arr

