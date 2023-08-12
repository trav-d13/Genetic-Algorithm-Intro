# This file serves as the main execution of the genetic algorithm.
import Mutation
import Reproduction
import Selection
from Population import Population

generation = 0  # Variable keeping track of each generation


def stopping_condition():
    if generation > 1000:
        return True
    return False


if __name__ == "__main__":
    # GA INFORMATION
    target = "hello world"
    population_size = 1000

    # POPULATION CREATION
    population = Population(population_size=population_size, target=target)
    population.initialize_population()

    while not stopping_condition():
        # INFORMATION DISPLAY
        print("Generation: ", generation,
              " | Highest fitness: ", population.find_fittest_individual().fitness,
              " | Population avg fitness: ", population.population_avg_fitness())

        # SELECTION
        parent_1 = Selection.select("Tournament", population)  # Specify the selection method
        parent_2 = Selection.select("Tournament", population)

        # REPRODUCTION
        child_1, child_2 = Reproduction.reproduce(parent_1, parent_2, "Double")
        Reproduction.add_children_to_population(child_1, child_2, population)

        # MUTATION
        Mutation.mutate(child_1, child_2)

        # UPDATE
        generation += 1


