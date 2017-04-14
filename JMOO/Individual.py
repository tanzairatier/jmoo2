class Individual:
    def __init__(self, problem, decisions, fitness = None):
        self._problem = problem
        self._decisions = decisions
        self._fitness = fitness
        self._set_weighted_fitness()

    def _set_weighted_fitness(self):
        if self._fitness:
            self._weighted_fitness = [-1.0 * fitness if objective.less_is_more else 1.0 * fitness for fitness,objective in zip(self._fitness, self._problem.objectives)]

    def rounded(self, n):
        return [round(decision.value, n) for decision in self._decisions]

    def evaluate(self):
        if self._fitness is None:
            self._fitness = self._problem.evaluate(input = self.get_decision_values())
            self._set_weighted_fitness()
            self._problem.num_evaluations += 1

    def get_decision_values(self):
        return [decision.value for decision in self._decisions]

    def dominates(self, other):
        """self dominates other if self is not worse on any objective than other and better on at least one"""
        better_than = False
        for me,him in zip(self._weighted_fitness, other.weighted_fitness):
            if me > him:
                better_than = True
            elif me < him:
                return False
        return better_than

    def __eq__(self, other):
        return self.fitness == other.fitness

    def __str__(self):
        return "[" + ",".join([str(decision) for decision in self._decisions]) + "]"

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return self._decisions

    def __getitem__(self, i):
        return self._decisions[i]

    def __len__(self):
        return len(self._decisions)

    """ Decisions: an individual's decisions to its problem."""
    @property
    def decisions(self):
        return self._decisions

    """ Determines if the individual has been evaluated or not."""
    @property
    def is_evaluated(self):
        return self._fitness is not None

    """ Fitness: objective score evaluations for an individual's decisions."""
    @property
    def fitness(self):
        return self._fitness

    """ Weighted Fitness: objective score evaluations with -1 or +1 weights to control which is better."""
    @property
    def weighted_fitness(self):
        return self._weighted_fitness