# This file serves as the main execution of the genetic algorithm.
import Reproduction
import Selection
from Population import Population

generation = 0  # Variable keeping track of each generation


def stopping_condition():
    if generation > 2:
        return True
    return False


if __name__ == "__main__":
    # GA INFORMATION
    target = "with enough probability anything is possible"
    population_size = 50

    # POPULATION CREATION
    population = Population(population_size=population_size, target=target)
    population.initialize_population()
    print("Population avg fitness: ", population.population_avg_fitness())

    while not stopping_condition():
        # SELECTION
        parent_1 = Selection.roulette_wheel_selection(population)  # This can be substituted with Selection,tournament_selection()
        parent_2 = Selection.roulette_wheel_selection(population)  # Alternative substitution is Selection.boltzman()

        # REPRODUCTION
        Reproduction.single_point_crossover(parent_1, parent_2)

        # INFORMATION DISPLAY
        generation += 1
        print("Generation: ", generation,
              " | Highest fitness: ", population.find_fittest_individual().fitness,
              " | Population avg fitness: ", population.population_avg_fitness())


