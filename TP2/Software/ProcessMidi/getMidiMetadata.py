from mido import MidiFile


def getMidiMetadata(filename):
    data = []

    midi_file = MidiFile(filename)
    for j, track in enumerate(midi_file.tracks):
        data.append(
            {
                "name": "Canal " + str(j),
                "id": j
            }
        )

    return data

