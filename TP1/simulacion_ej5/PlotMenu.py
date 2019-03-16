import tkinter as tk
import config
from ButtonSelector import ButtonSelector
from ButtonSelectorModel import ButtonSelectorModel
from ButtonModel import ButtonModel
from PlotContainerTabs import PlotContainerTabs
import ConfigureMenu


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
        modesEnabled = config.getModes().modesEnabled
        buttons = {}
        buttons["Entrada"] = ButtonModel(
                "Entrada",
                self.modeSelected("Entrada"
            )
        )

        for mode in modesEnabled.keys():
            if modesEnabled[mode].get():
                buttons[mode] = ButtonModel(
                    "Salida de " + mode,
                    lambda: self.modeSelected(mode)
                )

        self.buttonModel.setButtons(buttons)




    def modeSelected(self, mode):
        print("Mode selected: ", mode)

    def goToConfigureMenu(self):
        self.controller.showFrame(ConfigureMenu.ConfigureMenu)
