import xml.etree.ElementTree as ET
import importlib
import os


class Instrumento:
    def __init__(self, data):
        self.demoSound = data["demoSound"]
        self.name = data["nombre"]

        moduleName = "InstrumentsSynth.Instruments."+os.path.splitext(data["code"])[0]

        self.function = getattr(
            importlib.import_module(moduleName),
            data["function"]
        )

        print("Function ", self.function, "importada con exito")

    def getName(self):
        return self.name

class Instruments:
    def __init__(self):
        self.instrumentos = []
        root = ET.parse('InstrumentsSynth/instrumentos.xml').getroot()

        for instrumento in root:
            self.instrumentos.append(
                Instrumento(
                    {
                        "nombre" : instrumento.attrib["nombre"],
                        "demoSound" : instrumento.attrib["demoSound"],
                        "code" : instrumento.attrib["code"],
                        "function": instrumento.attrib["function"]
                    }
                )
            )

instruments = None


def getInstruments():
    global instruments

    if not instruments:
        instruments = Instruments()

    return instruments