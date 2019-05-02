from Utils import notas
from ProcessMidi.InstrumentsSynth import getInstruments
from util_python import soundUtils

from Globals import config

nota = notas.notas["A"][0]
duration = 2


def generateDemoSounds():
    instruments = getInstruments()

    for instrument in instruments.instrumentos:
        print(127, nota, duration, config.fs)
        sound = instrument.getFunction()(
            127,
            nota,
            duration,
            config.fs
        )
        soundUtils.write(
            "ProcessMidi/InstrumentsSynth/DemoSounds/"+instrument.getName()+".mp3",
            config.fs,
            sound,
            True
        )
    print("Sounds written")


generateDemoSounds()
