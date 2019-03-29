

class SliderModel:
    def __init__(self, start, end, step, startValue, title):
        self.value = startValue
        self.start = start
        self.end = end
        self.step = step
        self.title = title

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getTitle(self):
        return self.title
