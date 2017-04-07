import random
from Individual import Individual

class Crossover:
    """takes a population and generates an equal-size population of offspring by taking sequential pairs of parents"""
    def __init__(self, problem, population, crossover_rate):
        if crossover_rate > 1.0:
            crossover_rate = 1.0
        elif crossover_rate < 0.0:
            crossover_rate = 0.0
        self._crossover_rate = crossover_rate
        self._problem = problem
        self._population = population

    def crossover(self):
        offspring = []
        midpt = int(len(self._population)/2)
        for individual_1, individual_2 in zip(self._population[:midpt], self._population[midpt:]):
            if random.random() < self._crossover_rate:
                crossover_point = int(min(len(individual_1), len(individual_2))/2)
                offspring.append(Individual(self._problem, list(individual_1[:crossover_point])+list(individual_2[crossover_point:])))
                offspring.append(Individual(self._problem, list(individual_2[:crossover_point])+list(individual_1[crossover_point:])))
            else:
                offspring.append(individual_1)
                offspring.append(individual_2)
        return offspring
