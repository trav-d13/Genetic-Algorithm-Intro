import random
import string

from Individual import Individual


class Population:
    def __init__(self, population_size: int, target: str):
        self.population_size = population_size  # Parameter of population size
        self.target = target  # Parameter of target string
        Individual.set_target(self.target)  # Set the target used by the Individual class
        self.individuals = []  # Container to hold all individuals in a population

    def initialize_population(self):
        for i in range(self.population_size):  # Loop through the number of individuals and initialize them at random
            genetics = self.random_genetic_material_creator()  # Create random genetic material for a single individual
            self.individuals.append(Individual(genetics))  # Create the individual and add it to the population

    def random_genetic_material_creator(self) -> str:
        genetic_choices = random.choices(string.ascii_lowercase + " ", k=len(self.target))  # Select 44 characters from a list of lower case characters and include the space
        genetics = "".join(genetic_choices)  # Join that list together into a single string
        return genetics

    def print_population(self):
        for individual in self.individuals:  # Loop through each individual
            print(individual)  # Pprint the individual

    def population_avg_fitness(self):
        total_fitness = self.calc_total_fitness()  # Calculate the sum of the population fitness
        return total_fitness / self.population_size  # Average the fitness and return it

    def calc_total_fitness(self):
        total_fitness = 0
        for individual in self.individuals:  # Loop through each individual
            total_fitness = total_fitness + individual.fitness  # Add each individual's fitness to the total
        return total_fitness

    def find_fittest_individual(self):
        highest_fitness = 0
        fittest_individual = None
        for individual in self.individuals:
            if individual.fitness >= highest_fitness:
                fittest_individual = individual
                highest_fitness = individual.fitness
        return fittest_individual
