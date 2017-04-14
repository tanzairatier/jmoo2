from Population.Random_Population import Random_Populator
from Selection.Random_Selection import Random_Selector
from Selection.Tournament import Tournament
from Perturbation.Mutation import Mutator
from Reproduction.Crossover import Crossover 
from StoppingCriteria.Criteria import MaxGenerationsCriteria, MaxEvaluationsCriteria
from Algorithm import Algorithm

class Random_Evolution(Algorithm):

    NAME = "RAND"

    def __init__(self, problem, stat_tracker):
        self._problem = problem
        self._stat_tracker = stat_tracker
        self._stopping_criteria = MaxEvaluationsCriteria(2000)

    def evolve(self):

        population = Random_Populator(self._problem, 100).populate()

        self._stat_tracker.collect_stats(population)

        while not self._stopping_criteria.is_satisfied(self._stat_tracker):
            population = Crossover(self._problem, population, 0.80).crossover()
            population = Mutator(0.08).mutate(population)
            population = Tournament(4, 100, population).select()
            self._stat_tracker.collect_stats(population)

        self._stat_tracker.pretty_print_stats()