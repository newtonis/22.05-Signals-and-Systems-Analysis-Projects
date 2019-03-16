import tkinter as tk
from tkinter import filedialog
from PlotMenu import PlotMenu
import ntpath

import config


class ConfigureMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        label = tk.Label(self, height=2, text="Configuración", font=config.LARGE_FONT)
        label.pack(side=tk.TOP, fill=tk.BOTH)

        self.filename = ""

        self.btnText = tk.StringVar()

        self.buttonSelectFile = tk.Button(
            self,
            height=2,
            width=44,
            textvariable=self.btnText,
            background="dodger blue",
            font=config.SMALL_FONT,
            command=self.searchFile
        )
        self.btnText.set("Seleccionar entrada")

        self.buttonSelectFile.pack(side=tk.TOP, fill=tk.BOTH)

        for mode in config.getModes().modesEnabled.keys():
            checkButton = tk.Checkbutton(
                self,
                text=mode,
                variable=config.getModes().modesEnabled[mode],
                height=3,
                width=44,
                font=config.SMALL_FONT,
                background="light yellow"
            )

            checkButton.pack(side=tk.TOP, fill=tk.BOTH)

        self.button = tk.Button(
            self,
            height=2,
            width=44,
            background="pale green",
            text="ACEPTAR",
            font=config.LARGE_FONT,
            command=lambda: self.goToPlotMenu()
        )

        self.button.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def focus(self):
        pass

    def searchFile(self):
        tk.Tk().withdraw()
        config.getModes().setFilename(filedialog.askopenfilename())

        self.btnText.set("Seleccionar entrada ["+ntpath.basename(self.filename)+"]")

    def goToPlotMenu(self):
        self.controller.showFrame(PlotMenu)
