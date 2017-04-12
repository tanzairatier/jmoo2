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
        
    def test_individual_evaluation(self):
        """If we evaluate an individual, check that its fitness and weighted fitness are correct."""
        median_stat = Median(self.population)
        medians = median_stat.collect()
        self.assertEquals(round(medians[0],3), 0.769) 
        self.assertEquals(round(medians[1],3), 0.792)


if __name__ == '__main__':
    unittest.main()
