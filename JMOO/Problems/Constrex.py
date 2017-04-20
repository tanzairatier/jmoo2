from Base import Problem
from Core import DecisionVariable, Objective
from Errors import ImproperInputError

class Constrex(Problem):
    """Constr-Ex problem by Deb.
    Deb, Kalyanmoy (2002) Multiobjective optimization using evolutionary algorithms (Repr. ed.). Chichester [u.a.]: Wiley. ISBN 0-471-87339-X.
    """
    NAME = "Constrex"

    def __init__(self):
        """constructor"""
        Problem.__init__(self)

        self.decision_variables = [DecisionVariable(0.1, 1.0, "x1"), DecisionVariable(0, 5, "x2")]
        self.objectives = [Objective("y1", less_is_more=True),
                           Objective("y2", less_is_more=True)]

    def evaluate(self, input = None):
        """evaluates fitness scores for this problem"""
        Problem.initialize(self, input)

        X = [decision_variable.value for decision_variable in self.decision_variables]
        self.objectives[0].value = X[0]
        self.objectives[1].value = (1+X[1])/X[0]
        
        return Problem.objective_values_as_list(self)

    def evaluate_constraints(self, input = None):
        """Evaluates the constraints, returning true if input is legal."""
        Problem.initialize(self, input)
        X = [decision_variable.value for decision_variable in self.decision_variables]

        return X[1] + 9*X[0] >= 6 and \
               -X[1] + 9*X[0] >= 1