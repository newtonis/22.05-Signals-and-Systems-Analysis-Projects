from synthesize_midi import *
from utils import *
import matplotlib.pyplot as plt
import time
fs = 44100
start = time.time()

number_of_tracks = 13
track_synthesis = {}
for i in range(number_of_tracks):
    canal = "channel"+str(i)
    track_synthesis[canal]=getClarinet

name = "The_Pink_Panther"

ytot = synthesize_midi('midi-samples/'+name+'.mid',track_synthesis,fs)
# t = range(len(ytot))
# plt.plot(t,ytot)
# plt.show()
#playSound(ytot)
#sr,x = read('megalovania.mp3',normalized = False)
# print(x)
write(name+'.mp3',fs,ytot,normalized = True)

end = time.time()
print(int(abs(end-start))/60)