from util_python import read_csv
from Etapas import SignalsReadWrite
from util_python import Senial
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

inputDirectory = "ExpressInput"
outputDirectory = "ExpressOutput"


def csvToSignal(data, field):
    while len(data["x-axis"]) > len(data[field]):
        data["x-axis"].pop()

    senial = Senial.Senial(data["x-axis"], data[field])

    return senial


class CombinedPlot:
    def __init__(self):
        self.plotCount = []

    def setXTitle(self, title):
        self.xAxisTitle = title
        return self

    def setYTitle(self, title):
        self.yAxisTitle = title
        return self

    def addCSVPlot(self, filename, field, name, color):
        data = read_csv.read_csv_bode(inputDirectory + "/" + filename)
        signal = csvToSignal(data, field)

        self.plotCount.append({
            "signal": signal,
            "color": color,
            "name": name
        })

        return self

    def addXMLPlot(self, filename, name, color):
        signal = SignalsReadWrite.readSignal(inputDirectory + "/" + filename)

        self.plotCount.append(
            {
                "signal": signal,
                "color": color,
                "name": name
            }
        )
        return self

    def placeLimits(self):
        if len(self.plotCount) >= 2:
            case1 = self.plotCount[-1]
            case2 = self.plotCount[-2]

            if case1.mode == "teorica":
                teorica = case1
                practica = case2
            else:
                teorica = case2
                practica = case1
            if teorica.xvarEnd:
                practica.setShowStartXvar(teorica.xvarStart)
                teorica.setShowEndXvar(teorica.xvarEnd)

    def plotAndSave(self, filename):
        patches = []


        fig, ax1 = plt.subplots()
        for plot in self.plotCount:
            if plot["signal"].mode == "teorica":
                xvalues, yvalues = plot["signal"].getSamplesFiltered()
            elif plot["signal"].mode == "csv":
                xvalues, yvalues = plot["signal"].getSamplesBetweenLimits()
            else:
                xvalues, yvalues = plot["signal"].xvar, plot["signal"].values

            ax1.plot(
                xvalues,
                yvalues,
                plot["color"]
            )
            patches.append(
                mpatches.Patch(color=plot["color"], label=plot["name"])
            )
        plt.legend(handles=patches)

        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
        plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

        plt.xlabel(self.xAxisTitle)
        plt.ylabel(self.yAxisTitle)

        fig.savefig(outputDirectory + "/" + filename, dpi=300)


def main():
    CombinedPlot()\
        .setXTitle("tiempo (s)")\
        .setYTitle("Tensión (V)")\
        .addXMLPlot(
            filename="Signals/AM_1.0Hz.xml",
            name="Simulación",
            color="blue"
        )\
        .placeLimits()\
        .addCSVPlot(
        filename="Mediciones basicas/med_01.csv",
        name="Medición 1",
        field="B",
        color="orange") \
        .plotAndSave("med01.png")

    #test01.addXMLPlot("ExpressInput/test01.xml")
    #test01.addXLSPlot("ExpressInput/Mediciones basicas/med_01.csv")


main()
