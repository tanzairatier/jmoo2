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

"""Base module for storing Base Classes defining their abstract requirements and
providing common methods."""

import logging
import random
import sys
from .Errors import ObjectiveNotEvaluatedError, NullInputError, ImproperInputError, DecisionOutOfBoundsError

class Algorithm:
    """Base class for defining Algorithms for search problems."""

    NAME = "UnnamedAlgorithm"

    def __init__(self, problem, stat_tracker, settings):
        self._problem = problem
        self._stat_tracker = stat_tracker
        self._settings = settings
        self._problem.num_evaluations = 0

    def evolve(self):
        pass

class Mutator:
    """Base class for defining mutators: a method of perturbing individuals of a
    population."""

    def mutate(self):
        raise NotImplementedError()

class Populator:
    """Base class for populators, used in generating initial populations for algorithms."""

    def populate(self):
        raise NotImplementedError()

class Problem:
    """The Problem base class to extend when creating new problems for search.  Every
    defined problem must extend this base class and use its methods per the standard
    of defining new problems.
    """

    def __init__(self):
        # The number of times this problem was evaluated
        self.num_evaluations = 0

        # The decision structure of this problem
        self.decision_variables = None

        # The objectives of this problem
        self.objectives = None

    def assert_decision_variables_exist(self):
        """Asserts that the member *decision_variables* is set properly on the *self* class
        instance.  The decision variables would normally be set by the subclass of this
        Problem class.  If not, it will cause problems with some of the methods of this class.

        Args:
            self: A reference to the problem class instance.

        Returns:
            None

        Raises:
            DecisionVariableStructureError: Problem does not have any decision variables defined.
        """
        if self.decision_variables is None or not isinstance(self.decision_variables, list):
            raise DecisionVariableStructureError("Problem does not have any decision variables \
                defined.")

    def assert_objectives_exist(self):
        """Asserts that the member *objectives* is set properly on the *self* class
        instance.  The objectives would normally be defined by the subclass of this
        Problem class.  If not, it will cause problems with some of the methods of this class.

        Args:
            self: A reference to the problem class instance.

        Returns:
            None

        Raises:
            ObjectiveStructureError: Problem does not have any objectives or they
            are not defined properly
        """
        if self.objectives is None or not isinstance(self.objectives, list):
            raise ObjectiveStructureError("Problem does not have any decision variables or they \
                are not defined properly")

    def generate_input(self):
        """Randomly generate decision-inputs for a problem along a uniform distribution.
        This method is typically called within population populators that grow individuals
        that subscribe to a particular problem.

        All problems must define a decision variable structure.  If that has not been
        defined correctly, this method will raise an error.

        Args:
            self: A reference to the problem class instance.

        Returns:
            A list containing a single row of input for one individual subscribing to the
            problem, wherein the input is of the structure defined by decision variables.

        Raises:
            DecisionVariableStructureError: Cannot generate input because decision variables
            not defined properly.
        """

        self.assert_decision_variables_exist()

        return [random.uniform(decision_variable.lower_bound, decision_variable.upper_bound)
                for decision_variable in self.decision_variables]  # pylint: disable=E1133

    def evaluate(self, input = None):
        raise NotImplementedError()

    def evaluate_constraints(self, input = None):
        raise NotImplementedError()

    def initialize(self, decision_input=None):
        """Disibutes decision values into the value slot of decision variables of the problem
        so that it can be more readily accessed by evaluators of those decisions.

        This method is typically called before the *evaluate* function of every problem.

        Args:
            self: A reference to the problem class instance.
            decision_input: The values to be assigned for each decision variable.

        Returns:
            None

        Raises:
            DecisionVariableStructureError: Cannot assign decision values to decision variables
            because the decision variable structure was not defined properly.
            ImproperInputError: Provided *decision_input* to method *Problem.initialize must be
            a list and have length equal to the number of decision variables.
            NullInputError: Provided *decision_input* to method *Problem.initialize* must exist.
            DecisionOutOfBoundsError: "A *decision_input* was out of bounds in method
            *Problem.initialize*.
        """

        if not decision_input:
            raise NullInputError("Provided *decision_input* to method *Problem.initialize* must \
                exist.")

        self.assert_decision_variables_exist()

        if len(decision_input) != len(self.decision_variables):
            raise ImproperInputError("Provided *decision_input* to method *Problem.initialize \
                must be a list and have length equal to the number of decision variables.")

        for i, decision_variable in enumerate(self.decision_variables):
            if decision_input[i] < decision_variable.lower_bound or \
                    decision_input[i] > decision_variable.upper_bound:
                raise DecisionOutOfBoundsError("A *decision_input* was out of bounds in method \
                    *Problem.initialize*.")
            else:
                decision_variable.value = decision_input[i]

    def objective_values_as_list(self):
        """Returns the values assigned to objectives as a list.

        This method is typically used at the end of the *evaluate* function of every problem.

        Args:
            self: A reference to the problem class instance.

        Returns:
            A list representing the evaluation of decisions to the problem.

        Raises:
            ObjectiveStructureError: Cannot get value of an objective because its structure
            was not defined properly.
            ObjectiveNotEvaluatedError: Cannot get value of an objective because the objective
            has not yet been evaluated.
        """
        self.assert_objectives_exist()

        try:
            return [objective.value for objective in self.objectives]  # pylint: disable=E1133
        except AttributeError:
            raise ObjectiveNotEvaluatedError("Cannot get value of an objective because the \
                objective has not yet been evaluated")

class Reproducer:
    """Base class for defining a Reproducer used in algorithms."""
    def reproduce(self):
        raise NotImplementedError()

class ReturnPolicy:
    """Base class for defining a Return Policy for electing which 
    generation and stat to return as result of running algorithm."""

    def elect_generation(self, stat_tracker):
        raise NotImplementedError()

class Selector:
    """Base class for defining a Selector."""
    
    def select(self):
        raise NotImplementedError()

class Stat:
    """Base class for defining Stats for search problems."""

    STAT_NAME = "UnnamedStat"
    FORMATTER = "%10.3f"

    def collect(self):
        raise NotImplementedError()

class StoppingCriteria:
    """Base class for defining stopping criteria for algorithms."""

    def is_satisfied(self):
        raise NotImplementedError()
