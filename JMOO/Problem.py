import random

class Problem:
    """base class representation of a problem with inputs, evaluation function and fitness-objective-outputs"""
    def generate_input(self):
        return [random.uniform(decision.lower_bound, decision.upper_bound) for decision in self.decisions]
    
    def initialize(self, decision_variables, input = None):
        """used before the evaluate function of every problem
        inserts inputs to evaluate inside the decision objects for the probem"""
        if input:
            for i,decision_variable in enumerate(decision_variables):
                decision_variable.value = input[i]

    def objective_values_as_list(self, objectives):
        """used at the end of the evaluate function of every problem
        gets the fitness scores as a list"""
        return [objective.value for objective in objectives]