# This file is part of JMOO.
#
#    JMOO is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    JMOO is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with JMOO.  If not, see < http: // www.gnu.org / licenses / >.

"""Core Jmoo Module for establishing MOO search scenarios."""

from Problem import Problem
from Algorithm import Algorithm
from Stat import Stat
from StatTracker import StatTracker
from FriendlyErrors import ImproperInputError, DuplicateStatError, NonUniqueStatError

class Jmoo():
    """Core Jmoo for defining MOO problem and solution scenarios.

    Example usage:
    TODO: update Jmoo example usage
    """

    DEFAULT_POPULATION_SIZE = 100
    DEFAULT_GENERATION_LIMIT = 20
    DEFAULT_NUMBER_OF_REPEATS = 1
    DEFAULT_RANDOM_SEED = None

    def __init__(self):
        self._population_size = Jmoo.DEFAULT_POPULATION_SIZE
        self._generation_limit = Jmoo.DEFAULT_GENERATION_LIMIT
        self._number_of_repeats = Jmoo.DEFAULT_NUMBER_OF_REPEATS
        self._random_seed = Jmoo.DEFAULT_RANDOM_SEED

        #List of algorithms to run on each problem
        self._algorithms = []

        #List of problems to run under each algorithm
        self._problems = []

        #List of stats to collect in each generation of an algorithm running a problem
        self._stats_to_track = []

    def set_algorithms(self, *algorithms):
        """Establishes a set of algorithms to be run by the jmoo module.

        Each algorithm must be a subclass of, or instance of subclass of the *Algorithm* base class.

        Args:
            self: A reference to this Jmoo object
            algorithms: A list of algorithms

        Returns:
            None

        Raises:
            ImproperInputError: if supplied *algorithms* argument does not contain algorithms.
        """

        try:
            for algorithm in algorithms:
                if isinstance(algorithm, Algorithm):
                    raise ImproperInputError(
                        "*jmoo.set_algorithms*: supplied algorithm must be a class reference, \
                        not an instance;  i.e. use Algorithm instead of Algorithm().")
                if issubclass(algorithm, Algorithm):
                    self._algorithms.append(algorithm)
        except:
            raise ImproperInputError(
                "Parameter *algorithms* from method *jmoo.set_algorithms* can only take instances \
                or references of type *Algorithm*.")

    def set_problems(self, *problems):
        """Establishes a set of problems to be run by the jmoo module.

        Each problem must be a subclass of, or instance of subclass of the *Problem* base class.

        Args:
            self: A reference to this Jmoo object
            algorithms: A list of problems

        Returns:
            None

        Raises:
            ImproperInputError: if supplied *problems* argument does not contain problems.
        """

        try:
            for problem in problems:
                if isinstance(problem, Problem):
                    self._problems.append(problem)
                elif issubclass(problem, Problem):
                    self._problems.append(problem())
        except:
            raise ImproperInputError(
                "Parameter *problems* from method *jmoo.set_problems* can only take instances or \
                references of type *Problem*.")

    def set_stats_to_track(self, *stats_to_track):
        """Establishes a set of stats to track after each generation of an algorithm solving a
        problem.

        Each stat must be a subclass or instance of the *Stat* base class.

        Args:
            self: A reference to this Jmoo object
            stats_to_track: A list of stats to track

        Returns:
            None

        Raises:
            ImproperInputError: if supplied stats_to_track argument does not contain stats.
        """

        try:
            for stat in stats_to_track:
                if isinstance(stat, Stat):
                    raise ImproperInputError(
                        "Supplied stat must be a class reference, \
                        not an instance;  i.e. use Stat instead of Stat().")
                if issubclass(stat, Stat):
                    self._stats_to_track.append(stat)
        except:
            raise ImproperInputError(
                "Parameter *algorithms* from method *jmoo.set_algorithms* can only take instances \
                or references of type *Algorithm*.")

        unique_stats = list(set(self._stats_to_track))
        if len(unique_stats) != len(self._stats_to_track):
            raise DuplicateStatError("A unique stat was provided twice.")

        stat_names = [stat.STAT_NAME for stat in self._stats_to_track]
        unique_stat_names = list(set(stat_names))
        if len(unique_stat_names) != len(stat_names):
            raise NonUniqueStatError("Provided stats are unique, but they do not have distinct names.")

    def run(self):
        """Core JMOO runner to execute MOO problem solving plan."""
        for problem in self._problems:
            for algorithm in self._algorithms:
                algorithm(problem, StatTracker(self._stats_to_track, problem, algorithm)).evolve()

    @property
    def population_size(self):
        """Gets the opulation size: the number of candidate solutions within each population."""
        return self._population_size

    @population_size.setter
    def population_size(self, population_size):
        """Sets the population size."""
        if not isinstance(population_size, int):
            raise ImproperInputError("Population size must be an integer.")
        self._population_size = population_size

    @property
    def generation_limit(self):
        """Gets the generation limit: the maximum number of generations that an EA searcher will run
        for before stopping."""
        return self._generation_limit

    @generation_limit.setter
    def generation_limit(self, num_generations):
        """Sets the generational limit."""
        if not isinstance(num_generations, int):
            raise ImproperInputError("Number of generations must be an integer.")
        self._generation_limit = num_generations

    @property
    def number_of_repeats(self):
        """Gets the number of repeats: the number of times to repeat the algorithm for statistical
        consideration."""
        return self._number_of_repeats

    @number_of_repeats.setter
    def number_of_repeats(self, num_repeats):
        """Sets the number of repeats for the algorithm to run on each problem."""
        if not isinstance(num_repeats, int):
            raise ImproperInputError("Number of repeats must be an integer.")
        self._number_of_repeats = num_repeats

    @property
    def random_seed(self):
        """Gets the random seed: the seed to propagate throughout the system for testing
        purposes."""
        return self._random_seed

    @random_seed.setter
    def random_seed(self, seed):
        """Sets the Random Seed."""
        if not isinstance(seed, int):
            raise ImproperInputError("Random seed must be an integer.")
        self._random_seed = seed
