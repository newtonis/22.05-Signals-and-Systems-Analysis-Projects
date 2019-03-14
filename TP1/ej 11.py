import matplotlib.pyplot as plt
import numpy as np
from math import cos, pi, log
import datacursor_easy

f = np.logspace(0, 3, 10000)

H= [ 20*log( (0.4/(1+0.4**2-0.8*cos(2*pi*fi*1/1000))**(1/2)) ) for fi in f]

print (H)

plt.semilogx(f, H)
plt.xlabel('Hz')
plt.ylabel('dB')
plt.title('Respuesta en frecuencia')
#plt.show()

datacursor_easy.make_datacursor("mag", "output/gananciaDb.png", plt, plt.gcf())
