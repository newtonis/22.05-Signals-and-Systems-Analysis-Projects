import tkinter as tk
from Globals import config
from GuiUtils.RecyclerView import RecyclerView
from PredefinedModes import getPredefined
from EffectsInterface import getEffectsInterface


class PredefinidoMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.label = tk.Label(
            self,
            height=1,
            width=44,
            text="Sonido predefinido",
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
        self.populate()

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

    def goBack(self):
        from Menus.StartMenu import StartMenu
        self.controller.showFrame(StartMenu)

    def populate(self):
        for mode in getPredefined():
            mode.setAction(
                self.enterPredefined
            )
            self.recyclerView.addElement(mode)

    def enterPredefined(self, mode):
        getEffectsInterface().runCommands(mode.content)
        from Menus.RealtimeOrFilenameMenu import RealtimeOrFilenameMenu

        self.controller.showFrame(RealtimeOrFilenameMenu)
