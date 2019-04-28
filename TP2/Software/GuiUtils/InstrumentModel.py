from GuiUtils.InstrumentCard import InstrumentCard


class InstrumentModel:
    def __init__(self, name):
        self.viewClass = InstrumentCard
        self.name = name
        self.enabled = False
        self.onSelectedListener = None
        self.view = None

    def setView(self, view):
        self.view = view

    def getViewClass(self):
        return self.viewClass

    def getInstrumentName(self):
        return self.name

    def enable(self):
        self.enabled = True
        if self.view:
            self.view.enable()

    def disable(self):
        self.enabled = False
        if self.view:
            self.view.disable()

    def getSelected(self):
        return self.selected

    def getOnSelectedListener(self):
        return self.onSelectedListener

    def setOnSelectedListener(self, listener):
        self.onSelectedListener = listener
