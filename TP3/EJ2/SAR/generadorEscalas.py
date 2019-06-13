
from numpy import logspace, log10

file = open("PeriodosEscala.hex")
escalas = open("output.hex", "w")

k = 1000
n = 1e-9

f_init = 5 * k
f_last = 1000 * k
points = 256

frecuencies = logspace(log10(f_init), log10(f_last), points)
print(frecuencies)

base = 20 * n

lines = []
mem = 0

for f in frecuencies:
    t = 1/f

    lines.append(str(mem)+" : "+str(int(t/base))+" ;\n")

    mem += 1

print(lines)

escalas.writelines(lines)


