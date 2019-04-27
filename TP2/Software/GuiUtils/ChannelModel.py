

class ChannelModel:
    def __init__(self, name):
        self.name = name
        self.instrumento = ""
        self.volume = 100

    def SetName(self, name):
        self.name = name

    def SetInstrumento(self, instrumento):
        self.instrumento = instrumento

    def SetVolume(self, volume):
        self.volume = volume

