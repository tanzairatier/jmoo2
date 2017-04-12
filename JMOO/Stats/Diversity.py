import numpy as np

def diversity(population_frontier):
    n = len(population_frontier)
    L = len(population_frontier[0].fitness)

    extremity_individuals = (population_frontier[0], population_frontier[-1])

    df = sqrt(sum( [ (population_frontier[0].fitness[i] - extremity_individuals[0].fitness[i])**2 for i in range(L)  ]  ))
   
    dl = sqrt(sum( [ (population_frontier[-1].fitness[i] - extremity_individuals[1].fitness[i])**2 for i in range(L)  ]  ))
    
    d = [0.0] * (n-1)
    for i in range(len(d)):
       d[i] = sqrt(sum( [ (first_front[i].fitness.values[j] - first_front[i+1].fitness.values[j])**2 for j in range(len(first))  ]  ))
    dm = sum(d)/len(d)
    di = sum(abs(d_i - dm) for d_i in d)
    if (dm == 0): return 0
    delta = (df + dl + di)/(df + dl + len(d) * dm )
    return delta


class Diversity:
    """collects the mean on each objective of a population"""
    
    STAT_NAME = "Mean"
    FORMATTER = "%10.3f"

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