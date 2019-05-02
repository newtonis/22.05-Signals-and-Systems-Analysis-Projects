from mido import MidiFile


def getMidiMetadata(filename):
    data = []

    midi_file = MidiFile(filename)
    for j, track in enumerate(midi_file.tracks):
        t_on = []
        time_counter = 0
        for index, message in enumerate(track):
            if message.type == "note_on" and message.velocity != 0:
                t_on.append([time_counter, message.velocity, message.note])
        if len(t_on) > 0:
            data.append(
                {
                    "name": "Canal " + str(j),
                    "id": j
                }
            )

    return data

