

class SliderModel:
    def __init__(self, start, end, step, startValue):
        self.value = startValue
        self.start = start
        self.end = end
        self.step = step

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
