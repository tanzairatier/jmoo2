import random

class Mutator:
    def __init__(self, mutation_rate, population):
        self._population = population
        if mutation_rate > 1.0:
            mutation_rate = 1.0
        elif mutation_rate < 0.0:
            mutation_rate = 0.0
        #Logger.Warn("Mutation rate set to within boundaries of [0,1].")
        self._mutation_rate = mutation_rate
    def mutate(self):
        for member in self._population:
            if random.random() < self._mutation_rate:
                pass