import tkinter as tk
from Globals import config
from EffectsInterface import getEffectsInterface


class RealtimeOrFilenameMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        self.title = tk.Label(
            self,
            height=1,
            width=44,
            text="Modo de funcionamiento",
            font=config.LARGE_FONT,
            background="#ccffd5"
        )


        buttonFrame = tk.Frame(self)

        self.button1 = tk.Button(
            buttonFrame,
            height=5,
            width=20,
            text="REALTIME",
            font=config.SMALL_FONT,
            background="#b8caff",
            command=self.realtime
        )

        self.button2 = tk.Button(
            buttonFrame,
            height=5,
            width=20,
            text="CON ARCHIVOS",
            font=config.SMALL_FONT,
            background="#fff49f",
            command=self.file
        )

        self.title.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        f = tk.Frame(self)
        f.configure(height=200)
        f.pack(side=tk.TOP, expand=1, fill = tk.X)

        self.button1.pack(side=tk.LEFT, expand=1, fill=tk.X)
        self.button2.pack(side=tk.RIGHT, expand=1, fill=tk.X)
        buttonFrame.pack(side=tk.TOP, expand=1, fill=tk.X)

        f = tk.Frame(self)
        f.configure(height=100)
        f.pack(side=tk.TOP, expand=1, fill = tk.X)

    def file(self):
        getEffectsInterface().sendParam("Funcionamiento", "Filename")
        from Menus.FilenameMenu import FilenameMenu
        self.controller.showFrame(FilenameMenu)

    def realtime(self):
        getEffectsInterface().sendParam("Funcionamiento", "Realtime")
        from Menus.RealtimeMenu import RealtimeMenu
        self.controller.showFrame(RealtimeMenu)

    def goBack(self):
        getEffectsInterface().restart()
        from Menus.StartMenu import StartMenu
        self.controller.showFrame(StartMenu)
