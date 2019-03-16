import tkinter as tk
import matplotlib.pyplot as plt

LARGE_FONT = ("Bahnschrift", 24)
SMALL_FONT = ("Bahnschrift", 16)
SMALLEST_FONT = ("Bahnschrift", 10)
debug = True


class Modes:
    def __init__(self):
        self.modesEnabled = None
        self.filename = None

    def start(self):
        self.modesEnabled = {
            "FAA": tk.IntVar(),
            "Sample and Hold": tk.IntVar(),
            "LLave Analógica": tk.IntVar(),
            "FR": tk.IntVar()
        }

    def setFilename(self, filename):
        self.filename = filename

    def getFilename(self):
        return self.filename


class AxisData:
    axisData = None

    def __init__(self):
        self.fig, self.axis = plt.subplots()


modes = Modes()


def getModes():
    if not modes.modesEnabled:
        modes.start()
    return modes


def getAxisData():
    if not AxisData.axisData:
        AxisData.axisData = AxisData()
    return AxisData.axisData
