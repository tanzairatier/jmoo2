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

"""Common algorithms for search problems."""

from Base import Algorithm
from Perturbation.Common import SimpleMutation
from Population.Common import RandomPopulator
from Reproduction.Common import SimpleCrossover
from Selection.Common import RandomSelection
from Criteria.Common import MaxGenerationsCriteria

class SGA(Algorithm):
    """The Simple Genetic Algorithm.  Beginning with a random population, randomly select
    a half of the population as the mating pool.  Perform simple crossover and mutation
    on the mating pool to restore population back to size and stop after 20 generations
    have been run."""

    NAME = "SGA"

    def __init__(self, problem, stat_tracker):
        self._problem = problem
        self._problem.num_evaluations = 0 #TODO: move this into base class
        self._stat_tracker = stat_tracker
        self._stopping_criteria = MaxGenerationsCriteria(20)

    def evolve(self):

        population = RandomPopulator(self._problem, 100).populate()

        self._stat_tracker.collect_stats(population)

        while not self._stopping_criteria.is_satisfied(self._stat_tracker):
            sub_pop = RandomSelection(50, population).select()
            population = SimpleCrossover(self._problem, sub_pop, 0.80).reproduce()
            population = SimpleMutation(0.08).mutate(population)
            
            self._stat_tracker.collect_stats(population)

        self._stat_tracker.pretty_print_stats()

class Random(Algorithm):
    """The 'Random' GA, which simply generates a random population repeatedly."""

    NAME = "Random"

    def __init__(self, problem, stat_tracker):
        self._problem = problem
        self._problem.num_evaluations = 0 #TODO: move this into base class
        self._stat_tracker = stat_tracker
        self._stopping_criteria = MaxGenerationsCriteria(20)

    def evolve(self):

        population = RandomPopulator(self._problem, 100).populate()

        self._stat_tracker.collect_stats(population)

        while not self._stopping_criteria.is_satisfied(self._stat_tracker):
            population = RandomPopulator(self._problem, 100).populate()
            
            self._stat_tracker.collect_stats(population)

        self._stat_tracker.pretty_print_stats()