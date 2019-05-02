from GuiUtils.AskFilenameCard import AskFilenameCard
from tkinter import filedialog


class AskFilenameModel:
    def __init__(self):
        self.filename = None
        self.viewClass = AskFilenameCard
        self.view = None

    def setView(self, view):
        self.view = view

    def getViewClass(self):
        return self.viewClass

    def getFilename(self):
        return self.filename

    def setFilename(self, filename):
        self.filename = filename

    def getFilename(self):
        return self.filename
