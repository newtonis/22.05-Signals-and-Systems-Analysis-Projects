from Etapas import SampleAndHold, LlaveAnalogica, SignalsReadWrite
from Globals import config
from util_python import Senial
from matplotlib import pyplot as plt
import numpy as np


def testsubplot():
	s_in = SignalsReadWrite.readSignal("Signals/Coseno_0.5k_2Vp.xml")

	config.GetConfigData().setFs(4000)
	config.GetConfigData().setSampleCycle(50)
	s_sh = SampleAndHold.getSampleAndHold().processInput(
		s_in,
		None,
		1
	)

	s_out = LlaveAnalogica.getLlaveAnalogica().processInput(
		s_sh,
		None,
		1
	)

	f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
	ax1.plot(s_in.xvar, s_in.values)
	# ax1.set_title('Sharing both axes')
	ax2.plot(s_sh.xvar, s_sh.values)
	ax3.plot(s_out.xvar, s_out.values)
	# Fine-tune figure; make subplots close to each other and hide x ticks for
	# all but bottom plot.
	f.subplots_adjust(hspace=0)
	plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
	ticks = np.arange(0, 0.00401, 0.0005/4)
	#ticks = ticks + [ticks[1]+ticks[-1]]
	ax1.xaxis.set_ticks(ticks, minor=True)
	ax2.xaxis.set_ticks(ticks, minor=True)
	ax3.xaxis.set_ticks(ticks, minor=True)

	ax1.grid(axis='x', which='major', linestyle='-', linewidth=0.3, color='black')
	ax1.grid(axis='x', which='minor', linestyle=':', linewidth=0.1, color='black')
	ax2.grid(axis='x', which='major', linestyle='-', linewidth=0.3, color='black')
	ax2.grid(axis='x', which='minor', linestyle=':', linewidth=0.1, color='black')
	ax3.grid(axis='x', which='major', linestyle='-', linewidth=0.3, color='black')
	ax3.grid(axis='x', which='minor', linestyle=':', linewidth=0.1, color='black')
	plt.show()



