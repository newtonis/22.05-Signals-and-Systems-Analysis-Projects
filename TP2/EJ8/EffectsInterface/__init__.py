import subprocess

from threading import Thread
import sys
import os
from binascii import a2b_uu, crc32


class EffectsInterface:
    def __init__(self):
        self.thread = Thread(target=self.deamon, args=())
        self.thread.start()

        self.continuar = True
        self.mode = None
        self.reverbMode = None
        self.sentData = dict()

    def deamon(self):
        print("Corriendo EJ8.exe \n")

        self.p = subprocess.Popen(
            "cmake-build-debug-mingw\EJ8.exe",
            shell=False,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            bufsize=100
        )
        while self.continuar:
            line = self.p.stdout.readline()
            print(line)

    def end(self):
        #print("Ending ...")
        self.continuar = False
        self.p.stdin.write(b'Salir\n')
        self.p.stdin.flush()

    def setMode(self, mode):
        self.mode = mode
        foo = mode + "\n"
        self.p.stdin.write(bytes(foo, encoding='utf-8'))
        self.p.stdin.flush()

    def setReverbMode(self, mode):
        self.reverbMode = mode
        foo = mode + "\n"
        self.p.stdin.write(bytes(foo, encoding='utf-8'))
        self.p.stdin.flush()

    def getMode(self):
        return self.mode

    def getCompleteMode(self):
        ans = ""
        if self.mode:
            ans += self.mode
        if self.reverbMode:
            ans += " " + self.reverbMode

        return ans

    def sendParam(self, name, value):
        self.sentData[name] = value
        print("Enviando parametro ", name, "con valor ", value)
        foo = str(value) + "\n"

        self.p.stdin.write(bytes(foo, encoding='utf-8'))
        self.p.stdin.flush()

    def sendData(self, value):
        foo = str(value) + "\n"
        self.p.stdin.write(bytes(foo, encoding='utf-8'))
        self.p.stdin.flush()

    def restart(self):

        self.sentData = dict()
        self.reverbMode = None
        self.mode = None

        self.p.stdin.write(b'Restart\n')
        self.p.stdin.flush()


effectsInferface = None


def getEffectsInterface():
    global effectsInferface
    if not effectsInferface:
        effectsInferface = EffectsInterface()

    return effectsInferface