from mido import MidiFile


def getMidiMetadata(filename):
    data = []

    midi_file = MidiFile(filename)
    j = 0
    for track in midi_file.tracks:
        t_on = []
        time_counter = 0
        for message in track:
            if message.type == "note_on" and message.velocity != 0:
                t_on.append([time_counter, message.velocity, message.note])
        if len(t_on) > 0:
            data.append(
                {
                    "name": "Canal " + str(j),
                    "id": j
                }
            )
            j += 1

    return data

