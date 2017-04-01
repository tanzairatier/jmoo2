import unittest
import random
from Selection import Random_Selection

class TestSelection(unittest.TestCase):
    def setUp(self):
        self._population_size_we_want = 100
        self._population = [(random.uniform(-100,100), random.uniform(-100, 100)) for i in range(200)] 

    def tearDown(self):
        pass
        
    def test_random_selector(self):
        """If we set the population size, make sure it is set correctly.  If not, ensure it was set to the default."""
        random_selector = Random_Selection.Random_Selector(self._population_size_we_want, self._population)
        self._population = random_selector.select()
        self.assertEqual(len(self._population), self._population_size_we_want)

if __name__ == '__main__':
    unittest.main()
