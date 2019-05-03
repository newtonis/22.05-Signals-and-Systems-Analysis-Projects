from GuiUtils.SimpleButtonCard import SimpleButtonCard


class SimpleButtonModel:
    def __init__(self, action, text):
        self.viewClass = SimpleButtonCard
        self.action = action
        self.text = text
        self.view = None

    def setView(self, view):
        self.view = view

    def getViewClass(self):
        return self.viewClass

    def onAction(self):
        self.action()

    def getText(self):
        return self.text
