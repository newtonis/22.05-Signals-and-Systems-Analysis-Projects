import tkinter as tk
from Globals import config
from GuiUtils.ChannelCard import ChannelCard


class SelectMidiMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        label = tk.Label(
            self,
            height=2,
            text="Seleccionar midi",
            font=config.LARGE_FONT
        )

        label.pack(
            side=tk.TOP,
            expand=1,
            fill="both"
        )

        self.filename = ""
        self.btnText = tk.StringVar()

        self.buttonSelectFile = tk.Button(
            self,
            height=2,
            width=60,
            textvariable=self.btnText,
            background="dodger blue",
            font=config.SMALL_FONT,
            command=self.searchFile
        )

        self.btnText.set("Seleccionar archivo midi")

        self.buttonSelectFile.pack(side=tk.TOP, fill=tk.BOTH)

        self.buttonAceptar = tk.Button(
            self,
            height=1,
            width=44,
            background="pale green",
            text="ACEPTAR",
            font=config.LARGE_FONT,
            command=lambda: self.goToChannelMenu()
        )
        self.buttonAceptar.pack(side=tk.TOP, fill=tk.BOTH)

        channelCard = ChannelCard(self, self)
        channelCard.pack(side=tk.TOP, fill=tk.BOTH)

    def goToChannelMenu(self):
        pass

    def searchFile(self):
        pass
