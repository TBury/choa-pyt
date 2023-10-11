from calculations import Calculations


class Chimp:
    def __init__(self):
        self.pos = Calculations.generate_pos(dim=30)
        self.group = 0
        self.fitness = 0
        self.f = 2.5
        self.m = Calculations.calculate_m(0.7)
        self.a = 0
        self.c = 0

    def update_pos(self, attacker, chaser, barrier, driver):
        d_att = Calculations.calculate_distance(self, attacker, attacker.c, attacker.m)
        d_cha = Calculations.calculate_distance(self, chaser, chaser.c, chaser.m)
        d_bar = Calculations.calculate_distance(self, barrier, barrier.c, barrier.m)
        d_dri = Calculations.calculate_distance(self, driver, driver.c, driver.m)

        x1 = Calculations.calculate_x(attacker, self.a, d_att)
        x2 = Calculations.calculate_x(chaser, self.a, d_cha)
        x3 = Calculations.calculate_x(barrier, self.a, d_bar)
        x4 = Calculations.calculate_x(driver, self.a, d_dri)

        for i in range(len(self.pos)):
            self.pos[i] = (x1[i] + x2[i] + x3[i] + x4[i]) / 4

    def update_pos_chaotically(self):
        for i in range(len(self.pos)):
            self.pos[i] *= self.m

    def update_coefficients(self, current_iter: int, max_iter: int):
        f_coef_c1 = Calculations.calculate_f_coefficient_c1(self.group, current_iter, max_iter)
        f_coef_c2 = Calculations.calculate_f_coefficient_c2(self.group, current_iter, max_iter)
        self.f = 2.5 - current_iter * (2.5/max_iter)
        self.m = Calculations.calculate_m(self.m)
        self.c = Calculations.calculate_c(f_coef_c2)
        self.a = Calculations.calculate_a(self.f, f_coef_c1)
