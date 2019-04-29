import numpy as np


def systemE(x, fs, l, rl=1, pb = 1):
    y = [0] * len(x)
    a = 1/2
    b = 1/2

    for n in range(len(x)):
        mult = 1 - np.random.choice(2, 1, p = [pb, 1-pb])*2

        mult = mult[0]
        #print(mult)

        if n >= l + 1:
            y[n] = mult*(x[n] + x[n - 1] + y[n - l] * a * rl + y[n - l - 1] * b * rl)
        else:
            x_last = x[n - 1] if n >= 1 else 0
            y_last_l = y[n - l] if n >= l else 0
            y_last_l_1 = y[n - l - 1] if n >= l + 1 else 0

            y[n] = mult*(x[n] + x_last + y_last_l * a * rl + y_last_l_1 * b * rl)

    z = [0] * len(y)

    for n in range(len(y)):
       if n >= 1:
           z[n] = y[n] - y[n - 1] + 0.9999 * z[n - 1]
       else:
           z[n] = y[n]

    return np.array(z)

