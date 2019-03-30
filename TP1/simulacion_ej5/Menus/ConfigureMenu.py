import tkinter as tk
from tkinter import filedialog
from Menus.PlotMenu import PlotMenu
from GuiUtils.SliderContainer import SliderContainer
from GuiUtils.SliderModel import SliderModel
from Globals import Modes
import ntpath
from Etapas import ProcessSignals
from Globals import config


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

        self.slider1 = SliderModel(1, 2000, 5, config.GetConfigData().FAAfreq, "Sample rate (hz)")
        SliderContainer(self, self.slider1).pack(side=tk.TOP, fill=tk.BOTH)

        self.slider2 = SliderModel(2, 98, 1, config.GetConfigData().FAAfreq, "Sample cycle (%)")
        SliderContainer(self, self.slider2).pack(side=tk.TOP, fill=tk.BOTH)

        self.buttonSelectFile.pack(side=tk.TOP, fill=tk.BOTH)

        for mode in Modes.getModes().modesEnabled.keys():
            checkButton = tk.Checkbutton(
                self,
                text=mode,
                variable=Modes.getModes().modesEnabled[mode],
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
        Modes.getModes().setFilename(filedialog.askopenfilename())

        self.btnText.set("Seleccionar entrada [" + ntpath.basename(Modes.getModes().getFilename()) + "]")

    def goToPlotMenu(self):
        if Modes.getModes().getFilename():
            ProcessSignals.processSignals(Modes.getModes().getFilename(), Modes.getModes().modesEnabled)
            self.controller.showFrame(PlotMenu)

            config.GetConfigData().setSRate(self.slider1.getValue())
            config.GetConfigData().setSampleTime(self.slider2.getValue())

            config.GetConfigData().save()
