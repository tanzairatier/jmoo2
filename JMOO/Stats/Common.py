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

"""Common stats for MOEAs to collect at the end of each generation."""

import numpy as np
from Base import Stat

class Population(Stat):
    """The entire population of each generation.  Use this stat in conjunction with
    Return policies."""

    STAT_NAME = "Population"
    FORMATTER = "DND" #do not display

    def __init__(self, population):
        self._population = population

    def collect(self):
        return self._population

class Evaluations(Stat):
    """The number of evaluations to a problem.
    
    This is a stub for defining some key constants."""
    
    STAT_NAME = "Evaluations"
    FORMATTER = "%d"

    def collect(self):
        pass

class Mean(Stat):
    """The mean on each objective of a population."""
    
    STAT_NAME = "Mean"
    FORMATTER = "%10.3f"

    def __init__(self, population):
        self._population = population
        

    def collect(self, do_not_evaluate = False):
        """return a vector representing the mean of each objective score"""

        if not do_not_evaluate:
            for individual in self._population:
                individual.evaluate()

        valid_individuals = [individual for individual in self._population if individual.is_evaluated]

        fitnesses = [individual.fitness for individual in valid_individuals]
        num_columns = len(fitnesses[0])
        fitness_as_columns = [[fitness[column_index] for fitness in fitnesses] for column_index in range(num_columns)]
        return [np.mean(fitness_column) for fitness_column in fitness_as_columns] 

class Median(Stat):
    """The median on each objective of a population"""
    
    STAT_NAME = "Median"
    FORMATTER = "%10.3f"

    def __init__(self, population):
        self._population = population
        

    def collect(self, do_not_evaluate = False):
        """return a vector representing the median of each objective score"""

        if not do_not_evaluate:
            for individual in self._population:
                individual.evaluate()

        valid_individuals = [individual for individual in self._population if individual.is_evaluated]

        fitnesses = [individual.fitness for individual in valid_individuals]
        num_columns = len(fitnesses[0])
        fitness_as_columns = [[fitness[column_index] for fitness in fitnesses] for column_index in range(num_columns)]
        return [np.percentile(fitness_column, 50) for fitness_column in fitness_as_columns] 