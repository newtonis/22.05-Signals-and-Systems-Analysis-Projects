from ProcessMidi import synthesize_midi


class ProcessMidiInterface:
    def __init__(self):
        pass

    def loadConfiguration(self, channelConfig, midiFilename):
        print("Loading channel configuration")
        self.channelConfig = channelConfig
