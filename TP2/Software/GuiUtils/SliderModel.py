

class SliderModel:
    def __init__(self, start, end, step, startValue, title):
        self.value = startValue
        self.start = start
        self.end = end
        self.step = step
        self.title = title
        self.view = None

    def setView(self, view):
        self.view = view

    def getView(self):
        return self.view

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        if self.view:
            self.view.refresh()

    def getTitle(self):
        return self.title
