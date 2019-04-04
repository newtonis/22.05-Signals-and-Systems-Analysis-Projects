from IndividualTests.test_subplot_rochi import testsubplot as start
from IndividualTests.subniquist2 import subniquistMediciones
from IndividualTests.joaco_spectrum import joaco_spectrum
from IndividualTests.sub_niquist1 import subniquistTest
from IndividualTests.joaco_spectrum_2 import joaco_spectrum2
from IndividualTests.bodes import makeBodes
from IndividualTests.espectros import spectra_plot

#joaco_spectrum()
#makeBodes()
#start()
<<<<<<< HEAD
#<<<<<<< HEAD
#subniquistTest()
#=======


# joaco_spectrum()
#spectra_plot("ExpressInput/Mediciones/EspectroAM_IN.csv", 0, 10e3)
# spectra_plot("ExpressInput/Mediciones/EspectroAM_ConRF.csv", 0, 10e3)
# spectra_plot("ExpressInput/Mediciones/EspectroAM_SinFR.csv", 0, 10e3)
#>>>>>>> 9b51456fd0733f943ba9c7b64e1d82e319348978

joaco_spectrum2()
=======
#subniquistTest()



# joaco_spectrum()
spectra_plot("ExpressInput/Mediciones/EspectroAM_IN.csv", "ExpressInput/espectro_in.xml", "7_in", 2e3)
spectra_plot("ExpressInput/Mediciones/EspectroAM_SinFR.csv", "ExpressInput/espectro_llave.xml", "7_llave", 10e3)
spectra_plot("ExpressInput/Mediciones/EspectroAM_ConRF.csv", "ExpressInput/espectro_fr.xml", "7_out", 2e3)
>>>>>>> 6c07272332f8eecd6fc12056032b4c70aec631d6
