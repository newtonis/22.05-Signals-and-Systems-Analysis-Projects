from synthesize_midi import *
from main_utils import *
#import matplotlib.pyplot as plt
import time
from scipy import signal
from matplotlib import *
from matplotlib.pyplot import *

fs = 44100


number_of_tracks = 13
track_synthesis = {}
for i in range(number_of_tracks):
    track = "track"+str(i)
    #track_synthesis[canal]=SitetizarGuitarraDistorsion
    track_synthesis[track]=getClarinet

name = "RodrigoAdagio_2"
ytot = synthesize_midi('midi-samples/'+name+'.mid', track_synthesis, fs)
write('output/'+name+'.mp3', fs, ytot, normalized = True)