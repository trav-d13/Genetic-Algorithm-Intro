import random

from Individual import Individual
from Population import Population

reproduce_prob = 0.98  # Probability of parents reproducing


def reproduce(parent_1: Individual, parent_2: Individual, method: str):
    prob = random.uniform(0, 1)

    child_1 = parent_1  # Assign parents as children, in case reproduction does not occur
    child_2 = parent_2

    if prob < reproduce_prob:  # Determine if reproduction occurs
        match method:  # Determine method of reproduction
            case "Single":
                child_1, child_2 = single_point_crossover(parent_1, parent_2)
            case "Double":
                child_1, child_2 = double_point_crossover(parent_1, parent_2)
    return child_1, child_2


def add_children_to_population(child_1: Individual, child_2: Individual, population: Population):
    population.individuals.append(child_1)
    population.individuals.append(child_2)


def single_point_crossover(parent_1: Individual, parent_2: Individual):
    point = random.randint(a=0, b=len(parent_1.genetics))  # Determine random point of crossover in genetics
    child_1_genetics = parent_1.genetics[:point] + parent_2.genetics[point:]  # Child 1 genetics
    child_2_genetics = parent_2.genetics[:point] + parent_1.genetics[point:]  # Child 2 genetics

    return Individual(genetics=child_1_genetics), Individual(genetics=child_2_genetics)  # Return new child individuals


def double_point_crossover(parent_1: Individual, parent_2: Individual):
    point_a = random.randint(a=0, b=len(parent_1.genetics))  # Determine random point of crossover in genetics
    point_b = random.randint(a=0, b=len(parent_2.genetics))  # Determine random point of crossover in genetics

    if point_b < point_a:
        temp = point_b
        point_b = point_a
        point_a = temp

    child_1_genetics = parent_1.genetics[:point_a] + parent_2.genetics[point_a: point_b] + parent_1.genetics[point_b:]
    child_2_genetics = parent_2.genetics[:point_a] + parent_1.genetics[point_a: point_b] + parent_2.genetics[point_b:]

    return Individual(genetics=child_1_genetics), Individual(genetics=child_2_genetics)  # Return new child individuals
