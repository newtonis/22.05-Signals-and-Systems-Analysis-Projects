import tkinter as tk
import config


class TickOption(tk.Frame):
    def __init__(self, parent, controller, title, model):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text=title, font=config.SMALL_FONT)
        label.grid(column=0, row=0)


class TickOptionModel(tk.Frame):
    def __init__(self):
        self.ticked = False

    def getTicked(self):
        return self.ticked

    def setTicked(self, ticked):
        self.ticked = ticked
