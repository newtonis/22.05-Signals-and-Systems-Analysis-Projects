from source import *

data=read_csv_bode("2osc.csv")
ton = (3.725e-5) -(-4.80282e-6)
ton2 = (1e-5)-(-2.04972e-5)

#data=read_csv_bode("max_f_max_d.csv")
#ton = 2.04638e-5-1.28581e-5
#data=read_csv_bode("min_f_max_d.csv")
#ton = (-3.28419e-5)-(-0.00216566)
#data=read_csv_bode("min_f_min_d.csv")
#ton = -0.0021520-(-0.00218579)
#data=read_csv_bode("max_f_min_d.csv")
#ton =  8.6e-6 -8.21e-6


second = data["x-axis"]
second = second[:-1]
Volt1 = data["1"]
Volt2 = data["2"]

freq = getfreq(second,Volt1,2)
#freq = getfreq2(second,Volt1,2,2e-5)
#freq = getfreq2(second,Volt1,2,2e-06)
#duty = getduty(second,Volt1,0.01,freq)

freq2 = getfreq(second,Volt2,2)


duty = round(ton*freq*100,2)
duty2 = round(ton2*freq2*100,2)

plegend = "f: "+str(int(freq)) +"Hz , DC: " + str(duty) + "%"
plegend2 = "f: "+str(int(freq2)) +"Hz , DC: " + str(duty2) + "%"

print(plegend)
plotfunc("Tiempo(s)","Tensión(V)",second,Volt1,plegend)
plotfunc("Tiempo(s)","Tensión(V)",second,Volt2,plegend)

plt.show()

