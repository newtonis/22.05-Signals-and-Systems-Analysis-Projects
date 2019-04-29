import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import matplotlib.pyplot as plt
from tkinter import *
from Globals import config
from scipy import signal


class SpectogramMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        self.graph = Canvas(
            self,
            width=600
        )

        self.fig, self.axis = plt.subplots()

        self.fig.set_size_inches(5, 4)

        self.dataPlot = FigureCanvasTkAgg(self.fig, master=self.graph)
        # self.dataPlot.draw(self)

        self.nav = NavigationToolbar2Tk(self.dataPlot, self.graph)

        self.dataPlot._tkcanvas.pack(side=BOTTOM, fill=X, expand=1)

        self.title = tk.Label(
            self,
            height=1,
            text="Espectograma",
            font=config.LARGE_FONT,
            background="#ccffd5"
        )
        self.title.pack(side=TOP, expand=1, fill=BOTH)

        self.graph.pack(side=TOP, expand=1, fill=X)

        self.backButton = tk.Button(
            self,
            height=1,
            width=50,
            text="Volver a empezar",
            font=config.SMALL_FONT,
            background="#ff644f",
            command=self.goBack
        )

        self.backButton.pack(side=TOP, expand=1, fill=BOTH)

        self.playing = False

    def setFilename(self, name):
        self.title.configure(
            text="Espectograma - " + name
        )

    def setMusicData(self, content):
        print("setting music data")

        self.content = content
        f, t, Sxx = signal.spectrogram(content, config.fs)

        self.axis.clear()

        self.axis.pcolormesh(t, f, Sxx)
        self.axis.set_xlabel('Frecuencia [Hz]')
        self.axis.set_xlabel('Tiempo [sec]')

        self.dataPlot.draw()

    def goBack(self):
        from Menus.MidiConfigMenu import MidiConfigMenu
        self.controller.showFrame(MidiConfigMenu)
