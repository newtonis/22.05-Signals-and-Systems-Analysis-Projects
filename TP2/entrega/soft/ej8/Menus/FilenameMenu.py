import tkinter as tk
from EffectsInterface import getEffectsInterface
from Globals import config
from tkinter import filedialog
import os


class FilenameMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        self.title = tk.Label(
            self,
            height=1,
            width=44,
            text="Process file",
            font=config.LARGE_FONT,
            background="#ccffd5"
        )

        self.title.pack(side=tk.TOP, expand=1, fill=tk.BOTH)


        buttonFrame = tk.Frame(self)

        self.button1 = tk.Button(
            buttonFrame,
            height=5,
            width=20,
            text="ENTRADA []",
            font=config.SMALL_FONT,
            background="#b8caff",
            command=self.configureInput
        )

        self.button2 = tk.Button(
            buttonFrame,
            height=5,
            width=20,
            text="SALIDA []",
            font=config.SMALL_FONT,
            background="#fff49f",
            command=self.configureOutput
        )

        self.title.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        f = tk.Frame(self)
        f.configure(height=150)
        f.pack(side=tk.TOP, expand=1, fill = tk.X)

        self.button1.pack(side=tk.LEFT, expand=1, fill=tk.X)
        self.button2.pack(side=tk.RIGHT, expand=1, fill=tk.X)
        buttonFrame.pack(side=tk.TOP, expand=1, fill=tk.X)

        self.buttonAceptar = tk.Button(
            self,
            height=1,
            width=34,
            text="Aceptar",
            font=config.LARGE_FONT,
            background="#aeffba",
            command=self.aceptar
        )
        self.buttonAceptar.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
        self.set = False

        self.buttonSalir = tk.Button(
            self,
            height=1,
            width=10,
            text="Salir",
            font=config.LARGE_FONT,
            background="#ffbaae",
            command=self.goBack
        )
        self.buttonSalir.pack(side=tk.LEFT, expand=1, fill= tk.BOTH)

    def focus(self):
        self.title.configure(text="Process file " + getEffectsInterface().getCompleteMode())

    def configureInput(self):
        filename = filedialog.askopenfilename()
        self.input = filename

        self.button1.configure(
            text="entrada [" + os.path.basename(filename) + "]"
        )

    def configureOutput(self):
        filename = filedialog.asksaveasfile(mode='w', defaultextension=".wav").name
        self.output = filename

        self.button2.configure(
            text="salida [" + os.path.basename(filename) + "]"
        )

    def goBack(self):
        getEffectsInterface().sendData("Salir\n")

        from Menus.StartMenu import StartMenu
        self.controller.showFrame(StartMenu)

    def aceptar(self):

        getEffectsInterface().sendData(self.input)
        getEffectsInterface().sendData(self.output)


        self.buttonAceptar.configure(
            text="Cargando ...",
            background="#ffe4a5"
        )
        self.title.configure(text="Cargando ...")
        getEffectsInterface().setFlagAction(
            self.finished
        )

    def finished(self):
        self.title.configure(
            text="Process file"
        )
        self.buttonAceptar.configure(
            text="Aceptar",
            background="#aeffba",
            command=self.aceptar
        )

