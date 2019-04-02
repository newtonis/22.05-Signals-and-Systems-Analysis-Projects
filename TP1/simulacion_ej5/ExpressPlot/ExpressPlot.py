from util_python import read_csv
from Etapas import SignalsReadWrite
from util_python import Senial
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def csvToSignal(data, field):
    while len(data["x-axis"]) > len(data[field]):
        data["x-axis"].pop()

    senial = Senial.Senial(data["x-axis"], data[field])

    return senial


class CombinedPlot:
    def __init__(self):
        self.plotCount = []
        self.title = ""
        self.xAxisTitle = ""
        self.yAxisTitle = ""
        self.func = None

    def setTitle(self, title):
        self.title = title
        return self

    def setXTitle(self, title):
        self.xAxisTitle = title
        return self

    def setYTitle(self, title):
        self.yAxisTitle = title
        return self

    def addSignalPlot(self, signal, color, name):
        self.plotCount.append({
            "signal": signal,
            "color": color,
            "name": name
        })
        return self

    def addCSVPlot(self, filename, field, name, color):
        data = read_csv.read_csv_bode(filename)
        signal = csvToSignal(data, field)
        signal.mode = "csv"

        self.plotCount.append({
            "signal": signal,
            "color": color,
            "name": name
        })

        return self

    def addXMLPlot(self, filename, name, color):
        signal = SignalsReadWrite.readSignal(filename)
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

        if self.func:
            func, args = self.func
            args["ax"] = ax1
            func(args)

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

        fig.savefig(filename, dpi=300)

    def extraPlot(self, func, args):
        self.func = func, args

        return self
