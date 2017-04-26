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

"""Common populators.  Use these to get initial populations for algorithms."""

from ..Base import Populator
from ..Core import Decision, Individual

class RandomPopulator(Populator):
    """The Random Populator.  Generates a population of individuals that
    subscribe to a given population along a random uniform distribution."""

    def __init__(self, problem, population_size):
        #Number of individuals in the population
        self._population_size = population_size

        #The population of individuals
        self._population = []

        #The problem individuals in population subscribe to
        self._problem = problem

    def populate(self):
        """Main method to generate individuals for this populator."""

        return [Individual(self._problem, [Decision(decision_variable, decision_variable.generate_random_value()) for decision_variable in self._problem.decision_variables]) for i in range(self._population_size)]