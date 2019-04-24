from synthesize_midi import *
from utils import *
import matplotlib.pyplot as plt
import time
fs = 44100
start = time.time()
track_synthesis = {"channel1":getClarinet,"channel2":getBell}
t,ytot = synthesize_midi("midi-samples/pirates.mid",track_synthesis,fs)
#plt.plot(t,ytot)
#plt.show()

#playSound(ytot)
#sr,x = read('megalovania.mp3',normalized = False)
# print(x)
write('output.mp3',fs,ytot,normalized = True)

end = time.time()
print(int(abs(end-start))/60)