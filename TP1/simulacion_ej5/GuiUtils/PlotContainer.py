import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import matplotlib.pyplot as plt
from tkinter import *


class PlotContainer(tk.Frame):
    def __init__(self, tabControl):
        super(PlotContainer, self).__init__(tabControl)

        self.graph = Canvas(self)

        self.fig, self.axis = plt.subplots()
        self.dataPlot = FigureCanvasTkAgg(self.fig, master=self.graph)
        #self.dataPlot.draw(self)

        self.nav = NavigationToolbar2Tk(self.dataPlot, self.graph)

        #self.dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.dataPlot._tkcanvas.pack(side=BOTTOM, fill=X, expand=1)

        self.graph.pack(side=TOP, expand=1, fill=BOTH)

    def plot(self, signal):
        self.axis.plot(signal.time, signal.values)

        self.dataPlot.draw()
