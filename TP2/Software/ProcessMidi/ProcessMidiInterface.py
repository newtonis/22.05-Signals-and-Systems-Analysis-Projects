from ProcessMidi import synthesize_midi


class ProcessMidiInterface:
    def __init__(self):
        pass

    def loadConfiguration(self, channelConfig):
        print("Loading channel configuration")
        self.channelConfig = channelConfig

        filename = self.channelConfig.getMidiFilename()

        print("filename: ", filename)

