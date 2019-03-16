import config
import tkinter as tk
from tkinter import *
from ConfigureMenu import ConfigureMenu
from PlotMenu import PlotMenu
import styles

frames = [
    ConfigureMenu,
    PlotMenu
]


class UI(tk.Tk):
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)
        self.protocol('WM_DELETE_WINDOW', self.exitFunction)

        self.resizable(width=False, height=False)
        #self.minsize(width=800)
        #self.maxsize(width=800)

        if config.debug:
            print("Comenzando aplicación principal")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for frame in frames:
            self.frames[frame] = frame(container, self)
            self.frames[frame].grid(row=0, column=0, sticky=E+W+N+S)

        self.showFrame(ConfigureMenu)

        styles.getData().load()

    def showFrame(self, frame):
        self.frames[frame].focus()
        frame = self.frames[frame]
        frame.tkraise()

    def run(self):
        self.mainloop()

    def exitFunction(self):
        self.quit()
        self.destroy()


if __name__ == "__main__":
    UI().run()
