from .context import *
import unittest
import random
from jmoo.Criteria.Common import MaxGenerationsCriteria
from jmoo.Problems.Fonseca import Fonseca

class TestCriteria(unittest.TestCase):
    def setUp(self):
        random.seed(1)
        self.max_number_generations = 15

    def tearDown(self):
        pass
        
    def test_max_generations_criteria(self):
        criteria = MaxGenerationsCriteria(self.max_number_generations)
        self.assertEquals(criteria.max_generations, self.max_number_generations)


if __name__ == '__main__':
    unittest.main()
