import tkinter as tk
from Globals import config
from tkinter import filedialog
import os


class AskFilenameCard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.button = tk.Button(
            self,
            height=2,
            width=46,
            text="Rta al impulso []",
            background="#c54dff",
            font=config.SMALL_FONT,
            command=lambda: self.selectFilename()
        )

        self.button.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def selectFilename(self):
        self.controller.setFilename(filedialog.askopenfilename())

        self.button.configure(
            text="Rta al impulso ["+os.path.basename(self.controller.getFilename())+"]"
        )
