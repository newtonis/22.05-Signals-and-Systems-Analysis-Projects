from xml.dom import minidom
import xml.etree.ElementTree as ET

from Etapas.Senial import Senial


def readSignal(filename):
    mydoc = minidom.parse(filename)

    root = mydoc.childNodes[0]
    try:
        shift = float(root.attributes['shift'].value)
    except:
        shift = 0

    samples = mydoc.getElementsByTagName("sample")

    t = []
    y = []

    for sample in samples:
        t.append(float(sample.attributes['time'].value))
        y.append(complex(sample.attributes['value'].value).real)

    senial = Senial(t, y)
    senial.setShift(shift)
    return senial


def writeSignal(signal, filename):
    data = ET.Element('signal')

    for index in range(len(signal.xvar)):
        item = ET.SubElement(data, 'sample')
        item.set("time", str(signal.xvar[index]))
        item.set("value", str(signal.values[index]))

    myData = ET.tostring(data)
    myFile = open(filename, "wb")
    print(myData)
    myFile.write(myData)

