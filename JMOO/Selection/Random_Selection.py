import random

class Random_Selector(object):
    """given a population of candidates, down-select the pool to a fixed number"""
    def __init__(self, population_size_desired, population):
        self._population_size_desired = population_size_desired
        self._population = population

    def select(self):
        num_to_deselect = len(self._population) - self._population_size_desired
        while num_to_deselect > 0:
            self._population.remove(random.choice(self._population))
            num_to_deselect -= 1
        return self._population
        
        



