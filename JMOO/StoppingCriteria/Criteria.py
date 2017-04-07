class MaxGenerationsCriteria:
    """A stopping criteria that claims convergence after a maximum number of generations have been achieved."""

    def __init__(self, max_generations):
        self._max_generations = max_generations

    def is_satisfied(self, stat_tracker):
        if stat_tracker.num_generations >= self._max_generations:
            return True
        else:
            return False
