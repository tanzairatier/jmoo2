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

"""This module defines a *DecisionVariable* and a *Decision*.

Decision variables are stubs that define the structure of a decision (min,
max, etc).

Decisions are subscribers to a decision variable type and can also hold a value
that must fall within legal boundaries of its decision variable.
"""

import random
from Variable import Variable

class DecisionVariable(Variable):
    """Stores the structure of a decision to a problem.

    Decision variables are not meant to hold a value, however, for temporary
    purposes, it can.
    """

    def __init__(self, lower=None, upper=None, descript=""):
        Variable.__init__(self, lower, upper, descript)

    def generate_random_value(self):
        """Generates a random, legal value that falls within the legal boundaries
        of this decision variable, on a uniform distribution.

        Args:
            self: A reference to this decision variable.

        Returns:
            A floating point number that falls within the legal boundaries
            of this decision variable.

        Raises:
            Nothing
        """

        return random.uniform(self.lower_bound, self.upper_bound)

class Decision(Variable):
    """Stores a decision to a problem.  Decisions must subscribe to a
    decision variable and they must also have a value that falls within the
    legal boundaries of the decision variable it subscribes to."""

    def __init__(self, decision_structure, decision_value):
        #The structure of the decision
        self.structure = decision_structure

        #The value of the decision
        self.value = decision_value

    def __str__(self):
        return str(self.value)
    