import random

class Strength:
    """Sort the individuals according to the number of other individuals they dominate.  Then
    select the top *population_size_desired* individuals.

    This is based on the SPEA2 algorithm.
    """

    def __init__(self, tournament_size, population_size_desired, population):
        self._tournament_size = tournament_size
        self._population_size_desired = population_size_desired
        self._population = population

    def select(self):
        winners = []
        for i in range(self._population_size_desired):
            competitors = [random.choice(self._population) for j in range(self._tournament_size)]
            for competitor in competitors:
                if not competitor.is_evaluated:
                    competitor.evaluate()
            winners.append(max(competitors, key=lambda r: r.weighted_fitness))
        return winners