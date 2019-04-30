from synthesize_midi import *
from main_utils import *
#import matplotlib.pyplot as plt
import time
from scipy import signal
from matplotlib import *
from matplotlib.pyplot import *

fs = 44100
start = time.time()

number_of_tracks = 13
track_synthesis = {}
for i in range(number_of_tracks):
    track = "track"+str(i)
    #track_synthesis[canal]=SitetizarGuitarraDistorsion
    track_synthesis[track]=getBrassTone

name = "1note1sec"
ytot = synthesize_midi('midi-samples/'+name+'.mid', track_synthesis, fs)

# t = arange(0,len(ytot)*(1/fs),1/fs)
# f, t, Sxx = signal.spectrogram(ytot, fs)
# pcolormesh(t, f, Sxx)
# ylabel('Frequency [Hz]')
# xlabel('Time [sec]')
# show()

#plt.plot(x,ytot)
#plt.show()
#sr,x = read('funk_study_no_1tpt.wav',normalized = False)

#t = arange(0,len(x)*(1/fs),1/fs)
#plot(t,x)
# t = arange(0,len(ytot)*(1/fs),1/fs)
# plot(t,ytot)
# show()

write('output/'+name+'.mp3', fs, ytot, normalized = True)

end = time.time()
print("se sintetizo en ",int(abs(end-start))/60," minutos")