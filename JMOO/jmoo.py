from Problem import Problem
from Algorithm import Algorithm
from Problems.Schaffer import Schaffer
from Problems.Constrex import Constrex
from Problems.Fonseca import Fonseca
from StatTracker import StatTracker
from Stats.Median import Median
from Stats.Mean import Mean
from Stats.Evaluations import Evaluations
from Friendly_Errors import DecisionOutOfBoundsError, NullInputError, ImproperInputError

class jmoo(object):
    DEFAULT_POPULATION_SIZE = 100
    DEFAULT_GENERATION_LIMIT = 20
    DEFAULT_NUMBER_OF_REPEATS = 1
    DEFAULT_RANDOM_SEED = None

    def __init__(self):
        self._population_size = jmoo.DEFAULT_POPULATION_SIZE
        self._generation_limit = jmoo.DEFAULT_GENERATION_LIMIT
        self._number_of_repeats = jmoo.DEFAULT_NUMBER_OF_REPEATS
        self._random_seed = jmoo.DEFAULT_RANDOM_SEED
        self._algorithms = []
        self._problems = []

    def set_algorithms(self, algorithms):
        """ Establishes a set of algorithms to be run by the jmoo module.
        *algorithms* can either be list or scalar.  They must also be references to a *Algorithm* class or subclass, or they can be instances.
        """
        try:
            if isinstance(algorithms, list):
                for algorithm in algorithms:
                    if isinstance(algorithm, Algorithm):
                        self._algorithms.append(algorithm)
                    if issubclass(algorithm, Algorithm):
                        self._algorithms.append(algorithm())
            else:
                if issubclass(algorithms, Algorithm):
                    self._algorithms = [algorithms]
        except:
            raise ImproperInputError("Parameter *algorithms* from method *jmoo.set_algorithms* can only take instances of *Algorithm* (or its subclasses) or references to classes (or subclasses) of *Algorithm*.")

    def set_problems(self, problems):
        try:
            if isinstance(problems, list):
                for problem in problems:
                    if isinstance(problem, Problem):
                        self._problems.append(problem)
                    elif issubclass(problem, Problem):
                        self._problems.append(problem())
            else:
                if issubclass(problems, Problem):
                    self._problems = [problems]
        except:
            raise ImproperInputError("Parameter *problems* from method *jmoo.set_problems* can only take instances of *Problem*  (or its subclasses) or classes (or subclasses) of *Problem*.")

    def run(self):
        for problem in self._problems:
            for algorithm in self._algorithms:
                algorithm(problem, StatTracker([Median, Mean, Evaluations])).evolve()

    """ Population Size: the number of candidate solutions within each population."""
    @property
    def population_size(self):
        return self._population_size

    @population_size.setter
    def population_size(self, N):
        self._population_size = N

    """ Generation Limit: the maximum number of generations that an EA searcher will run for before stopping."""
    @property
    def generation_limit(self):
        return self._generation_limit

    @generation_limit.setter
    def generation_limit(self, N):
        self._generation_limit = N

    """ Number of Repeats: the number of times to repeat the algorithm for statistical consideration."""
    @property
    def number_of_repeats(self):
        return self._number_of_repeats

    @number_of_repeats.setter
    def number_of_repeats(self, N):
        self._number_of_repeats = N

    """ Random Seed: the seed to propagate throughout the system for testing purposes."""
    @property
    def random_seed(self):
        return self._random_seed

    @random_seed.setter
    def random_seed(self, N):
        self._random_seed = N


