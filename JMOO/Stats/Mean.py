import numpy as np

def mean(column_of_data):
    return np.mean(column_of_data)

class Mean:
    """collects the mean on each objective of a population"""
    
    STAT_NAME = "Mean"

    def __init__(self, population):
        self._population = population
        

    def collect(self, do_not_evaluate = False):
        """return a vector representing the mean of each objective score"""

        if not do_not_evaluate:
            for individual in self._population:
                individual.evaluate()

        fitnesses = [individual.fitness for individual in self._population]
        num_columns = len(fitnesses[0])
        fitness_as_columns = [[fitness[column_index] for fitness in fitnesses] for column_index in range(num_columns)]
        means = [mean(fitness_column) for fitness_column in fitness_as_columns] 
        return means