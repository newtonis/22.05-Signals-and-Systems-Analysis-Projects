import tkinter as tk
from Globals import config
from GuiUtils.SimpleButtonModel import SimpleButtonModel
from GuiUtils.RecyclerView import RecyclerView
from EffectsInterface import getEffectsInterface


class ReverbMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.label = tk.Label(
            self,
            height=1,
            width=44,
            text="Reverberador",
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
            SimpleButtonModel(self.goToEco, "Eco")
        )
        self.recyclerView.addElement(
            SimpleButtonModel(self.goToPlano, "Reverberador plano")
        )
        self.recyclerView.addElement(
            SimpleButtonModel(self.goToPB, "Reverberador pasa bajos")
        )
        self.recyclerView.addElement(
            SimpleButtonModel(self.goToCompleto, "Reverberador completo")
        )
        self.recyclerView.addElement(
            SimpleButtonModel(self.goToConvolucion, "Reverberador de convolución")
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

    def goToEco(self):
        getEffectsInterface().setReverbMode("Eco-simple")
        self.goToConfigMenu()

    def goToPlano(self):
        getEffectsInterface().setReverbMode("Reverberador-plano")
        self.goToConfigMenu()

    def goToPB(self):
        getEffectsInterface().setReverbMode("Revervbrador-pasa-bajos")
        self.goToConfigMenu()

    def goToCompleto(self):
        getEffectsInterface().setReverbMode("Reverberador-completo")
        self.goToConfigMenu()

    def goToConvolucion(self):
        getEffectsInterface().setReverbMode("Reverberador-convolución")
        self.goToConfigMenu()

    def goBack(self):
        getEffectsInterface().restart()
        from Menus.StartMenu import StartMenu
        self.controller.showFrame(StartMenu)

    def goToConfigMenu(self):
        from Menus.ParametersConfigMenu import ParametersConfigMenu
        self.controller.showFrame(ParametersConfigMenu)
