import random

from Population import Population

tournament_pool_size = 500  # Initialize the size of the tournament pool


# This method allows you to specify which selection method is executed
def select(method: str, population: Population):
    individual = None
    match method:
        case "Roulette":
            individual = roulette_wheel_selection(population)
        case "Tournament":
            individual = tournament_selection(population)

    population.individuals.remove(individual)  # Remove the parent from the population
    return individual


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


def tournament_selection(population):
    pool = form_tournament_pool(population)  # Form the tournament pool
    fittest_ind = fittest_in_tournament(pool)  # Determine the fittest individaul from the pool
    return fittest_ind


def fittest_in_tournament(pool):
    highest_fitness = 0  # Initialize the values to determine who is the fittest individual
    fittest_individual = None

    for individual in pool:  # Loop through the individuals in the pool
        if individual.fitness > highest_fitness:  # A higher fitness is detected
            fittest_individual = individual  # Update the fittest individual
            highest_fitness = individual.fitness  # Update the highest fitness value

    return fittest_individual


def form_tournament_pool(population):
    pool = random.choices(population.individuals,
                          k=tournament_pool_size)  # Select 10 individuals randoms from the population
    return pool
