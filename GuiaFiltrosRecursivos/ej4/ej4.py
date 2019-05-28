from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from math import exp

pi = np.pi

ws = 40
Ts = 2*pi/ws

e6 = exp(-6*Ts)
e4 = exp(-4*Ts)
e2 = exp(-2*Ts)
e12 = exp(-(1/2)*Ts)
e92 = exp(-(9/2)*Ts)

# EJERCICIO A
cont = signal.TransferFunction([8], [1, 6, 8])
disc = signal.dlti(
	[4*(exp(-2*Ts)-exp(-4*Ts)), 0],
	[1, -exp(-2*Ts)-exp(-4*Ts), exp(-6*Ts)],
	dt=Ts
)


# # EJERCICIO B
# cont = signal.TransferFunction([8], [1, 6, 8, 0])
# disc = signal.dlti(
# 	[1+e4-2*e2, e2-2*e4+e6, 0],
# 	[1, -(1+e2+e4), e6+e4+e2, -e6],
# 	dt=Ts
# )

# # EJERCICIO C
# cont = signal.TransferFunction([1, 1], [1 , 4.5, 2])
# disc = signal.dlti(
# 	[1, -(e4+6*e12)/7, 0],
# 	[1, -(e12+e4), e92],
# 	dt=Ts
# )

t_disc, imp_disc = disc.impulse()
imp_disc = np.squeeze(imp_disc)
t_cont, imp_cont = signal.impulse(cont)

t2_disc, s_disc = disc.step()
s_disc = np.squeeze(s_disc)
t2_cont, s_cont = signal.step(cont)

w_disc, mag_disc, phase_disc = disc.bode()
w_cont, mag_cont, phase_cont = signal.bode(cont, w_disc)


# plt.plot(t_disc, imp_disc)
# plt.plot(t_cont, imp_cont)
# plt.show()
#
# plt.plot(t2_disc, s_disc)
# plt.plot(t2_cont, s_cont)
# plt.show()
#
# plt.semilogx(w_disc, mag_disc)
# plt.semilogx(w_cont, mag_cont)
# plt.show()

f_disc = [2*pi*w for w in w_disc]
f_cont = [2*pi*w for w in w_cont]

plt.figure(num=1, figsize=(10, 5), dpi=80, facecolor='w', edgecolor='k')
plt.semilogx(f_disc, mag_disc, "green")
plt.semilogx(f_cont, mag_cont, "orange")

plt.ylabel("|H(f)| [dB]")
plt.xlabel("Frecuencia [Hz]")

# pongo una grilla
#plt.xlim(f_disc[0], f_disc[-1])
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')


# agregamos patches
patches = [
	mpatches.Patch(color="green", label="Filtro digital"),
	mpatches.Patch(color="orange" , label="Filtro analógico")
]
# agregamos leyenda
plt.legend(handles=patches)

# muestro el grafico que prepare
plt.show()