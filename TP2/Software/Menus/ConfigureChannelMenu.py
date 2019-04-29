import tkinter as tk
from Globals import config

from GuiUtils.RecyclerView import RecyclerView
from GuiUtils.InstrumentModel import InstrumentModel
from GuiUtils.Listener import Listener
from GuiUtils.SliderContainer import SliderContainer
from GuiUtils.SliderModel import SliderModel

from ProcessMidi.InstrumentsSynth import getInstruments


class ConfigureChannelMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.channel = None

        self.title = tk.Label(
            self,
            height=1,
            text="Configuración del canal X",
            font=config.LARGE_FONT,
            background="#ccffd5"
        )

        self.title.pack(side=tk.TOP, fill=tk.BOTH)

        self.selectedText = tk.Label(
            self,
            height=1,
            text="Ningún instrumento seleccionado",
            font=config.SMALL_FONT,
            background="#80aaff"
        )

        self.selectedText.pack(side=tk.TOP, fill=tk.BOTH)

        self.halfContainer = tk.Frame(self)
        self.recyclerView = RecyclerView(self.halfContainer, self.controller, height=360)

        tk.Frame(self.halfContainer).grid(column=0, row=0)
        self.recyclerView.grid(column=1, row=0)
        tk.Frame(self.halfContainer).grid(column=2, row=0)

        self.recyclerView.configureSeparation(70)

        self.halfContainer.grid_columnconfigure(0, weight=1)
        self.halfContainer.grid_columnconfigure(1, weight=10)
        self.halfContainer.grid_columnconfigure(2, weight=1)

        self.halfContainer.pack(side=tk.TOP, fill=tk.BOTH)

        self.sliderModel = SliderModel(
            start=0,
            end=100,
            step=1,
            startValue=0,
            title="Volumen",
            callOnChange=self.callOnChanged
        )

        self.volumeBar = SliderContainer(
            self,
            self.sliderModel
        )
        self.volumeBar.pack(side=tk.TOP, fill=tk.BOTH)

        self.buttonAceptar = tk.Button(
            self,
            height=1,
            width=50,
            text="Aceptar",
            font=config.LARGE_FONT,
            background="#ccffd5",
            command=self.aceptar
        )

        self.buttonAceptar.pack(side=tk.TOP, fill=tk.BOTH)

        self.updateInstruments()
        self.selectedInstrument = None

    def callOnChanged(self, value):
        for element in self.recyclerView.getElements():
            element.setVolume(value)

    def configureChannel(self, channel):
        self.title.configure(
            text="Configuración del canal "+channel.getName()
        )
        self.sliderModel.setValue(
            channel.getVolume()
        )
        self.instrumentSelected(
            channel.getInstrumento()
        )
        self.channel = channel

    def updateInstruments(self):
        self.recyclerView.clear()

        for instrument in getInstruments().instrumentos:
            instrumentModel = InstrumentModel(
                instrument.getName()
            )
            instrumentModel.setInstrumentData(
                instrument
            )
            instrumentModel.setOnSelectedListener(
                Listener(
                    self.instrumentSelected,
                    instrumentModel
                )
            )

            self.recyclerView.addElement(
                instrumentModel
            )

    def instrumentSelected(self, instrumentModel):
        #print("Instrumento seleccionado ", instrumentModel)
        if instrumentModel:
            self.selectedText.configure(
                text="El instrumento " + instrumentModel.getInstrumentName() + " ha sido seleccionado"
            )
        else:
            self.selectedText.configure(
                text="Ningún instrumento seleccionado"
            )

        for instrument in self.recyclerView.getElements():
            if instrument == instrumentModel:
                instrument.enable()
                self.selectedInstrument = instrument
            else:
                instrument.disable()

    def aceptar(self):
        self.channel.setVolume(self.sliderModel.getValue())
        if self.selectedInstrument:
            self.channel.setInstrumento(
                self.selectedInstrument
            )
            self.channel.setVolume(
                self.sliderModel.getValue()
            )

        from Menus.MidiConfigMenu import MidiConfigMenu

        self.controller.showFrame(MidiConfigMenu)
