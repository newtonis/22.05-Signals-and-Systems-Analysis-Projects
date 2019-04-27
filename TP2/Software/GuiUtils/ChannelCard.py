import tkinter as tk
from Globals import config


class ChannelCard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = tk.Label(
            self,
            height=2,
            text="CANAL 1",
            font=config.LARGE_FONT,
            background="sandy brown"
        )
        self.title.pack(side=tk.TOP, fill=tk.BOTH)

        self.content = ContentFrame(self, self)
        self.content.pack(side=tk.TOP, fill=tk.BOTH)


class ContentFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="thistle1")

        self.controller = controller

        self.title = tk.Label(
            self,
            height=2,
            width=20,
            text="FLAUTA",
            font=config.LARGE_FONT,
            background="thistle1"
        )
        self.title.grid(column=0, row=0)

        self.frameButtons = tk.Frame(self)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.buttonPlay = tk.Button(
            self.frameButtons,
            height=1,
            width=30,
            text="Escuchar",
            background="light goldenrod",
            font=config.SMALL_FONT,
            command=self.configure
        )

        self.buttonConfig = tk.Button(
            self.frameButtons,
            height=1,
            width=30,
            text="Configurar",
            background="SteelBlue1",
            font=config.SMALL_FONT,
            command=self.configure
        )

        self.buttonPlay.grid(column=0, row=0)
        self.buttonConfig.grid(column=0, row=1)

        self.frameButtons.grid(column=1, row=0)




