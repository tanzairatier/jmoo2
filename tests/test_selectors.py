from .context import *
import unittest
import random
from jmoo.Selection.Common import RandomSelector
from jmoo.Population.Common import RandomPopulator
from jmoo.Problems.Schaffer import Schaffer

class TestSelection(unittest.TestCase):
    def setUp(self):
        self._population_size = 200
        self._population_size_to_select = 100
        self._problem = Schaffer()
        self._population = RandomPopulator(self._problem, self._population_size).populate()

    def tearDown(self):
        pass
        
    def test_random_selector(self):
        """If we set the population size, make sure it is set correctly.  If not, ensure it was set to the default."""
        random_selector = RandomSelector(self._population_size_to_select, self._population)
        self._population = random_selector.select()
        self.assertEqual(len(self._population), self._population_size_to_select)

if __name__ == '__main__':
    unittest.main()
