import csv
import matplotlib.pyplot as plt
from ExpressPlot import ExpressPlot
from util_python import Senial
from Utils import FourierTransform

def spectra_plot(medcsv, simxml, fmax=None):
	fmed = []
	pmed = []

	with open(medcsv, 'rt') as csvfile:
		reader = list(csv.reader(csvfile))
		# hola = csv.reader(csvfile)

		reader.pop(0) # saco el header, me quedo solo con las mediciones
		if fmax is None:
			fmax = float(reader[-1][0])

		for row in reader:
			f = float(row[0])
			if f > fmax:
				break
			fmed.append(f)
			pmed.append(float(row[1]))


	#plt.plot(fmed, pmed)
	#plt.show()

	s1 = Senial.Senial(fmed, pmed)
	s2 = FourierTransform.fourierTransform(s1)

	ExpressPlot.CombinedPlot()\
	.setTitle("Espectros")\
	.setXTitle("Frecuencia (Hz)")\
	.setYTitle("Potencia (W)")\
	.addSignalPlot(
		signal=s1,
		color="blue",
		name="espectro 1"
	)\
	.addSignalPlot(
		signal=s2,
		color="green",
		name="espectro 2"
	)\
		.plotAndSave(
		filename="ExpressOutput/espectro_rochi.png"
	)
	plt.show()