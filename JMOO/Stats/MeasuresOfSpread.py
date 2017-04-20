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

from Population.Utils import get_local_frontier
from Base import Stat
import numpy as np

class Diversity(Stat):
    """The diversity of a population of individuals."""
    
    STAT_NAME = "Diversity"
    FORMATTER = "%10.3f"

    def __init__(self, population):
        self._population = population
        
    def compute_diversity(self, population):
        """ Computes the diversity of a population without regard to its "optimal" frontier.  That is:
         1) extract the local frontier of non-dominated individuals within the population
         2) sort the local frontier lexicographically
         3) compute d_i = distance between a member of the local frontier and the next member in order
         4) compute d_bar = average of all the d_i
         5) return the diversity, computed as the ratio: (sum{1 to N-1}(|d_i - d_bar|)) / ((N-1)*d_bar)

        Args:
            population: The population to compute diversity for

        Returns:
            A floating point number representing the diversity of the population

        Raises:
            AssertionError: if members in the population have unequal fitness lengths
        """

        #The number of individuals in the population
        n = len(population)

        if n == 0:
            return 0.0

        #The length of fitness objects; i.e. the number of objectives
        L = len(population[0].fitness)

        for individual in population:
            if len(population[0].fitness) != L:
                raise AssertionError("Method *diversity* of class *Diversity*: All members of the population must have the same number of objectives in their fitness score.")

        #Extract local pareto frontier of non-dominated individuals and then sort them
        local_frontier = get_local_frontier(population)
        local_frontier.sort(key=lambda r: r.fitness)
    
        #The number of individuals in the local pareto frontier
        N = len(local_frontier)

        if N <= 1:
            return 0.0

        d = [0.0] * (N-1)
        for i in range(len(d)):
           d[i] = np.sqrt(sum( [ (local_frontier[i].fitness[j] - local_frontier[i+1].fitness[j])**2 for j in range(L)  ]  ))
        d_bar = sum(d)/len(d)
        if (d_bar == 0): return 0
        delta = (sum(abs(d_i - d_bar) for d_i in d))/((N-1) * d_bar )
        return delta

    def collect(self, do_not_evaluate = False):
        """Return a floating point number representing the diversity metric.
        
        This method must exist in every stat.

        Args:
            do_not_evaluate: A boolean representing whether or not to evaluate
            any individuals that do not have a fitness.  If not evaluated, the
            individual will not be considered as part of the collected stat.

        Returns:
            A floating point number representing the diversity of the population

        Raises:
            Nothing
        """

        if not do_not_evaluate:
            for individual in self._population:
                individual.evaluate()

        valid_individuals = [individual for individual in self._population if individual.is_evaluated]

        return self.compute_diversity(valid_individuals)
