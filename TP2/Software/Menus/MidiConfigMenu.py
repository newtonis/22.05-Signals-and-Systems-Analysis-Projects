import tkinter as tk
from GuiUtils.ChannelCard import ChannelCard
from GuiUtils.ChannelModel import ChannelModel
from GuiUtils.RecyclerView import RecyclerView
from GuiUtils.Listener import Listener
from GuiUtils.SynthetizeConfig import SyntetizeConfig
from Menus.ConfigureChannelMenu import ConfigureChannelMenu
from Menus.ProcessingMidiMenu import ProcessMidiMenu

from ProcessMidi.getMidiMetadata import getMidiMetadata
from Globals import config
from tkinter import *
from tkinter import filedialog
import ntpath


def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))


class MidiConfigMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            text="Configuración de canales",
            font=config.LARGE_FONT,
            background="#ccffd5"
        )

        self.title.pack(side=tk.TOP, fill=BOTH)

        self.selectMidiMenu = MidiFileSelector(
            self,
            self.controller
        )
        self.selectMidiMenu.pack(side=tk.TOP, fill=BOTH, expand=1)

        self.halfContainer = tk.Frame(self)

        self.recyclerView = RecyclerView(self.halfContainer, self.controller)

        tk.Frame(self.halfContainer).grid(column=0, row=0)
        self.recyclerView.grid(column=1, row=0)
        tk.Frame(self.halfContainer).grid(column=2, row=0)

        self.halfContainer.grid_columnconfigure(0, weight=1)
        self.halfContainer.grid_columnconfigure(1, weight=10)
        self.halfContainer.grid_columnconfigure(2, weight=1)

        self.halfContainer.pack(side=tk.TOP, fill=BOTH)

        self.buttonProcess = tk.Button(
            self,
            height=1,
            width=50,
            text="Generar música",
            font=config.SMALL_FONT,
            background="#ccffd5",
            command=self.generateMusic
        )
        self.buttonProcess.pack(side=tk.TOP, fill=BOTH)
        self.filename = None

    def AddChannel(self):
        pass

    def removeChannel(self, channelName):
        pass

    def setFilename(self, filename):
        self.recyclerView.clear()

        self.filename = filename
        data = getMidiMetadata(filename)

        for channel in data:
            channelModel = ChannelModel(
                channel["id"],
                channel["name"]
            )
            channelModel.setOnConfigureListener(
                Listener(self.configureChannel, channelModel)
            )
            self.recyclerView.addElement(
                channelModel
            )

    def getFilename(self):
        return self.filename

    def configureChannel(self, channel):

        self.controller.showFrame(ConfigureChannelMenu)
        self.controller.getCurrentFrame().configureChannel(channel)

    def generateMusic(self):
        if self.filename:
            self.controller.showFrame(ProcessMidiMenu)
            self.controller.getCurrentFrame().startLoading(
                SyntetizeConfig(
                    channels=self.recyclerView.getElements(),
                    midiFilename=self.filename
                )
            )


class MidiFileSelector(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        self.buttonSelectFile = tk.Button(
            self,
            height=1,
            width=60,
            text="Seleccionar midi",
            font=config.SMALL_FONT,
            background="#80aaff",
            command=self.searchFile
        )

        self.buttonSelectFile.grid(
            column=0,
            row=0
        )

    def searchFile(self):
        tk.Tk().withdraw()
        self.parent.setFilename(filedialog.askopenfilename())

        self.buttonSelectFile.configure(
            text="Seleccionar midi [" + ntpath.basename(self.parent.getFilename()) + "]"
        )


