import midi
import fluidsynth
#pude instalar midi con esto
#pip install git+https://github.com/vishnubob/python-midi@feature/python3

# Instantiate a MIDI Pattern (contains a list of tracks)
pattern = midi.Pattern()
# Instantiate a MIDI Track (contains a list of MIDI events)
track = midi.Track()
# Append the track to the pattern
pattern.append(track)
# Instantiate a MIDI note on event, append it to the track
on = midi.NoteOnEvent(tick=0, velocity=20, pitch=midi.G_3)
track.append(on)
# Instantiate a MIDI note off event, append it to the track
off = midi.NoteOffEvent(tick=100, pitch=midi.G_3)
track.append(off)
# Add the end of track event, append it to the track
eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)
# Print out the pattern
print(pattern)
# Save the pattern to disk
midi.write_midifile("example.mid", pattern)


#fs.midi_to_audio("mary.mid","output.wav")

# # use a custom sound font
# FluidSynth('sound_font.sf2')
# # use a custom sample rate
# FluidSynth(sample_rate=22050)