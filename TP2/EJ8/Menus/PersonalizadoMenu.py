import tkinter as tk
from Globals import config
from EffectsInterface import getEffectsInterface
from GuiUtils.RecyclerView import RecyclerView
from GuiUtils.SimpleButtonModel import SimpleButtonModel
from EffectsInterface import getEffectsInterface


class PersonalizadoMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.label = tk.Label(
            self,
            height=1,
            width=44,
            text="Efecto personalizado",
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

        self.recyclerView.addElement(
            SimpleButtonModel(self.goToReverberador, "Reverberador")
        )
        self.recyclerView.addElement(
            SimpleButtonModel(self.goToRobotizacion, "Robotización")
        )
        self.recyclerView.addElement(
            SimpleButtonModel(self.goToFlanger, "Flanger")
        )
        self.recyclerView.addElement(
            SimpleButtonModel(self.goToVibrato, "Vibrato")
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

    def focus(self):
        pass

    def goToReverberador(self):
        getEffectsInterface().setMode("Reverb")
        from Menus.ReverbMenu import ReverbMenu
        self.controller.showFrame(ReverbMenu)

    def goToRobotizacion(self):
        getEffectsInterface().setMode("Robot")
        from Menus.ParametersConfigMenu import ParametersConfigMenu
        self.controller.showFrame(ParametersConfigMenu)

    def goToVibrato(self):
        getEffectsInterface().setMode("Vibrato")
        from Menus.ParametersConfigMenu import ParametersConfigMenu
        self.controller.showFrame(ParametersConfigMenu)

    def goToFlanger(self):
        getEffectsInterface().setMode("Flanger")
        from Menus.ParametersConfigMenu import ParametersConfigMenu
        self.controller.showFrame(ParametersConfigMenu)

    def goBack(self):
        getEffectsInterface().restart()
        from Menus.StartMenu import StartMenu
        self.controller.showFrame(StartMenu)
