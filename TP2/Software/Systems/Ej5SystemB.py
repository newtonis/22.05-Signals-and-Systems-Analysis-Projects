from numpy import random


def processSystemB(x, rl, l, b = 1):
    y = [0] * len(x)

    for i in range(len(x)):
        if i > l:
            yl = y[i - l]
        else:
            yl = 0

        if i > l + 1:
            yl1 = y[i - l - 1]
        else:
            yl1 = 0

        if i > 0:
            xl = x[i - 1]
        else:
            xl = 0

        r = 1 - 2 * random.choice(2, 1, p=[b, 1-b])
        y[i] = r * (1/2 * x[i] + 1/2 * xl + 1/2 * rl * yl + 1/2 * rl * yl1)

    return y
