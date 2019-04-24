
notas = dict()

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

standardA4 = 440
A0 = standardA4 / 4

notas['A'] = [A0]

for i in range(10):
    notas['A'].append(notas['A'][i-1]*2)
notas['A'].append(A0/2)

