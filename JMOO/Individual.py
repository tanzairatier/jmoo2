class Individual:
    def __init__(self, problem, decisions):
        self._problem = problem
        self._decisions = decisions

    """ Decisions: an individuals decisions to its problem."""
    @property
    def decisions(self):
        return self._decisions