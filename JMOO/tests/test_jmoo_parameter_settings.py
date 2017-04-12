from .context import *
import unittest
import random
from jmoo.jmoo import jmoo

class TestParameterSettings(unittest.TestCase):
    def setUp(self):
        """Setup a JMOO Object"""
        self.J = jmoo()

    def tearDown(self):
        pass
        
    def test_population_size_is_set_correctly(self):
        """If we set the population size, make sure it is set correctly.  If not, ensure it was set to the default."""
        self.assertEqual(self.J.population_size, jmoo.DEFAULT_POPULATION_SIZE)      
        pop_size = random.uniform(10,1000)
        self.J.population_size = pop_size
        self.assertEquals(pop_size, self.J.population_size)

    def test_generation_limit_is_set_correctly(self):
        """If we set the generation limit, it is set correctly.  If not, ensure it was set to the default."""
        self.assertEqual(self.J.generation_limit, jmoo.DEFAULT_GENERATION_LIMIT)
        gen_lim = random.uniform(10,1000)
        self.J.generation_limit = gen_lim
        self.assertEquals(gen_lim, self.J.generation_limit)

    def test_number_of_repeats_is_set_correctly(self):
        """If we set the number of repeats, it is set correctly.  If not, ensure it was set to the default."""
        self.assertEqual(self.J.number_of_repeats, jmoo.DEFAULT_NUMBER_OF_REPEATS)
        num_reps = random.uniform(10,1000)
        self.J.number_of_repeats = num_reps
        self.assertEquals(num_reps, self.J.number_of_repeats)

    def test_random_seed_is_set_correctly(self):
        """If we set the random seed, it is set correctly.  If not, ensure it was set to the default."""
        self.assertEqual(self.J.random_seed, jmoo.DEFAULT_RANDOM_SEED)
        ran_seed = random.uniform(10,1000)
        self.J.random_seed = ran_seed
        self.assertEquals(ran_seed, self.J.random_seed)

if __name__ == '__main__':
    unittest.main()
