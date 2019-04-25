from synthesize_midi import *
from utils import *
import matplotlib.pyplot as plt
import time
fs = 44100
start = time.time()
# track_synthesis = {"channel1":getClarinet,
#                    "channel2":getClarinet,
#                    "channel3":getClarinet,
#                    "channel4":getClarinet,
#                    "channel5":getClarinet,
#                    "channel6":getClarinet,
#                    "channel7":getClarinet,
#                    "channel8":getClarinet,
#                    "channel9":getClarinet,
#                    "channel10":getClarinet,
#                    "channel11":getClarinet,
#                    "channel12":getClarinet}
number_of_tracks = 12
track_synthesis = {}
for i in range(number_of_tracks):
    canal = "channel"+str(i)
    track_synthesis[canal]=getClarinet

name = "Pink_Panther"

t,ytot = synthesize_midi('midi-samples/'+name+'.mid',track_synthesis,fs)
#plt.plot(t,ytot)
#plt.show()

#playSound(ytot)
#sr,x = read('megalovania.mp3',normalized = False)
# print(x)
write(name+'.mp3',fs,ytot,normalized = True)

end = time.time()
print(int(abs(end-start))/60)