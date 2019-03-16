from xml.dom import minidom
import xml.etree.ElementTree as ET

from Etapas.Senial import Senial


def readSignal(filename):
    mydoc = minidom.parse(filename)

    samples = mydoc.getElementsByTagName("sample")


    t = []
    y = []

    for sample in samples:
        t.append(float(sample.attributes['time'].value))
        y.append(float(sample.attributes['value'].value))

    return Senial(t, y)


def writeSignal(signal, filename):
    data = ET.Element('signal')

    for index in range(len(signal.time)):
        item = ET.SubElement(data, 'sample')
        item.set("time", str(signal.time[index]))
        item.set("value", str(signal.values[index]))

    myData = ET.tostring(data)
    myFile = open(filename, "wb")
    print(myData)
    myFile.write(myData)

