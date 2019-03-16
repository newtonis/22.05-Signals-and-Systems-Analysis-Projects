import tkinter as tk
from tkinter import filedialog
import ntpath

import config

class ConfigureMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, height=2, text="Configuración", font=config.LARGE_FONT)
        label.pack(side=tk.TOP, fill=tk.BOTH)

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
                height=2,
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
            font=config.LARGE_FONT
        )

        self.button.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def searchFile(self):
        tk.Tk().withdraw()
        self.filename = filedialog.askopenfilename()

        self.btnText.set("Seleccionar entrada actual=["+ntpath.basename(self.filename)+"]")
