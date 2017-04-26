from .context import *
import unittest
import random
from Individual import Individual
from Problems.Fonseca import Fonseca
from Population import Random_Population
from Stats.Median import Median

class TestStatCollection(unittest.TestCase):
    def setUp(self):
        random.seed(1)
        self.problem = Fonseca(num_variables = 2, boundary = 1)
        self.population = Random_Population.Random_Populator(self.problem, population_size = 3).populate()

    def tearDown(self):
        pass
       


if __name__ == '__main__':
    unittest.main()
