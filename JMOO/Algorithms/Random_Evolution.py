from Population.Random_Population import Random_Populator
from Selection.Random_Selection import Random_Selector
from Selection.Tournament import Tournament
from Perturbation.Mutation import Mutator
from Reproduction.Crossover import Crossover 
from Stats.Median import Median
from StoppingCriteria.Criteria import MaxGenerationsCriteria 

class Random_Evolution:
    def __init__(self, jmoo_settings, problem, stat_tracker):
        self._jmoo_settings = jmoo_settings
        self._problem = problem
        self._stat_tracker = stat_tracker
        self._stopping_criteria = MaxGenerationsCriteria(20)

    def evolve(self):

        population = Random_Populator(self._problem, 100).populate()

        self._stat_tracker.collect_stats(population, self._problem)

        while not self._stopping_criteria.is_satisfied(self._stat_tracker):
            population = Crossover(self._problem, population, 0.80).crossover()
            population = Mutator(0.08).mutate(population)
            #population = Random_Selector(100, population).select()
            population = Tournament(4, 100, population).select()
            self._stat_tracker.collect_stats(population, self._problem)

        self._stat_tracker.pretty_print_stats()