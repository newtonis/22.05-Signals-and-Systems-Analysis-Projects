from mido import MidiFile
from synth_utils import *
#
# #importo las funciones de los intrumentos
from instruments_synth.campana import getBell
from instruments_synth.clarinete import getClarinet

import threading

def synthesize_midi( midiFilename ,tracks_synthesis ,fs):
    midi_file = MidiFile(midiFilename)
    ticks_per_beat = midi_file.ticks_per_beat
    total_time = midi_file.length
    bpm = 0
    tempo = 0
    config_tracks=[]
    note_tracks=[]
    for index,track in enumerate(midi_file.tracks):
        for MetaMessage in track:
            if (MetaMessage.type == "set_tempo"):
                bpm = mido.tempo2bpm(MetaMessage.tempo)
                tempo = MetaMessage.tempo
                #print("tempo:",tempo)

        aux_track=individual_track(ticks_per_beat,bpm,tempo,total_time,fs)
        aux_track.getNotes(track) # no hace nada si no hay note ons y off
        if aux_track.isNoteTrack():
            note_tracks.append(aux_track)
        else:
            config_tracks.append(aux_track)
    #threads_arr=[]
    for i,nt_track in enumerate(note_tracks):
        channel = "channel" + str(1 + i)
        nt_track.function = tracks_synthesis[channel]
        nt_track.getAmpArr()
        print("track "+str(i)+"no problem")

    #     threads_arr.append(threading.Thread(name='thread_track'+str(1+i),target=nt_track.getAmpArr,
    #                                         args=(bpm,tempo)))
    #     threads_arr[i].start()
    #
    # for thread in threads_arr:
    #     thread.join()

    list_of_amp_arr = []

    for index,track in enumerate(note_tracks):
        list_of_amp_arr.append(track.amp_arr)

    total_amp_arr=[sum(x) for x in zip(*list_of_amp_arr)]

    total_amp_arr = normalize(total_amp_arr)

    total_t_arr = (0,len(total_amp_arr),fs)

    return total_t_arr,total_amp_arr

