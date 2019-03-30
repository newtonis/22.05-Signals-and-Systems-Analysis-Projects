from util_python import read_csv
from Etapas import SignalsReadWrite
from util_python import Senial


def csvToSignal(data):
    pass
    #senial = Senial(data[""], data[""])


class CombinedPlot:
    def __init__(self):
        self.plotCount = []

    def addXLSPlot(self, filename):
        data = read_csv.read_csv_bode(filename)
        csvToSignal(data)

    def addXMLPlot(self, filename):
        signal = SignalsReadWrite.readSignal(filename)


class GraficosExpress:
    def __init__(self):
        pass

    def load(self, filename1, filename2):
        pass


graficosExpress = GraficosExpress()


def main():
    test01 = CombinedPlot()
    #test01.addXMLPlot("ExpressInput/test01.xml")
    test01.addXLSPlot("ExpressInput/Mediciones basicas/med_01.csv")


main()
