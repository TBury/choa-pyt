import math


def rastrigin(pos: list):
    return 10 * len(pos) + sum([math.pow(x, 2) - 10 * math.cos(2 * math.pi * x) for x in pos])


def rosenbrock(pos: list):
    value = 0
    for i in range(len(pos) - 1):
        value += 100 * math.pow((pos[i + 1] - pos[i] * pos[i]), 2) + math.pow((1 - pos[i]), 2)
    return value
