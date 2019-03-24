import tkinter as tk
from Globals import config, Modes
from Globals import PlotSignals
from GuiUtils.ButtonSelector import ButtonSelector
from GuiUtils.ButtonSelectorModel import ButtonSelectorModel
from GuiUtils.ButtonModel import ButtonModel
from GuiUtils.PlotContainerTabs import PlotContainerTabs
from Utils import FourierTransform

from Menus import ConfigureMenu


class PlotMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Gráficos", font=config.LARGE_FONT)
        label.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.buttonModel = ButtonSelectorModel()

        self.plotContainerTabs = PlotContainerTabs(self)
        self.plotContainerTabs.pack(side=tk.TOP, fill=tk.BOTH)

        self.buttonSelector = ButtonSelector(
            self,
            self.buttonModel
        )

        self.buttonSelector.pack(side=tk.TOP, fill=tk.X)


        self.returnButton = tk.Button(
            self,
            height=1,
            width=44,
            background="tomato",
            text="VOLVER",
            font=config.SMALL_FONT,
            command=lambda: self.goToConfigureMenu()
        )

        self.returnButton.pack(side=tk.TOP, fill=tk.X)

    def focus(self):
        self.updateButtons()

    def updateButtons(self):
        modesEnabled = Modes.getModes().modesEnabled
        buttons = {}
        buttons["Entrada"] = ButtonModel(
                "Entrada",
                self.modeSelected
        )


        for mode in modesEnabled.keys():
            #print(mode, modesEnabled[mode].get())
            if modesEnabled[mode].get():
                buttons[mode] = ButtonModel(
                    "Salida de " + mode,
                    self.modeSelected
                )

        self.buttonModel.setButtons(buttons)

    def modeSelected(self):
        mode = self.buttonSelector.var.get()

        inputSignal = PlotSignals.getSignalsData().signals[mode]
        self.plotContainerTabs.tab1.plot(inputSignal)
        self.plotContainerTabs.tab2.plot(FourierTransform.fourierTransform(inputSignal))

    def goToConfigureMenu(self):
        self.controller.showFrame(ConfigureMenu.ConfigureMenu)