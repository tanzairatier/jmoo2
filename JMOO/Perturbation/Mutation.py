import random
from Individual import Individual
from Decision import Decision

class Mutator:
    def __init__(self, mutation_rate):
        if mutation_rate > 1.0:
            mutation_rate = 1.0
        elif mutation_rate < 0.0:
            mutation_rate = 0.0
        #Logger.Warn("Mutation rate set to within boundaries of [0,1].")
        self._mutation_rate = mutation_rate

    def mutate(self, population):
        mutated_population = []
        for member in population:
            if random.random() < self._mutation_rate:
                mutated_population.append(Individual(member._problem, [Decision(decision_variable, decision_variable.generate_random_value()) for decision_variable in member._problem.decision_variables]))
            else:
                mutated_population.append(member)
        return mutated_population