from .context import *
import unittest
import random
from jmoo.Core import Individual
from jmoo.Problems.Fonseca import Fonseca
from jmoo.Population.Common import RandomPopulator

class TestParameterSettings(unittest.TestCase):
    def setUp(self):
        self.problem = Fonseca(num_variables = 2)
        self.population = RandomPopulator(self.problem, population_size = 2).populate()

    def tearDown(self):
        pass
        
    def test_individual_evaluation(self):
        """If we evaluate an individual, check that its fitness and weighted fitness are correct."""
        for individual in self.population:
            individual.evaluate()
            self.assertEquals(individual.fitness[0] * -1.0, individual.weighted_fitness[0])
            self.assertEquals(individual.fitness[1] * -1.0, individual.weighted_fitness[1])


if __name__ == '__main__':
    unittest.main()
