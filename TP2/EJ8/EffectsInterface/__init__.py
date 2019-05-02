import subprocess

from threading import Thread
import sys
import os


class EffectsInterface:
    def __init__(self):
        self.thread = Thread(target=self.deamon, args=())
        self.thread.start()

        self.continuar = True

    def deamon(self):
        print("Corriendo EJ8.exe \n")

        self.p = subprocess.Popen(
            "cmake-build-debug\EJ8.exe",
            shell=False,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            bufsize=100
        )
        while self.continuar:
            line = self.p.stdout.readline()
            print(line)

    def end(self):
        print("Ending ...")
        self.continuar = False
        self.p.stdin.write(b'Salir\n')
        self.p.stdin.flush()

    def setMode(self, mode):
        self.p.stdin.write(mode)
        self.p.stdin.flush()

effectsInferface = None


def getEffectsInterface():
    global effectsInferface
    if not effectsInferface:
        effectsInferface = EffectsInterface()

    return effectsInferface