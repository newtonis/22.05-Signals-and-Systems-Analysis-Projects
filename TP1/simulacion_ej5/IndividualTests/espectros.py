import csv
import matplotlib.pyplot as plt
from ExpressPlot import ExpressPlot
from util_python import Senial
from Utils import FourierTransform
from Etapas import SignalsReadWrite
import math


def spectra_plot(medcsv, simxml, out, fmax=None):
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
			pmed.append((10 ** (float(row[1])/20))**2)


	#plt.plot(fmed, pmed)
	#plt.show()

	s1 = Senial.Senial(fmed, pmed)
	s_xml = SignalsReadWrite.readSignal(simxml)
	s2 = FourierTransform.fourierTransform(s_xml)
	fsim = []
	psim = []
	for f in s2.xvar:
		if f < 0:
			continue
		if f > fmax:
			break
		fsim.append(f)
		psim.append(s2.values[s2.xvar.index(f)])

	s2.xvar = fsim
	s2.values = psim
	psum = sum(s2.values)
	s2.values = [v/psum*100 for v in s2.values]

	psum = sum(pmed)
	s1.values = [v/psum*100 for v in s1.values]

	ExpressPlot.CombinedPlot()\
	.setTitle(" ")\
	.setXTitle("Frecuencia (Hz)")\
	.setYTitle("Potencia (% de total)")\
	.addSignalPlot(
		signal=s1,
		color="orange",
		name="Medido"
	)\
	.addSignalPlot(
		signal=s2,
		color="blue",
		name="Simulado"
	)\
		.plotAndSave(
		filename=out
	)
	plt.show()

