import tkinter as tk


class SliderContainer(tk.Frame):
    def __init__(self, model):
        self.model = model
        self.slider = tk.Slider(
            self,
            from_=model.start,
            to=model.end,
            tickinterval=model.step,
            command=self.updateValue
        )

        self.slider.pack(side=tk.LEFT, fill=tk.X, expand=1)

    def updateValue(self):
        self.model.setValue(self.slider.get())


