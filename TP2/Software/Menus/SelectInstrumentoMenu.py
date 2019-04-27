import tkinter as tk
from GuiUtils.ChannelCard import ChannelCard
from tkinter import *


def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))


class SelectInstrumentMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(
            self,
            width=800, height=400,
            borderwidth=5,
            background="#ffffff"
        )

        self.vsb = tk.Scrollbar(
            self,
            orient="vertical",
            command=self.canvas.yview
        )

        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill=tk.BOTH)
        self.vsb.pack(side="right", fill=tk.BOTH)

        self.canvas.pack(side="left", fill=tk.BOTH, expand=True)

        self.channelCard1 = ChannelCard(self.canvas, self.controller)
        self.channelCard2 = ChannelCard(self.canvas, self.controller)
        self.channelCard3 = ChannelCard(self.canvas, self.controller)

        self.w1 = self.canvas.create_window((400, 104), window=self.channelCard1)
        self.w2 = self.canvas.create_window((400, 304), window=self.channelCard2)
        self.w3 = self.canvas.create_window((400, 504), window=self.channelCard3)

        self.window = self.channelCard1.bind(
            "<Configure>",
            lambda event,
            canvas=self.canvas: onFrameConfigure(self.canvas),
        )
        self.channelCard2.bind(
            "<Configure>",
            lambda event,
            canvas=self.canvas: onFrameConfigure(self.canvas),
        )
        self.channelCard3.bind(
            "<Configure>",
            lambda event,
            canvas=self.canvas: onFrameConfigure(self.canvas),
        )
        #self.canvas.bind("<Configure>", self.onCanvasConfigure)

    def AddChannel(self):
        pass

    def removeChannel(self, channelName):
        pass

    #def onCanvasConfigure(self, event):
    #    self.canvas.itemconfig(self.window, width = 700)
