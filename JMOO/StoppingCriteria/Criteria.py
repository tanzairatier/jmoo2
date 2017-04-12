from Friendly_Errors import ImproperInputError

class MaxGenerationsCriteria:
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



class MaxEvaluationsCriteria:
    """A stopping criteria that claims convergence after a maximum number of evaluations have been achieved."""

    def __init__(self, max_evaluations):
        if not isinstance(max_evaluations, int):
            raise ImproperInputError("Parameter *max_evaluations* must be an integer greater than zero.")
        if max_evaluations < 1:
            raise ImproperInputError("Parameter *max_evaluations* for MaxEvaluationsCriteria must be greater than zero.")
        self._max_evaluations = max_evaluations

    def is_satisfied(self, stat_tracker):
        if stat_tracker.get_latest_stat("Evaluations") >= self._max_evaluations:
            return True
        else:
            return False

    """ Max Generations: the maximum number of evaluations that criteria will be satisfied. """
    @property
    def max_evaluations(self):
        return self._max_evaluations
