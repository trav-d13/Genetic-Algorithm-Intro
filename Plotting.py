import csv

import pandas as pd
from matplotlib import pyplot as plt

filename = "store.csv"


class Plotting:
    def __init__(self):
        self.x = [0]
        self.average_line = [0]
        self.best_line = [0]

    def update(self, avg, best, generation):
        self.average_line.append(avg * 100)
        self.best_line.append(best * 100)
        self.x.append(generation)

    def save(self):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Generation', 'Average', 'Best'])

            # Combine the lists using zip and write each row
            for row in zip(self.x, self.average_line, self.best_line):
                writer.writerow(row)

    def display(self):
        df = pd.read_csv("store.csv")

        # Create a line chart using Matplotlib
        plt.figure(figsize=(10, 6))

        plt.plot(df['Generation'], df['Average'], marker='o', label='Average')
        plt.plot(df['Generation'], df['Best'], marker='o', label='Fittest')

        plt.xlabel('Generation')
        plt.ylabel('Value')
        plt.title('Generational Average and Fittest Individuals')
        plt.legend()

        plt.grid(True)
        plt.show()
