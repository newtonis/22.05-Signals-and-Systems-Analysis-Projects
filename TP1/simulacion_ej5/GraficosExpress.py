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
        self.title = ""

    def setTitle(self, title):
        self.title = title
        return self

    def setXTitle(self, title):
        self.xAxisTitle = title
        return self

    def setYTitle(self, title):
        self.yAxisTitle = title
        return self

    def addCSVPlot(self, filename, field, name, color):
        data = read_csv.read_csv_bode(inputDirectory + "/" + filename)
        signal = csvToSignal(data, field)
        signal.mode = "csv"

        self.plotCount.append({
            "signal": signal,
            "color": color,
            "name": name
        })

        return self

    def addXMLPlot(self, filename, name, color):
        signal = SignalsReadWrite.readSignal(inputDirectory + "/" + filename)
        signal.mode = "teorica"

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
                practica.setShowEndXvar(teorica.xvarEnd)
        return self

    def plotAndSave(self, filename):
        patches = []
        fig, ax1 = plt.subplots()
        for plot in self.plotCount:
            if plot["signal"].mode == "teorica":
                xvalues, yvalues = plot["signal"].getSamplesChangeXvar()
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

        plt.title(self.title)

        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
        plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

        plt.xlabel(self.xAxisTitle)
        plt.ylabel(self.yAxisTitle)

        fig.savefig(outputDirectory + "/" + filename, dpi=300)


def main():

    data = [
        # ["med_01", '2'],
        # ["med_02", '2'],
        # ["med_03", '2'],
        # ["med_04", '2'],
        # ["med_05", 'B'],
        # ["med_06", 'B'],
        # ["med_07", 'B'],
        # ["med_08", 'B'],
        # ["med_09", 'B'],
        # ["med_10", '1'],
        # ["med_11", '1'],
        # ["med_12", '2'],
        # ["med_13", '2'],
        # ["med_14", '2'],
        # ["med_15", '2'],
        # ["med_16", '2'],
        # ["med_17", '2'],
        # ["med_18", '2'],
        # ["med_19", '2'],
        # ["med_20", '2'],
        # ["med_21", '2'],
        # ["med_22", '2'],
        # ["med_24", '2'],
        # ["med_25", '2'],
        # ["med_26", '2'],
        # ["med_27", '2'],
        ["6c_ll_sen", '2'],
        # ["6b_ll_exp", '2'],
    ]

    for di in data:
        filename = di[0]
        field = di[1]

        CombinedPlot()\
            .setXTitle("tiempo (s)")\
            .setYTitle("Tensión (V)")\
            .setTitle(filename)\
            .addXMLPlot(
                filename=filename+".xml",
                name="Simulación",
                color="blue"
            )\
            .placeLimits()\
            .addCSVPlot(
            filename="Mediciones basicas/"+filename+".csv",
            name="Medición " + filename,
            field=field,
            color="orange") \
            .plotAndSave(filename+".png")
        print("done ", filename)
        plt.show()



    #test01.addXMLPlot("ExpressInput/test01.xml")
    #test01.addXLSPlot("ExpressInput/Mediciones basicas/med_01.csv")


main()
