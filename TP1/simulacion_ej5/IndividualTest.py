from IndividualTests.test_subplot_rochi import testsubplot as start
from IndividualTests.subniquist2 import subniquistMediciones
from IndividualTests.joaco_spectrum import joaco_spectrum
from IndividualTests.bodes import makeBodes
from IndividualTests.espectros import spectra_plot

#joaco_spectrum()
#makeBodes()
#start()


# joaco_spectrum()
spectra_plot("ExpressInput/Mediciones/EspectroAM_IN.csv", 0, 10e3)
# spectra_plot("ExpressInput/Mediciones/EspectroAM_ConRF.csv", 0, 10e3)
# spectra_plot("ExpressInput/Mediciones/EspectroAM_SinFR.csv", 0, 10e3)
