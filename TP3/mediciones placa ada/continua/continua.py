import matplotlib.pyplot as plt
import csv
import matplotlib.patches as mpatches
import numpy as np


filename = "adc.csv"

vin = []
vout = []
bin = []

with open(filename, 'r') as csvfile:
	reader = csv.reader(csvfile)
	next(reader, None)
	for row in reader:
		vin.append(float(row[0]))
		bin.append(float(row[1]))
		vout.append(float(row[2]))


ideal = np.arange(0, 5000, 0.01)

plt.plot(vin, vout, color="green", marker="o")
plt.plot(vin, bin, "orange", marker='o')
plt.plot(ideal, ideal, "blue")


plt.xlabel("Tensión de entrada (mV)")
plt.ylabel("Tensión de salida (mV)")

# pongo una grilla
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

# agregamos patches
patches = [
	mpatches.Patch(color="green", label="Analógica"),
	mpatches.Patch(color="orange", label="Digital"),
	mpatches.Patch(color="blue", label="Ideal")
]
# agregamos leyenda
plt.legend(handles=patches)

# muestro el grafico que prepare
plt.show()

