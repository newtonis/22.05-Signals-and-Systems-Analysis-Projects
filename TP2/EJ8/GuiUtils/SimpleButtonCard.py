import tkinter as tk
from Globals import config
from threading import Thread


class SimpleButtonCard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.setView(self)

        self.button = tk.Button(
            self,
            height=2,
            width=46,
            text=self.controller.getText(),
            background="#c5d4ff",
            font=config.SMALL_FONT,
            command=lambda: self.controller.onAction()
        )

        self.button.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
