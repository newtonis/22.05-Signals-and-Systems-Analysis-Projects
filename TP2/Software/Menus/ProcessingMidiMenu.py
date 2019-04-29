import tkinter as tk
from tkinter import filedialog

from Globals import config
from GuiUtils.RecyclerView import RecyclerView
from GuiUtils.LoadingModel import LoadingModel
from GuiUtils.LoadingContainer import LoadingContainer
from GuiUtils.InfoModel import InfoModel

from util_python import soundUtils

from ProcessMidi.ProcessMidiInterface import getProcessMidiInterface
import os


class ProcessMidiMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            text="Generando canción",
            font=config.LARGE_FONT,
            background="#ccffd5"
        )


        self.title.pack(side=tk.TOP, fill=tk.BOTH)

        self.halfContainer = tk.Frame(self)

        self.recyclerView = RecyclerView(self.halfContainer, self.controller, 390)
        self.recyclerView.setStart(50)
        self.recyclerView.configureSeparation(50)

        tk.Frame(self.halfContainer).grid(column=0, row=0)
        self.recyclerView.grid(column=1, row=0)

        tk.Frame(self.halfContainer).grid(column=2, row=0)

        self.halfContainer.grid_columnconfigure(0, weight=1)
        self.halfContainer.grid_columnconfigure(1, weight=10)
        self.halfContainer.grid_columnconfigure(2, weight=1)

        self.halfContainer.pack(side=tk.TOP, fill=tk.BOTH)

        self.loadingModel = LoadingModel(
            value=0,
            maxValue=100
        )

        self.loadingContainer = LoadingContainer(
            self, self.loadingModel
        )
        self.loadingModel.setContainer(self.loadingContainer)

        self.loadingContainer.pack(side=tk.TOP, fill=tk.BOTH)

        self.buttonProcess = tk.Button(
            self,
            height=1,
            width=50,
            text="Cancelar",
            font=config.SMALL_FONT,
            background="#ff644f"
        )

        self.buttonProcess.pack(side=tk.TOP, fill=tk.BOTH)
        self.loaded = False

    def startLoading(self, configuration):
        self.loaded = False

        self.title.configure(
            text="Generando canción - " + os.path.basename(configuration.getMidiFilename())
        )
        getProcessMidiInterface().setOnMsgArrived(
            self.onMsg
        )
        getProcessMidiInterface().setOnLoadUpdate(
            self.onLoadUpdate
        )
        getProcessMidiInterface().setOnComplete(
            self.onComplete
        )
        getProcessMidiInterface().start(configuration)

    def onMsg(self, message):
        self.recyclerView.addElement(
            InfoModel(message)
        )
        #print("channel configuration: ", configuration)

    def onLoadUpdate(self, percentaje):
        #print("percentaje ", percentaje)
        self.loadingModel.setValue(percentaje)

    def onComplete(self, result):

        self.buttonProcess.configure(
            text="Guardar",
            height=1,
            width=50,
            font=config.SMALL_FONT,
            background="#91ff7e",
            command=lambda: self.save(result)
        )

        self.loaded = True

    def save(self, result):
        filename = filedialog.asksaveasfile(mode='w', defaultextension=".mp3").name
        if filename:
            self.onMsg("Escribiendo " + os.path.basename(filename))
            soundUtils.write(
                filename,
                config.fs,
                result,
                normalized=True
            )
            self.goToSpectogramMenu(filename, result)
        else:
            self.onMsg("Nompre de archivo invalido")

    def goToSpectogramMenu(self, filename, data):
        from Menus.SpectogramMenu import SpectogramMenu
        self.controller.showFrame(SpectogramMenu)

        self.controller.getCurrentFrame().setFilename(os.path.basename(filename))
        self.controller.getCurrentFrame().setMusicData(data)





