from Problem import Problem
from Decision import Decision
from Objective import Objective

class Schaffer(Problem):
    def __init__(self, a = 10):
        """constructor"""
        self.decisions = [Decision(-a, a, "x1")]
        self.objectives = [Objective("y1", less_is_more=True),
                           Objective("y2", less_is_more=True)]

    def evaluate(self, input = None):
        """evaluates fitness scores for this problem"""
        Problem.initialize(self, self.decisions, input)
        x1 = self.decisions[0].value
       
        self.objectives[0].value = x1**2
        self.objectives[1].value = (x1-2)**2
        
        return Problem.objective_values_as_list(self, self.objectives)
