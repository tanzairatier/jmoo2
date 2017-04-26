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

"""Common stopping criteria.  Use these to tell an algorithm when to stop."""

from ..Base import StoppingCriteria
from ..Errors import ImproperInputError, InvalidSetupError

class MaxGenerationsCriteria(StoppingCriteria):
    """A stopping criteria that claims convergence after a maximum number of generations have been achieved."""

    def __init__(self, max_generations):
        if not isinstance(max_generations, int):
            raise ImproperInputError("Parameter *max_generations* must be an integer greater than zero.")
        if max_generations < 1:
            raise ImproperInputError("Parameter *max_generations* for MaxGenerationsCriteria must be greater than zero.")
        self._max_generations = max_generations

    def is_satisfied(self, stat_tracker):
        if stat_tracker.num_generations >= self._max_generations:
            return True
        else:
            return False

    """ Max Generations: the maximum number of generations that criteria will be satisfied. """
    @property
    def max_generations(self):
        return self._max_generations

class MaxEvaluationsCriteria(StoppingCriteria):
    """A stopping criteria that claims convergence after a maximum number of evaluations have been achieved."""

    def __init__(self, max_evaluations):
        if not isinstance(max_evaluations, int):
            raise ImproperInputError("Parameter *max_evaluations* must be an integer greater than zero.")
        if max_evaluations < 1:
            raise ImproperInputError("Parameter *max_evaluations* for MaxEvaluationsCriteria must be greater than zero.")

        self._max_evaluations = max_evaluations

    def is_satisfied(self, stat_tracker):
        try:
            number_of_evaluations = stat_tracker.get_latest_stat("Evaluations")
        except:
            raise InvalidSetupError("Tried to use MaxEvaluationsCriteria without collecting an Evaluations stat.")

        if number_of_evaluations >= self._max_evaluations:
            return True
        else:
            return False

    """ Max Generations: the maximum number of evaluations that criteria will be satisfied. """
    @property
    def max_evaluations(self):
        return self._max_evaluations