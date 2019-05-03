import xml.etree.ElementTree as ET
from GuiUtils.SimpleButtonCard import SimpleButtonCard


class Mode:
    def __init__(self, name, content):
        self.text = name
        self.name = name
        self.content = content
        self.viewClass = SimpleButtonCard
        self.view = None
        self.action = None

    def getView(self):
        return self.view

    def setView(self, view):
        self.view = view

    def getViewClass(self):
        return self.viewClass

    def getContent(self):
        return self.content

    def getText(self):
        return self.text

    def onAction(self):
        if self.action:
            self.action(self)

    def setAction(self, action):
        self.action = action

    def show(self):
        print("Name = ", self.name)
        print("-----------")

        for i in self.content:
            print(i)

        print("-----------")


def ReadPredefined():
    root = ET.parse('PredefinedModes/predefined.xml').getroot()

    modes = []

    for mode in root:
        nombre = mode.attrib["nombre"]
        commands = []
        for command in mode:
            commands.append(command.text)

        modes.append(Mode(nombre, commands))

    for u in modes:
        u.show()

    return modes


modes = None


def getPredefined():
    global modes
    if not modes:
        modes = ReadPredefined()
    return modes

