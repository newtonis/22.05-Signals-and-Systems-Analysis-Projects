

def processSystemB(x, rl, l):
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

        y[i] = 1/2 * x[i] + 1/2 * x[i-1] + 1/2 * rl * yl + 1/2 * rl * yl1

    return y
