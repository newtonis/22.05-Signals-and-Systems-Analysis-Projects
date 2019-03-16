import tkinter as tk

LARGE_FONT = ("Bahnschrift", 24)
SMALL_FONT = ("Bahnschrift", 16)


class Modes:
    def __init__(self):
        self.modesEnabled = None

    def start(self):
        self.modesEnabled = {
            "FAA": tk.IntVar(),
            "Sample and Hold": tk.IntVar(),
            "LLave Analógica": tk.IntVar(),
            "FR": tk.IntVar()
        }


modes = Modes()


def getModes():
    if not modes.modesEnabled:
        modes.start()
    return modes


debug = True
