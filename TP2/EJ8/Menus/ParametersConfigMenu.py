import tkinter as tk
from Globals import config
from EffectsInterface import getEffectsInterface
from GuiUtils.RecyclerView import RecyclerView
from GuiUtils.SliderModel import SliderModel
from GuiUtils.SimpleButtonModel import SimpleButtonModel
from GuiUtils.AskFilenameModel import AskFilenameModel


class ParametersConfigMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.mode = getEffectsInterface().getCompleteMode()

        self.label = tk.Label(
            self,
            height=1,
            width=44,
            text="Configuracion de parametros - " + self.mode,
            font=config.LARGE_FONT,
            background="#ccffd5"
        )

        self.label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.halfContainer = tk.Frame(self)

        self.recyclerView = RecyclerView(
            self.halfContainer,
            controller,
            400
        )

        tk.Frame(self.halfContainer).grid(column=0, row=0)
        self.recyclerView.grid(column=1, row=0)
        tk.Frame(self.halfContainer).grid(column=2, row=0)
        self.halfContainer.grid_columnconfigure(0, weight=1)
        self.halfContainer.grid_columnconfigure(1, weight=10)
        self.halfContainer.grid_columnconfigure(2, weight=1)

        self.halfContainer.pack(side=tk.TOP, fill=tk.BOTH)

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

    def configReverbEcoSimple(self):
        self.ganancia = SliderModel(0, 1, 0.001, 0.999, "Ganancia (g)")
        self.recyclerView.addElement(
            self.ganancia
        )
        self.delay = SliderModel(5, 8000, 1, 5000, "Delay (m)")
        self.recyclerView.addElement(
            self.delay
        )
        self.recyclerView.addElement(
            SimpleButtonModel(self.sendParams, "Aceptar")
        )

    def configureReverbPlano(self):
        self.ganancia = SliderModel(0, 1, 0.01, 0.5, "Ganancia (g)")
        self.recyclerView.addElement(
            self.ganancia
        )
        self.delay = SliderModel(5, 8000, 1, 500, "Delay (m)")
        self.recyclerView.addElement(
            self.delay
        )
        self.recyclerView.addElement(
            SimpleButtonModel(self.sendParams, "Aceptar")
        )

    def configReverbPB(self):
        self.ganancia = SliderModel(0, 1, 0.01, 0.5, "Ganancia (g)")
        self.recyclerView.addElement(
            self.ganancia
        )
        self.delay = SliderModel(5, 8000, 1, 500, "Delay (m)")
        self.recyclerView.addElement(
            self.delay
        )
        self.recyclerView.addElement(
            SimpleButtonModel(self.sendParams, "Aceptar")
        )

    def configureReverbCompleto(self):
        self.pFilter = SliderModel(1, 15, 1, 12, "Cantidad de Filtros en paralelo")
        self.recyclerView.addElement(
            self.pFilter
        )
        self.combCount = SliderModel(1, 4, 1, 2, "Cantidad de combs en serie")
        self.recyclerView.addElement(
            self.combCount
        )
        self.combDelay = SliderModel(100, 1000, 1, 500, "Delay combs")
        self.recyclerView.addElement(
            self.combDelay
        )
        self.combGain = SliderModel(0, 1, 0.01, 0.5, "Comb gain")
        self.recyclerView.addElement(
            self.combGain
        )
        self.recyclerView.addElement(
            SimpleButtonModel(self.sendParams, "Aceptar")
        )

    def configureReverbConvolucion(self):
        self.fileImpulse = AskFilenameModel()
        self.recyclerView.addElement(
            self.fileImpulse
        )
        self.recyclerView.addElement(
            SimpleButtonModel(self.sendParams, "Aceptar")
        )

    def configureRobotization(self):
        self.windowWidth = SliderModel(2, 12, 1, 6, "Tamaño de la ventana")
        self.recyclerView.addElement(
            self.windowWidth
        )
        self.recyclerView.addElement(
            SimpleButtonModel(self.sendParams, "Aceptar")
        )

    def configureFlangerOrVibrato(self):
        self.fm = SliderModel(0, 5, 0.01, 2.5, "Frecuencia de modulación (hz)")
        self.recyclerView.addElement(
            self.fm
        )

        self.pm = SliderModel(0, 0.02, 0.001, 0.01, "Profundidad de modulación (s)")
        self.recyclerView.addElement(
            self.pm
        )
        self.recyclerView.addElement(
            SimpleButtonModel(self.sendParams, "Aceptar")
        )

    def focus(self):
        self.recyclerView.clear()

        self.mode = getEffectsInterface().getCompleteMode()
        #print(self.mode)
        if self.mode == "Reverb Eco-simple":
            self.configReverbEcoSimple()
        elif self.mode == "Reverb Reverberador-plano":
            self.configureReverbPlano()
        elif self.mode == "Reverb Reverberador-pasa-bajos":
            self.configReverbPB()
        elif self.mode == "Reverb Reverberador-completo":
            self.configureReverbCompleto()
        elif self.mode == "Reverb Reverberador-convolucion":
            self.configureReverbConvolucion()
        elif self.mode == "Vibrato":
            self.configureFlangerOrVibrato()
        elif self.mode == "Flanger":
            self.configureFlangerOrVibrato()
        elif self.mode == "Robot":
            self.configureRobotization()


        self.label.configure(
            text=self.mode
        )

    def goBack(self):
        getEffectsInterface().sendData("-1\n")
        getEffectsInterface().restart()
        from Menus.StartMenu import StartMenu
        self.controller.showFrame(StartMenu)

    def sendParams(self):

        if self.mode == "Reverb Eco-simple" or \
                self.mode == "Reverb Reverberador-plano" or \
                self.mode == "Reverb Reverberador-pasa-bajos":

            #print("sending ...")
            getEffectsInterface().sendParam("g", self.ganancia.getValue())
            getEffectsInterface().sendParam("d", self.delay.getValue())

        elif self.mode == "Reverb Reverberador-completo":
            getEffectsInterface().sendParam("pf", self.pFilter.getValue())
            getEffectsInterface().sendParam("cc", self.combCount.getValue())
            getEffectsInterface().sendParam("dc", self.combDelay.getValue())
            getEffectsInterface().sendParam("gc", self.combGain.getValue())

        elif self.mode == "Reverb Reverberador-convolucion":
            getEffectsInterface().sendData(self.fileImpulse.getFilename())
        elif self.mode == "Robot":
            getEffectsInterface().sendParam("Ventana",self.windowWidth.getValue())
        elif self.mode == "Flanger" or self.mode == "Vibrato":
            getEffectsInterface().sendParam("fm", self.fm.getValue())
            getEffectsInterface().sendParam("pm", self.pm.getValue())


        from Menus.RealtimeOrFilenameMenu import RealtimeOrFilenameMenu
        self.controller.showFrame(RealtimeOrFilenameMenu)




