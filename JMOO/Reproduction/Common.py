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

"""Common reproducers.  Use these to expand and create more individuals in algorithms."""

import random
from ..Base import Reproducer
from ..Core import Individual

class SimpleCrossover(Reproducer):
    """Generates an equal-size population of offspring by taking sequential pairs of parents
    to crossover their decisions (genes) in creating children (new individuals)."""

    def __init__(self, problem, population, crossover_rate):
        if crossover_rate > 1.0:
            crossover_rate = 1.0
        elif crossover_rate < 0.0:
            crossover_rate = 0.0
        self._crossover_rate = crossover_rate
        self._problem = problem
        self._population = population

    def reproduce(self):
        offspring = []
        midpt = int(len(self._population)/2)
        for individual_1, individual_2 in zip(self._population[:midpt], self._population[midpt:]):
            if random.random() < self._crossover_rate:
                crossover_point = int(min(len(individual_1), len(individual_2))/2)
                offspring.append(Individual(self._problem, list(individual_1[:crossover_point])+list(individual_2[crossover_point:])))
                offspring.append(Individual(self._problem, list(individual_2[:crossover_point])+list(individual_1[crossover_point:])))
            else:
                offspring.append(individual_1)
                offspring.append(individual_2)
        return offspring
