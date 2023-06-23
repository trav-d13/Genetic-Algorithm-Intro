target = ""  # Initialize the global target variables


class Individual:
    def __init__(self, genetics: str, target_string: str):
        global target  # Global keyword allows access to target global variable

        if target == "":  # If target has not been initialized yet, initialize it
            target = target_string

        self.genetics = genetics  # Assign the genetics variable to an object variable
        self.fitness = self.calculate_fitness()  # Calculate the individual's fitness based on the genetics

    def calculate_fitness(self):
        genetic_breakdown = list(self.genetics)  # Break the genetics string into a list of genetic components (characters)
        target_breakdown = list(target)  # Break the target down into a set of components (characters)
        fitness_value = 0  # Initialize fitness value
        for component_pos in range(len(genetic_breakdown)):
            if genetic_breakdown[component_pos] == target_breakdown[component_pos]:  # If the components (characters) match, then increase the fitness
                fitness_value = fitness_value + 1
        return fitness_value


    def __str__(self):
        return "Genetics: " + self.genetics + " | Fitness = " + str(self.fitness)
