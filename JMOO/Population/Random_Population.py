from Individual import Individual
from Decision import Decision

class Random_Populator:
    def __init__(self, problem, population_size):
        self._population_size = population_size
        self._population = []
        self._problem = problem
    def populate(self):
        return [Individual(self._problem, [Decision(decision_variable, decision_variable.generate_random_value()) for decision_variable in self._problem.decision_variables]) for i in range(self._population_size)]