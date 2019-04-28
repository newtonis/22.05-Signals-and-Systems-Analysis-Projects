from GuiUtils.ChannelCard import ChannelCard




class ChannelModel:
    def __init__(self, id, name):
        self.viewClass = ChannelCard
        self.id = id
        self.name = name
        self.instrumento = "Sin elegir instrumento"
        self.volume = 100
        self.enabled = True
        self.channelBackground = "blue"
        self.instrumentBackground = "pink"
        self.onConfigure = None

    def getViewClass(self):
        return self.viewClass

    def getType(self):
        return self.type

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def setInstrumento(self, instrumento):
        self.instrumento = instrumento
        return self

    def setVolume(self, volume):
        self.volume = volume
        return self

    def setChannelBackground(self, color):
        self.channelBackground = color
        return self

    def setInstrumentBackground(self, color):
        self.instrumentBackground = color
        return self

    def setOnConfigureListener(self, action):
        self.onConfigure = action
        return self

    def getName(self):
        return self.name

    def getInstrumento(self):
        return self.instrumento

    def getVolume(self):
        return self.volume

    def getChannelBackground(self):
        return self.channelBackground

    def getInstrumentBacgrkound(self):
        return self.instrumentBackground

    def toggleEnable(self):
        if self.enabled:
            self.enabled = False
        else:
            self.enabled = True

    def getEnabled(self):
        return self.enabled

    def getOnConfigureListener(self):
        return self.onConfigure
