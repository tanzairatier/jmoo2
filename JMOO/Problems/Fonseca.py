from math import exp, sqrt
from Problem import Problem
from Decision import DecisionVariable
from Objective import Objective
from Friendly_Errors import ImproperInputError

class Fonseca(Problem):
    """Fonseca and Fleming's problem
    C. M. Fonzeca and P. J. Fleming, “An overview of evolutionary algorithms in multiobjective optimization,” Evol Comput, vol. 3, no. 1, pp. 1-16, 1995.
    """

    def __init__(self, boundary = 4, num_variables = 2):
        """constructor"""
        Problem.__init__(self)

        if not isinstance(num_variables, int):
            raise ImproperInputError()

        if not isinstance(boundary, int) and not isinstance(boundary, float):
            raise ImproperInputError()

        self.decision_variables = [DecisionVariable(-boundary, boundary, "x"+str(i+1)) for i in range(num_variables)]
        self.objectives = [Objective("y1", less_is_more=True),
                           Objective("y2", less_is_more=True)]

    def evaluate(self, input = None):
        """evaluates fitness scores for this problem"""
        Problem.initialize(self, self.decision_variables, input)

        X = [decision_variable.value for decision_variable in self.decision_variables]
        self.objectives[0].value = 1 - exp( -sum([(x - 1/sqrt(len(self.decision_variables)))**2 for x in X]) )
        self.objectives[1].value = 1 - exp( -sum([(x + 1/sqrt(len(self.decision_variables)))**2 for x in X]) )
        
        return Problem.objective_values_as_list(self, self.objectives)

    def evaluate_constraints(self, input = None):
        pass
