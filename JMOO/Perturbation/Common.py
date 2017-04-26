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

"""Common perturbers-mutators-etc.  Use these to change populations on the chance
that the changes would luck into finding good solutions."""

import random
from ..Base import Mutator
from ..Core import Decision, Individual

class SimpleMutation(Mutator):
    """Simple mutation which randomly chooses an individual of a population to mutate
    based on a random (usually small) chance.  This mutator simply re-generates all decisions
    whenever an individual is chosen to mutate."""

    def __init__(self, mutation_rate):
        if mutation_rate > 1.0:
            mutation_rate = 1.0
        elif mutation_rate < 0.0:
            mutation_rate = 0.0
        self._mutation_rate = mutation_rate

    def mutate(self, population):
        mutated_population = []
        for member in population:
            if random.random() < self._mutation_rate:
                mutated_population.append(Individual(member._problem, [Decision(decision_variable, decision_variable.generate_random_value()) for decision_variable in member._problem.decision_variables]))
            else:
                mutated_population.append(member)
        return mutated_population