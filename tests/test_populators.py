from .context import *
import unittest
import random
from jmoo.Population.Common import RandomPopulator
from jmoo.Problems.Schaffer import Schaffer

class TestPopulation(unittest.TestCase):
    def setUp(self):
        self._problem = Schaffer() 
        self._population_size = 100
        self._population = []

    def tearDown(self):
        pass
        
    def test_random_populator(self):
        """Ensure that random population works properly"""
        random_populator = RandomPopulator(self._problem, self._population_size)
        self._population = random_populator.populate()
        self.assertEqual(len(self._population), self._population_size)
        for individual in self._population:
            for decision in individual.decisions:
                self.assertTrue(decision.value >= decision.structure.lower_bound and decision.value <= decision.structure.upper_bound)

if __name__ == '__main__':
    unittest.main()
