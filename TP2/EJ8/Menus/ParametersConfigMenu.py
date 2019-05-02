import tkinter as tk
from Globals import config
from EffectsInterface import getEffectsInterface
from GuiUtils.RecyclerView import RecyclerView
from GuiUtils.SliderModel import SliderModel
from GuiUtils.SimpleButtonModel import SimpleButtonModel


class ParametersConfigMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.mode = getEffectsInterface().getCompleteMode()

        self.label = tk.Label(
            self,
            height=1,
            width=44,
            text="Configuracion de parametros - " + self.mode,
            font=config.LARGE_FONT,
            background="#ccffd5"
        )

        self.label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.halfContainer = tk.Frame(self)

        self.recyclerView = RecyclerView(
            self.halfContainer,
            controller,
            400
        )

        tk.Frame(self.halfContainer).grid(column=0, row=0)
        self.recyclerView.grid(column=1, row=0)
        tk.Frame(self.halfContainer).grid(column=2, row=0)
        self.halfContainer.grid_columnconfigure(0, weight=1)
        self.halfContainer.grid_columnconfigure(1, weight=10)
        self.halfContainer.grid_columnconfigure(2, weight=1)

        self.halfContainer.pack(side=tk.TOP, fill=tk.BOTH)

        self.buttonVolver = tk.Button(
            self,
            height=1,
            width=44,
            text="Volver",
            font=config.LARGE_FONT,
            background="#ffbaae",
            command=self.goBack
        )
        self.buttonVolver.pack(side=tk.TOP, expand=1, fill=tk.BOTH)

    def configReverbEcoSimple(self):
        self.ganancia = SliderModel(0, 1, 0.01, 0.9, "Ganancia (g)")
        self.recyclerView.addElement(
            self.ganancia
        )
        self.delay = SliderModel(5, 8000, 1, 0.9, "Delay (m)")
        self.recyclerView.addElement(
            self.delay
        )
        self.recyclerView.addElement(
            SimpleButtonModel(self.sendParams, "Aceptar")
        )

    def focus(self):
        self.recyclerView.clear()

        self.mode = getEffectsInterface().getCompleteMode()
        if self.mode == "Reverb Eco-simple":
            self.configReverbEcoSimple()

        self.label.configure(
            text="Configuracion de parametros - " + self.mode
        )

    def goBack(self):
        getEffectsInterface().restart()
        from Menus.StartMenu import StartMenu
        self.controller.showFrame(StartMenu)

    def sendParams(self):

        if self.mode == "Reverb Eco-simple":
            print("sending ...")
            getEffectsInterface().sendParam("g", self.ganancia.getValue())
            getEffectsInterface().sendParam("d", self.delay.getValue())

        from Menus.RealtimeOrFilenameMenu import RealtimeOrFilenameMenu
        self.controller.showFrame(RealtimeOrFilenameMenu)




