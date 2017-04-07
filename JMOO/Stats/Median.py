import numpy as np

def median(column_of_data):
    return np.percentile(column_of_data, 50)

class Median:
    """collects the median on each objective of a population"""
    
    STAT_NAME = "Median"

    def __init__(self, population):
        self._population = population
        

    def collect(self, do_not_evaluate = False):
        """return a vector representing the median of each objective score"""

        if not do_not_evaluate:
            for individual in self._population:
                individual.evaluate()

        fitnesses = [individual.fitness for individual in self._population]
        num_columns = len(fitnesses[0])
        fitness_as_columns = [[fitness[column_index] for fitness in fitnesses] for column_index in range(num_columns)]
        medians = [median(fitness_column) for fitness_column in fitness_as_columns] 
        return medians   