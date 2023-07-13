import random
import string

from Individual import Individual

mutation_prob = 0.15
child_selection_prob = 0.5


def mutate(child_1: Individual, child_2: Individual):
    prob = random.uniform(0, 1)
    child = child_1

    if prob < child_selection_prob:  # determine which child should be mutated
        child = child_2

    if prob < mutation_prob:  # Determine if mutation should occur
        single_point_mutation(child)


def single_point_mutation(child: Individual):
    random_letter = random.choice(string.ascii_lowercase + " ")
    random_location = random.randint(a=0, b=len(child.genetics) - 1)
    if random_location == len(child.genetics) - 1:  # Random swap location is the last position (edge case)
        child.update_genetics(child.genetics[:random_location] + random_letter)
    elif random_location == 0:
        child.update_genetics(random_letter + child.genetics[random_location + 1:])  # Random swap is the first location (edge case)
    else:  # Random swap location is any other position
        child.update_genetics(child.genetics[:random_location] + random_letter + child.genetics[random_location + 1:])


