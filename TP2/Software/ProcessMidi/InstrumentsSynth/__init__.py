import xml.etree.ElementTree as ET
import importlib
import os
from util_python.soundUtils import read
from Globals import config


class Instrumento:
    def __init__(self, data):
        self.name = data["nombre"]

        moduleName = "ProcessMidi.InstrumentsSynth.Instruments."+os.path.splitext(data["code"])[0]

        self.function = getattr(
            importlib.import_module(moduleName),
            data["function"]
        )
        self.sound = []

        try:
            fs, x = read(
                "ProcessMidi/InstrumentsSynth/DemoSounds/"+self.name+".mp3",
                config.fs
            )
            if fs != config.fs:
                print("Error invalid fs=", fs)
                print("Only 44.1 kHz allowed")
            else:
                self.sound = x

        except:
            print("No demo sound for ", self.name)
            print("Hint: run generateDemoSounds.py")


        #print("Function ", self.function, "importada con exito")

    def getName(self):
        return self.name

    def getFunction(self):
        return self.function

    def getSound(self):
        return self.sound


class Instruments:
    def __init__(self):
        self.instrumentos = []
        root = ET.parse('ProcessMidi/InstrumentsSynth/instrumentos.xml').getroot()

        for instrumento in root:
            self.instrumentos.append(
                Instrumento(
                    {
                        "nombre" : instrumento.attrib["nombre"],
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
