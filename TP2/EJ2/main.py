from synthesize_midi import *
from main_utils import *
import matplotlib.pyplot as plt
import time
fs = 44100
start = time.time()

number_of_tracks = 13
track_synthesis = {}
for i in range(number_of_tracks):
    track = "track"+str(i)
    #track_synthesis[canal]=SitetizarGuitarraDistorsion
    track_synthesis[track]=getClarinet

#name = "Pink_Panther"
       #<--- pesadilla
#name = "RodrigoAdagio_2" <- el que funciona
#name = "RodrigoAdagio"
name = "greenhill"

ytot = synthesize_midi('midi-samples/'+name+'.mid',track_synthesis,fs)

#plt.plot(x,ytot)
#plt.show()
#sr,x = read('megalovania.mp3',normalized = False)

write(name+'.mp3',fs,ytot,normalized = True)

end = time.time()
print("se sintetizo en ",int(abs(end-start))/60," minutos")