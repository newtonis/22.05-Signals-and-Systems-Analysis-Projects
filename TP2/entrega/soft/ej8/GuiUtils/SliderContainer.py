import tkinter as tk
from Globals import config


class SliderContainer(tk.Frame):
    def __init__(self, parent, model):
        tk.Frame.__init__(self, parent)

        self.model = model
        self.model.setView(self)

        self.slider = tk.Scale(
            self,
            width=15,
            from_=model.start,
            to=model.end,
            resolution=model.step,
            command=self.updateValue,
            orient=tk.HORIZONTAL
        )
        self.title = tk.Label(
            self,
            height=1,
            width=40,
            text=model.getTitle(),
            font=config.SMALL_FONT
        )
        #self.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(1, weight=1)

        self.title.pack(side=tk.TOP, expand=1, fill=tk.X)
        self.slider.pack(side=tk.TOP, expand=1, fill=tk.X)

    def updateValue(self, event):
        self.model.setValue(self.slider.get())

    def refresh(self):
        self.slider.set(self.model.getValue())
