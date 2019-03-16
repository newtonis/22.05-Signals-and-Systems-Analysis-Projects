import tkinter as tk
import config


class PlotMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Configuración", font=config.LARGE_FONT)
        label.pack(side=tk.TOP, fill=tk.X, expand=1)

        button = tk.Button(self, height=1, width=10, background="light coral", text="ACEPTAR")

        button.pack(side=tk.BOTTOM, fill=tk.BOTH)
