import math
import random

import numpy as np

from fitness import rastrigin, rosenbrock


class Calculations:
    def __init__(self):
        self.dim = 30

    @staticmethod
    def generate_pos(dim: int):
        return [random.random() * 5.12 for _ in range(dim)]

    @staticmethod
    def calculate_f_coefficient_c1(strategy: int, current_iter: int, max_iter: int):
        match strategy:
            case 1:
                return 1.95 - 2 * (math.pow(current_iter, (1 / 4)) / math.pow(max_iter, (1 / 3)))
            case 2:
                return 1.95 - 2 * (math.pow(current_iter, (1 / 3)) / math.pow(max_iter, (1 / 4)))
            case 3:
                return (-3 * math.pow(current_iter, 3) / math.pow(max_iter, 3)) + 1.5
            case 4:
                return (-2 * math.pow(current_iter, 3) / math.pow(max_iter, 3)) + 1.5

    @staticmethod
    def calculate_f_coefficient_c2(strategy: int, current_iter: int, max_iter: int):
        if current_iter == 0:
            current_iter = 1
        match strategy:
            case 1:
                return 2.5 - (2 * math.log(current_iter) / math.log(max_iter))
            case 2:
                return (-2 * math.pow(current_iter, 3) / math.pow(max_iter, 3)) + 2.5
            case 3:
                return 0.5 + 2 * math.exp(-1 * math.pow((4 * current_iter / max_iter), 2))
            case 4:
                return 2.5 + 2 * math.pow((current_iter / max_iter), 2) - 2 * (2 * current_iter / max_iter)

    @staticmethod
    def calculate_m(x=0.7):
        new_x = 4 * x * (1 - x)
        return new_x

    @staticmethod
    def calculate_fitness(chimp_pos: list):
        return rastrigin(chimp_pos)

    @staticmethod
    def calculate_distance(chimp, another_chimp, c: int, m: list):
        dist = []
        for i in range(len(chimp.pos)):
            dist.append(c * another_chimp.pos[i] - (m * chimp.pos[i]))
        return np.linalg.norm(dist)

    @staticmethod
    def calculate_x(chimp, a: int, d_chimp: float):
        x = []
        for i in range(len(chimp.pos)):
            x.append(chimp.pos[i] - a * d_chimp)
        return x

    @staticmethod
    def calculate_a(f: float, c1: float):
        return (2 * f * (c1 * random.random())) - f

    @staticmethod
    def calculate_c(c2):
        return 2 * (c2 * random.random())
