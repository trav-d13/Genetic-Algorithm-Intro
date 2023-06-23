# This file serves as the main execution of the genetic algorithm.
from Population import Population

if __name__ == "__main__":
    target = "with enough probability anything is possible"
    population_size = 10

    population = Population(population_size=population_size, target=target)
    population.initialize_population()
    population.print_population()
