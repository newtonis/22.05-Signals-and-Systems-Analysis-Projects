from mido import MidiFile
from synth_utils import *
import midi
# #importo las funciones de los intrumentos
from instruments_synth.campana import getBell
from instruments_synth.clarinete import getClarinet
from instruments_synth.guitarra import SitetizarGuitarraDistorsion
from instruments_synth.trombon import getBrassTone

import threading
import time

def sumAmpArr2Total(total_amp_arr,y,dx,track_name):
    exceso = False
    for k in range(len(y)):
        if k + dx >= len(total_amp_arr):
            if exceso == False:
                print("fuera de rango", track_name, " iteracion: ", k)
                exceso = True
        else:
            total_amp_arr[k + dx] += y[k]

def ThreadPaso(num_hilo, **datos):
    contador = datos['inicio']
    limite = datos['limite']
    nt_track = datos['note_track']
    total_amp_arr = datos['total']
    track_name = datos['track_name']

    for i in range(contador, limite):
        dx, y = nt_track.getAmpArr(i)
        sumAmpArr2Total(total_amp_arr, y, dx,track_name)

def sumTrack2TotalConThreads(total_amp_arr,nt_track):

    thread_indexes_inferior = []
    thread_indexes = []
    total = len(nt_track.t_on)
    min_step = int(total/10)
    last_step = total % min_step
    #esto falla si total fuera igual a 0
    #pero no pasa porque nos fijamos antes que la len de t_on sea mayor a 0
    cnt = 0
    while cnt < total:
        if cnt+min_step <= total:
            thread_indexes_inferior.append(cnt)
            cnt += min_step
            thread_indexes.append(cnt)
        elif cnt+last_step <= total:
            thread_indexes_inferior.append(cnt)
            cnt += last_step
            thread_indexes.append(cnt)

    threads_arr=[]

    for num_hilo in range(len(thread_indexes)):
        threads_arr.append(threading.Thread(target=ThreadPaso,
                                args=(num_hilo,),
                                kwargs={'inicio': thread_indexes_inferior[num_hilo],
                                        'limite': thread_indexes[num_hilo],
                                            'total': total_amp_arr,
                                            'note_track':nt_track,
                                        'track_name':nt_track.name}))
        threads_arr[num_hilo].start()
    for thread in threads_arr:
        thread.join()

def sumTrack2TotalSinThreads(total_amp_arr,nt_track):
    for j in range(len(nt_track.t_on)):
        dx, y = nt_track.getAmpArr(j)
        for k in range(len(y)):
            if k + dx >= len(total_amp_arr):
                if exceso == False:
                    print("fuera de rango", nt_track.name, " iteracion: ", k)
                    exceso = True
            else:
                total_amp_arr[k + dx] += y[k]
    print(nt_track.name,"no problem")

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
    #--------------------------------------------------------
    ticks_per_beat = midi_file.ticks_per_beat
    total_time = midi_file.length
    note_tracks = []
    tempo_list = []
    first_tempo_list = []
    #obtengo toda la info de los midis y los guardo en note_tracks
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
            # solo si ya hay un note_on agrego note_off o note_on con v=0
            #if (len(t_on)-1) == len(t_off):
            if message.type == "note_off":
                if len(t_off) < len(t_on):
                    t_off.append([time_counter, message.velocity, message.note])
            if message.type == "note_on" and message.velocity == 0:
                if len(t_v0) < len(t_on):
                    t_v0.append([time_counter, message.velocity, message.note])

        t_apagar = get_toff(t_on, t_v0, t_off)

        aux_track = individual_track(ticks_per_beat, total_time, fs, t_on, t_apagar,tempo_track)

        if aux_track.isNoteTrack():
            note_tracks.append(aux_track)
        if j == 0:
            first_tempo_list = tempo_list.copy()

    format = None
    # me fijo que formato es
    if first_tempo_list == tempo_list:
        print("estoy en el formato 1, viene todo en el primero")
        format = "first"
    else:
        print("estoy en el formato 2, viene todo segun cada track")
        format = "second"

    total_amp_arr = zeros(int(ceil(total_time*fs)))

    threads_arr = []

    start = time.time()

    #setup de cada track
    for i,nt_track in enumerate(note_tracks):
        track_name = "track" + str(i)
        nt_track.name = track_name
        nt_track.function = tracks_synthesis[track_name]
        if format == "first":
            nt_track.tempo_list = first_tempo_list
        elif format == "second":
            nt_track.tempo_list = nt_track.this_track_tempo
        else:
            print("no hay formato, esto no deberia pasar")
        threads_arr.append(threading.Thread(target=sumTrack2TotalSinThreads,
                                args=(total_amp_arr,nt_track,),
                                kwargs={}))
        threads_arr[i].start()
    print("ya esta listo el setup de tracks")
    # --------------------------------------------------------

    for thread in threads_arr:
        thread.join()
    # for nt_track in note_tracks:
    #     sumTrack2TotalSinThreads(total_amp_arr,nt_track)

        #print(nt_track.name + " no problem")


    #sin threads greenhill = 0.7333333333333333  minutos
    #con threads greenhill = 0.7166666666666667 minutos
    # ojo, para que los threads funcionen bien
    # hay que cerrar todo lo que tengamos abierto
    # es decir si estamos usando el cpu al 100% poner threads no cambia nada
    # y hasta puede ser peor

    total_amp_arr = normalize(total_amp_arr)
    end = time.time()
    print("se sintetizo en ",int(abs(end-start))/60," minutos")
    return total_amp_arr

