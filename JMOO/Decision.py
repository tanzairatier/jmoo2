import random
from Variable import Variable

class DecisionVariable(Variable):
    """class for storing the structure of a decision to a problem"""
    def __init__(self, lower = None, upper = None, descript = ""):
        Variable.__init__(self, lower, upper, descript)
    def generate_random_value(self):
        return random.uniform(self.lower_bound, self.lower_bound)

class Decision(Variable):
    """class for storing decision values to a problem"""
    def __init__(self, decision_structure, decision_value):
        self.structure = decision_structure
        self.value = decision_value
    