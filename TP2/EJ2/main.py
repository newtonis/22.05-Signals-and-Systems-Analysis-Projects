from synthesize_midi import *
from utils import *
import matplotlib.pyplot as plt

fs = 44100
track_synthesis = {"channel1":getBell}
t,ytot = synthesize_midi("midi-samples/2hits16.mid",track_synthesis,fs)
plt.plot(t,ytot)
plt.show()

sr,x = read('megalovania.mp3',normalized = False)
print(x)
write('output.mp3',sr,x,normalized = False)

