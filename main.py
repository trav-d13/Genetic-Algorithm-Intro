# This file serves as the main execution of the genetic algorithm.
import Selection
from Population import Population

if __name__ == "__main__":
    # GA INFORMATION
    target = "with enough probability anything is possible"
    population_size = 50

    # POPULATION CREATION
    population = Population(population_size=population_size, target=target)
    population.initialize_population()
    population.print_population()
    print("Population avg fitness: ", population.population_avg_fitness())

    # SELECTION
    parent_1 = Selection.roulette_wheel_selection(population)
    parent_2 = Selection.roulette_wheel_selection(population)
    print(parent_1)
    print(parent_2)
