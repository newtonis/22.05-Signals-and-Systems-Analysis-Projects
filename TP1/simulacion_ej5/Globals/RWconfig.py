from xml.dom import minidom
import xml.etree.ElementTree as ET


configFile = "config.xml"


def loadConfig():
    mydoc = minidom.parse("Globals/config.xml")
    # config = mydoc.getElementsByTagName("config")

    # config.FAAfreq = config.attributes['FAAfreq']
    # config.SRate = config.attributes['SFreq']
    # config.attributes['time']
    # config.attributes['time']


def writeConfig():
  pass

