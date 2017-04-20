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

from Base import Algorithm, Problem, Stat
from Core import ControlledExecution, StatTracker
from Errors import ImproperInputError, DuplicateStatError, NonUniqueStatError
from Criteria.Common import MaxGenerationsCriteria
from ReturnPolicy.Common import ReturnLastGeneration
import _thread
import logging


class JmooExperiment():
    """Core Jmoo for defining MOO problem and solution scenarios.

    Example usage:
    TODO: update Jmoo example usage
    """

    DEFAULT_POPULATION_SIZE = 100
    DEFAULT_GENERATION_LIMIT = 20
    DEFAULT_NUMBER_OF_REPEATS = 1
    DEFAULT_RANDOM_SEED = None

    DEFAULT_SETTINGS = {"Population Size": 100,
                                "Print Stats": True,
                                "Stopping Criteria": MaxGenerationsCriteria(50),
                                "Return Policy": ReturnLastGeneration()
                        }

    def __init__(self):
        """Constructor."""

        self._population_size = JmooExperiment.DEFAULT_POPULATION_SIZE
        self._generation_limit = JmooExperiment.DEFAULT_GENERATION_LIMIT
        self._number_of_repeats = JmooExperiment.DEFAULT_NUMBER_OF_REPEATS
        self._random_seed = JmooExperiment.DEFAULT_RANDOM_SEED
        self._settings = JmooExperiment.DEFAULT_SETTINGS

        #List of algorithms to run on each problem
        self._algorithms = []

        #List of problems to run under each algorithm
        self._problems = []

        #List of stats to collect in each generation of an algorithm running a problem
        self._stats_to_track = []

        #Setup logging
        #logging.basicConfig(filename='example.log',level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #logging.info('- JMOO Core was loaded successfuly.')

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
        
        with ControlledExecution():
            try:
                for algorithm in algorithms:
                    if isinstance(algorithm, Algorithm):
                        raise ImproperInputError("Method requires an Algorithm class reference.")
                    if issubclass(algorithm, Algorithm):
                        self._algorithms.append(algorithm)
            except:
                raise ImproperInputError("Method requires an Algorithm class reference.")

            logging.info('- Algorithms were set successfully.')

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

        with ControlledExecution():
            try:
                for problem in problems:
                    if isinstance(problem, Problem):
                        self._problems.append(problem)
                    elif issubclass(problem, Problem):
                        self._problems.append(problem())
            except:
                raise ImproperInputError("Method requires an instance of, or a class reference to Problem.")

            logging.info('- Problems were set successfully.')

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

        with ControlledExecution():
            try:
                for stat in stats_to_track:
                    if isinstance(stat, Stat):
                        raise ImproperInputError("Method requires an instance of, or a class reference to Stat.")
                    if issubclass(stat, Stat):
                        self._stats_to_track.append(stat)
            except:
                raise ImproperInputError("Method requires an instance of, or a class reference to Stat.")

            unique_stats = list(set(self._stats_to_track))
            if len(unique_stats) != len(self._stats_to_track):
                raise DuplicateStatError("A unique stat was provided twice.")

            stat_names = [stat.STAT_NAME for stat in self._stats_to_track]
            unique_stat_names = list(set(stat_names))
            if len(unique_stat_names) != len(stat_names):
                raise NonUniqueStatError("Provided stats are unique, but they do not have distinct names.")

            logging.info('- Stats were set successfully.')

    def set_settings(self, settings):
        """Takes settings in form of dictionary and updates them into Jmoo Experiment's settings."""

        if isinstance(settings, dict):
            self._settings.update(settings)

    def run(self):
        """Core JMOO runner to execute MOO problem solving plan."""

        with ControlledExecution():
            run_stats = {}   
            for algorithm in self._algorithms:
                run_stats[algorithm.NAME] = {}
                for problem in self._problems:
                    run_stats[algorithm.NAME][problem.NAME] = []
                    run_stats[algorithm.NAME][problem.NAME].append(algorithm(problem, StatTracker(self._stats_to_track, problem, algorithm), self._settings).evolve())
            logging.info('- Run of algorithms on problems occurred successfully.')
            return run_stats

    @property
    def population_size(self):
        """Gets the opulation size: the number of candidate solutions within each population."""

        with ControlledExecution():
            return self._population_size

    @population_size.setter
    def population_size(self, population_size):
        """Sets the population size."""

        with ControlledExecution():
            if not isinstance(population_size, int):
                raise ImproperInputError("Population size must be an integer.")
            self._population_size = population_size

    @property
    def generation_limit(self):
        """Gets the generation limit: the maximum number of generations that an EA searcher will run
        for before stopping."""

        with ControlledExecution():
            return self._generation_limit

    @generation_limit.setter
    def generation_limit(self, num_generations):
        """Sets the generational limit."""

        with ControlledExecution():
            if not isinstance(num_generations, int):
                raise ImproperInputError("Number of generations must be an integer.")
            self._generation_limit = num_generations

    @property
    def number_of_repeats(self):
        """Gets the number of repeats: the number of times to repeat the algorithm for statistical
        consideration."""
        
        with ControlledExecution():
            return self._number_of_repeats

    @number_of_repeats.setter
    def number_of_repeats(self, num_repeats):
        """Sets the number of repeats for the algorithm to run on each problem."""

        with ControlledExecution():
            if not isinstance(num_repeats, int):
                raise ImproperInputError("Number of repeats must be an integer.")
            self._number_of_repeats = num_repeats

    @property
    def random_seed(self):
        """Gets the random seed: the seed to propagate throughout the system for testing
        purposes."""
        with ControlledExecution():
            return self._random_seed

    @random_seed.setter
    def random_seed(self, seed):
        """Sets the Random Seed."""
        
        with ControlledExecution():
            if not isinstance(seed, int):
                raise ImproperInputError("Random seed must be an integer.")
            self._random_seed = seed
