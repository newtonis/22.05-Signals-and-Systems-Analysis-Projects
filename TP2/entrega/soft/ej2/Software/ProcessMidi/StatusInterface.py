

class StatusInterface:
    def __init__(self):
        self.loadListener = None
        self.messageListener = None
        self.onCompleteListener = None

    def setLoadListener(self, listener):
        self.loadListener = listener
        return self

    def setMessageListener(self, listener):
        self.messageListener = listener
        return self

    def setOnCompleteListener(self, listener):
        self.onCompleteListener = listener
        return self

    def callOnLoadUpdate(self, percentaje):
        if self.loadListener:
            self.loadListener.onActionWithCustomArgs(percentaje)

    def callOnSynthComplete(self, result):
        if self.onCompleteListener:
            self.onCompleteListener.onActionWithCustomArgs(result)

    def addMessage(self, message):
        if self.messageListener:
            self.messageListener.onActionWithCustomArgs(message)
