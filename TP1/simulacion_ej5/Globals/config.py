import Globals.RWconfig as RWconfig

LARGE_FONT = ("Bahnschrift", 24)
SMALL_FONT = ("Bahnschrift", 16)
SMALLEST_FONT = ("Bahnschrift", 10)
debug = True

# los valores no son los reales


class ConfigData:
    def __init__(self):
        self.FAAfreq = None
        self.SHsample = None
        self.SHhold = None
        self.SRate = None

        self.LLfreq = None
        self.LLoff = None
        self.LLon = None
        self.Transitorio = None

        self.loaded = False

    def setLoaded(self):
        self.loaded = True

    def load(self):
        RWconfig.loadConfig(self)

    def save(self):
        RWconfig.writeConfig(self)


configData = ConfigData()


def GetConfigData():
    if not configData.loaded:
        configData.load()

    return configData

