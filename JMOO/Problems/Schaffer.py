from Problem import Problem
from Decision import DecisionVariable
from Objective import Objective
from FriendlyErrors import ImproperInputError

class Schaffer(Problem):
    """Schaffer problem N1.
    J. D. Schaffer, “Some experiments in machine learning using vector evaluated genetic algorithms (artificial intelligence, optimization, adaptation, pattern recognition),” Ph.D. dissertation, Vanderbilt University, 1984.
    """

    NAME = "Schaffer"

    def __init__(self, boundary = 10):
        """constructor"""
        Problem.__init__(self)

        if not isinstance(boundary, int) and not isinstance(boundary, float):
            raise ImproperInputError()

        self.decision_variables = [DecisionVariable(-boundary, boundary, "x1")]
        self.objectives = [Objective("y1", less_is_more=True),
                           Objective("y2", less_is_more=True)]

    def evaluate(self, input = None):
        """evaluates fitness scores for this problem"""
        Problem.initialize(self, input)
        x1 = self.decision_variables[0].value
       
        self.objectives[0].value = x1**2
        self.objectives[1].value = (x1-2)**2
        
        return Problem.objective_values_as_list(self)

    def evaluate_constraints(self, input = None):
        pass