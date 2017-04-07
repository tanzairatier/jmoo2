import random
from Friendly_Errors import DecisionOutOfBoundsError, NullInputError, ImproperInputError

class Problem:
    def __init__(self):
        self.num_evaluations = 0
        pass

    """base class representation of a problem with inputs, evaluation function and fitness-objective-outputs"""
    def generate_input(self):
        return [random.uniform(decision_variable.lower_bound, decision_variable.upper_bound) for decision_variable in self.decision_variables]
    
    def initialize(self, decision_variables, input = None):
        """used before the evaluate function of every problem
        inserts inputs to evaluate inside the decision objects for the probem"""
        if input:
            if len(input) != len(decision_variables):
                raise ImproperInputError()
            else:
                for i,decision_variable in enumerate(decision_variables):
                    if input[i] < decision_variable.lower_bound or input[i] > decision_variable.upper_bound:
                        raise DecisionOutOfBoundsError()
                    else:
                        decision_variable.value = input[i]
        else:
            raise NullInputError()

    def objective_values_as_list(self, objectives):
        """used at the end of the evaluate function of every problem
        gets the fitness scores as a list"""
        return [objective.value for objective in objectives]