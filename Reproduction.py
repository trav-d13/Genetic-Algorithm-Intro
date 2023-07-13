import random

from Individual import Individual


def single_point_crossover(parent_1: Individual, parent_2: Individual):
    point = random.randint(a=0, b=len(parent_1.genetics))  # Determine random point of crossover in genetics
    child_1_genetics = parent_1.genetics[:point] + parent_2.genetics[point:]  # Child 1 genetics
    child_2_genetics = parent_2.genetics[:point] + parent_1.genetics[point:]  # Child 2 genetics

    return Individual(genetics=child_1_genetics), Individual(genetics=child_2_genetics)  # Return new child individuals
