import random

from Individual import Individual


def single_point_crossover(parent_1: Individual, parent_2: Individual):
    point = random.randint(a=0, b=len(parent_1.genetics))
    print(point)