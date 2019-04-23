from synthesize_midi import *
from utils import *
import matplotlib.pyplot as plt

fs = 44100
track_synthesis = {"channel1":getClarinet}
t,ytot = synthesize_midi("midi-samples/2difnotes.mid",track_synthesis,fs)
#plt.plot(t,ytot)
#plt.show()

#playSound(ytot)
#sr,x = read('megalovania.mp3',normalized = False)
# print(x)
write('output.mp3',fs,ytot,normalized = True)

