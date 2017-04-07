import random

class Tournament:
    """Select the *population_size_desired* number of individuals from *population* via 
    tournaments of *tournament_size* individuals, with winners selected by comparing
    their fitnesses lexicographically.

    Competitors are chosen randomly with replacement from the population.

    Competitors that haven't been evaluated will be evaluated here.
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