from ProcessMidi.synthesize_midi import synthesize_midi
from ProcessMidi.StatusInterface import StatusInterface
from GuiUtils.Listener import Listener

from threading import Thread
from Globals import config


class ProcessMidiInterface:
    def __init__(self):
        self.channelConfig = None
        self.midiFilename = None
        self.onMsgArrived = None
        self.onLoadUpdate = None
        self.onComplete = None

    def start(self, configuration, statusInterface = None):
        #print("Loading channel configuration")
        self.channelConfig = configuration.getChannels()
        self.midiFilename = configuration.getMidiFilename()

        self.statusInterface = StatusInterface()\
            .setMessageListener(
                Listener(self.messageArrived)
            )\
            .setLoadListener(
                Listener(self.updateLoad)
            )\
            .setOnCompleteListener(
                Listener(self.onComplete)
            )

        track_syntesis = dict()

        for track in self.channelConfig:
            if track.getInstrumento():
                track_syntesis[track.name] = track.getInstrumento().getInstrumentData().getFunction()

        self.thread = Thread(
            target=synthesize_midi,
            args=(self.midiFilename, track_syntesis, config.fs, self.statusInterface)
        )

        self.thread.start()

    def messageArrived(self, msg):
        if self.onMsgArrived:
            self.onMsgArrived(msg)

    def setOnMsgArrived(self, func):
        self.onMsgArrived = func

    def setOnLoadUpdate(self, func):
        self.onLoadUpdate = func

    def setOnComplete(self, func):
        self.onComplete = func

    def updateLoad(self, percentaje):
        if self.onLoadUpdate:
            self.onLoadUpdate(percentaje)


processMidiInterface = None


def getProcessMidiInterface():
    global processMidiInterface

    if not processMidiInterface:
        processMidiInterface = ProcessMidiInterface()

    return processMidiInterface