import tkinter as tk
from Globals import config
from GuiUtils.RecyclerView import RecyclerView
from GuiUtils.LoadingModel import LoadingModel
from GuiUtils.LoadingContainer import LoadingContainer


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

        self.recyclerView = RecyclerView(self.halfContainer, self.controller)

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

    def setChannelConfiguration(self, configuration):
        print("channel configuration: ", configuration)
