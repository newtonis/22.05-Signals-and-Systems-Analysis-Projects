from random import randrange
from scipy import fft, ifft
from numpy import real, imag

input_file = open("input.txt", "w+")
output_file = open("output.txt", "w+")

for i in range(100):

    ni = randrange(0, 12)
    n = 2**ni

    values = []

    for i in range(n):
        values.append(
            randrange(-100000, 100000, 1) * 0.01 + randrange(-100000, 10000, 1) * 0.01 * 1j
        )

    output = ifft(values)

    input_file.write(
        str(n) + "\n"
    )
    for value in values:
        input_file.write(
            str(real(value)) + "\n" + str(imag(value)) + "\n"
        )

    output_file.write(
        str(n) + "\n"
    )
    for out in output:
        output_file.write(
            str(real(out)) + "\n" + str(imag(out))  + "\n"
        )

