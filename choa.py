import more_itertools as mit
import random
from calculations import Calculations
from chimp import Chimp


class ChimpAlgo:
    def __init__(self):
        self.n = 30
        self.current_iter = 0
        self.dim = 30
        self.MAX_ITER = 500
        self.f = 2.5
        self.population = []
        self.groups = []
        self.attacker = None
        self.chaser = None
        self.barrier = None
        self.driver = None

    def init_population(self):
        for i in range(self.n):
            new_chimp = Chimp()
            self.population.append(new_chimp)

    def divide_population(self):
        if len(self.population) == self.n:
            temp_population = self.population
            random.shuffle(temp_population)
            new_groups = mit.distribute(4, temp_population)
            self.groups = [list(g) for g in new_groups]
        else:
            raise Exception("populacja nie została zainicjalizowana!")

    def calculate_fitness(self):
        for chimp in self.population:
            chimp.fitness = Calculations.calculate_fitness(chimp.pos)

    def select_best_agents(self):
        # TODO: implement __lt__ and __gt__ logic to sort without lambda
        best_chimps = sorted(self.population, key=lambda c: c.fitness)
        self.attacker = best_chimps[0]
        self.chaser = best_chimps[1]
        self.barrier = best_chimps[2]
        self.driver = best_chimps[3]

    def update_positions(self):
        for idx, g in enumerate(self.groups):
            for chimp in g:
                if chimp.group == 0:
                    chimp.group = idx + 1
                chimp.update_coefficients(self.current_iter, self.MAX_ITER)
                u = random.random()
                if u < 0.5:
                    if abs(chimp.a) < 1:
                        # tutaj znajduje się klasyczne wyliczanie dystansu
                        chimp.update_pos(self.attacker, self.chaser, self.barrier, self.driver)
                    elif abs(chimp.a > 1):
                        break
                elif u >= 0.5:
                    # tutaj wstawiamy chaotyczną wartość
                    chimp.m = Calculations.calculate_m(chimp.m)
                    chimp.update_pos_chaotically()

    def run_algorithm(self):
        self.init_population()
        self.divide_population()
        while self.current_iter < self.MAX_ITER:
            self.calculate_fitness()
            self.select_best_agents()
            self.update_positions()
            print(self.attacker.pos)
            self.current_iter += 1


choa = ChimpAlgo()
choa.run_algorithm()
