import tkinter as tk
from EffectsInterface import getEffectsInterface
from Globals import config


class RealtimeMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        self.playing = False

        self.title = tk.Label(
            self,
            height=1,
            width=44,
            text="Realtime",
            font=config.LARGE_FONT,
            background="#ccffd5"
        )
        self.title.pack(side=tk.TOP, expand=1, fill=tk.BOTH)

        buttonFrame = tk.Frame(self)

        self.button1 = tk.Button(
            buttonFrame,
            height=5,
            width=20,
            text="PLAY",
            font=config.SMALL_FONT,
            background="#b8caff",
            command=self.play
        )

        self.button2 = tk.Button(
            buttonFrame,
            height=5,
            width=20,
            text="STOP",
            font=config.SMALL_FONT,
            background="#fff49f",
            command=self.stop
        )

        self.title.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        f = tk.Frame(self)
        f.configure(height=200)
        f.pack(side=tk.TOP, expand=1, fill = tk.X)

        self.button1.pack(side=tk.LEFT, expand=1, fill=tk.X)
        self.button2.pack(side=tk.RIGHT, expand=1, fill=tk.X)
        buttonFrame.pack(side=tk.TOP, expand=1, fill=tk.X)

        # f = tk.Frame(self)
        # f.configure(height=100)
        # f.pack(side=tk.TOP, expand=1, fill = tk.X)
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
        self.title.configure(
            text="Realtime " + getEffectsInterface().getCompleteMode()
        )
        getEffectsInterface().sendData("Wait")

    def play(self):
        if not self.playing:
            self.playing = True
            getEffectsInterface().sendData("Play")

    def stop(self):
        if self.playing:
            self.playing = False
            getEffectsInterface().sendData("Wait")

    def goBack(self):
        self.playing = False
        getEffectsInterface().sendData("Exit")

        getEffectsInterface().restart()
        from Menus.StartMenu import StartMenu
        self.controller.showFrame(StartMenu)
