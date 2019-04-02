from Etapas import SampleAndHold, LlaveAnalogica, SignalsReadWrite
from Globals import config
from util_python import Senial
from matplotlib import pyplot as plt


def testsubplot():
	s_in = SignalsReadWrite.readSignal("Signals\Coseno_0.5k_1Vp.xml")

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

	plt.plot(s_out.xvar, s_out.values)
	plt.show()


