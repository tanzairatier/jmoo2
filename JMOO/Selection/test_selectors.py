import unittest
import random
from Selection import Random_Selection
from Population import Random_Population
from Problems import Schaffer

class TestSelection(unittest.TestCase):
    def setUp(self):
        self._population_size = 200
        self._population_size_to_select = 100
        self._problem = Schaffer.Schaffer()
        self._population = Random_Population.Random_Populator(self._problem, self._population_size).populate()

    def tearDown(self):
        pass
        
    def test_random_selector(self):
        """If we set the population size, make sure it is set correctly.  If not, ensure it was set to the default."""
        random_selector = Random_Selection.Random_Selector(self._population_size_to_select, self._population)
        self._population = random_selector.select()
        self.assertEqual(len(self._population), self._population_size_to_select)

if __name__ == '__main__':
    unittest.main()
