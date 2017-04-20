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

"""Common selectors.  Use these to select best candidates from a pool."""

import random
from Base import Selector

class RandomSelection(Selector):
    """given a population of candidates, down-select the pool to a fixed number"""
    def __init__(self, population_size_desired, population):
        self._population_size_desired = population_size_desired
        self._population = population

    def select(self):
        num_to_deselect = len(self._population) - self._population_size_desired
        while num_to_deselect > 0:
            self._population.remove(random.choice(self._population))
            num_to_deselect -= 1
        return self._population

class SimpleTournament:
    """Select the *population_size_desired* number of individuals from *population* via 
    tournaments of *tournament_size* individuals, with winners selected by comparing
    their fitnesses lexicographically.

    Competitors are chosen randomly with replacement from the population.

    Competitors that haven't been evaluated will be evaluated here.
    """

    def __init__(self, tournament_size, population_size_desired, population):
        self._tournament_size = tournament_size
        self._population_size_desired = population_size_desired
        self._population = population

    def select(self):
        winners = []
        for i in range(self._population_size_desired):
            competitors = [random.choice(self._population) for j in range(self._tournament_size)]
            for competitor in competitors:
                if not competitor.is_evaluated:
                    competitor.evaluate()
            winners.append(max(competitors, key=lambda r: r.weighted_fitness))
        return winners