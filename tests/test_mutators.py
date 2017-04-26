from .context import *
import unittest
import random
from jmoo.Population.Common import RandomPopulator
from jmoo.Problems.Schaffer import Schaffer
from jmoo.Perturbation.Common import SimpleMutation

class TestMutation(unittest.TestCase):
    def setUp(self):
        random.seed(1)
        self._problem = Schaffer() 
        self._population_size = 100
        self._population = RandomPopulator(self._problem, self._population_size).populate()

    def tearDown(self):
        pass
        
    def test_mutator(self):
        """Ensure that random mutation works properly"""
        mutator = SimpleMutation(0.10)
        self._population = mutator.mutate(self._population)
        for individual in self._population:
            for decision in individual.decisions:
                self.assertTrue(decision.value >= decision.structure.lower_bound and decision.value <= decision.structure.upper_bound)
        print(self._population[0])
        self.assertTrue(self._population[0], "7.400203103532796")

if __name__ == '__main__':
    unittest.main()


