# y(nT) = 0.5x((n-2)T) + alpha * y((n-1)T) + beta * y((n-2)T)


def diffEq(alpha, beta, x2, y1, y2):
    return 0.5 * x2 + alpha * y1 + beta * y2

n = 30
alpha = 1
beta = -0.5

step = [0, 0]
pulse = [0, 0]

n = n-2
for i in range(0, n+1):
    step.append(diffEq(alpha, beta, 1, step[-1], step[-2]))
    pulse.append(diffEq(alpha, beta, i == 0, pulse[-1], pulse[-2]))

print(step)
print(pulse)

