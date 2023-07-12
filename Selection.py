import random


# For this method it is essential that the Individual fitness values are positive (No negative values)
def roulette_wheel_selection(population):
    roulette_wheel = construct_roulette_wheel(population)
    selector = random.uniform(0, 1)
    keys = sorted(roulette_wheel.keys())  # Extract the probability values in ascending order
    for key in keys:
        if key >= selector:  # The probability key exceeds the selector. This is the selected individual.
            return roulette_wheel[key]


def construct_roulette_wheel(population):
    current_prob = 0  # Initialize the current porb value
    wheel = dict()  # Create a dict to hold the probability intervals and link to the correct individuals
    for individual in population.individuals:  # Loop through each individual in the population
        probability = individual.fitness / population.calc_total_fitness()  # Calculate the inidivudals prob of selection
        current_prob = current_prob + probability  # Adjust the current prob value
        wheel[current_prob] = individual  # Assign the prob interval to the individual
    return wheel

