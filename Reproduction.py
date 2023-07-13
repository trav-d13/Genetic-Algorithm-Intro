import random

from Individual import Individual

reproduce_prob = 0.9  # Probability of parents reproducing


def reproduce(parent_1: Individual, parent_2: Individual, method: str):
    prob = random.uniform(0, 1)

    child_1 = parent_1  # Assign parents as children, in case reproduction does not occur
    child_2 = parent_2

    if prob < reproduce_prob:  # Determine if reproduction occurs
        match method:  # Determine method of reproduction
            case "Single":
                child_1, child_2 = single_point_crossover(parent_1, parent_2)
    return child_1, child_2


def single_point_crossover(parent_1: Individual, parent_2: Individual):
    point = random.randint(a=0, b=len(parent_1.genetics))  # Determine random point of crossover in genetics
    child_1_genetics = parent_1.genetics[:point] + parent_2.genetics[point:]  # Child 1 genetics
    child_2_genetics = parent_2.genetics[:point] + parent_1.genetics[point:]  # Child 2 genetics

    return Individual(genetics=child_1_genetics), Individual(genetics=child_2_genetics)  # Return new child individuals
