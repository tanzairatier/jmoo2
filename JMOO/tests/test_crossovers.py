from .context import *
import unittest
import random
from Problems.Fonseca import Fonseca
from Population import Random_Population
from Reproduction import Crossover

class TestCrossovers(unittest.TestCase):
    def setUp(self):
        random.seed(1)
        self._problem = Fonseca() 
        self._population_size = 6
        self._population = Random_Population.Random_Populator(self._problem, self._population_size).populate()

    def tearDown(self):
        pass
        
    def test_crossover(self):
        """Ensure that the crossover working properly"""
        
        crosser = Crossover.Crossover(self._problem, self._population, 1.0)
        offspring = crosser.crossover()
        self.assertEquals(offspring[0].rounded(3), [round(-2.9250860471007902, 3), round(2.3097868090841054, 3)])

if __name__ == '__main__':
    unittest.main()
