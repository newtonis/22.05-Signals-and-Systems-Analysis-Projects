from source import *

data=read_csv_bode("2osc.csv")
ton = (3.76e-5) -(-4.80282e-6)
ton2 = (5.41-4.34)*(1e-5)

print(ton)
print(ton2)

second = data["x-axis"]
second = second[:-1]
Volt1 = data["1"]
Volt2 = data["2"]

freq = getfreq(second,Volt1,2)
duty = round(ton*freq*100,2)
duty2 = round(ton2*freq*100,2)
print(duty,duty2)
plegend = "f: "+str(int(freq)) +"Hz , DC: " + str(duty) + "%"
plegend2 = "f: "+str(int(freq)) +"Hz , DC: " + str(duty2) + "%"

print(plegend)
plotfunc("Tiempo(s)","Tensión(V)",second,Volt1,plegend)
plotfunc("Tiempo(s)","Tensión(V)",second,Volt2,plegend2)

plt.show()

