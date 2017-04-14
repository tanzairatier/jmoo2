# -*- coding: utf-8 -*-

"""Tests for the Jmoo Core module."""

import unittest
import random
from core import Jmoo

class TestParameterSettings(unittest.TestCase):
    """Tests for parameter settings to the Jmoo Core module."""

    def setUp(self):
        """Setup a JMOO Object"""
        self.jmoo_runner = Jmoo()

    def tearDown(self):
        pass

    def test_pop_size_is_set_correctly(self):
        """If we set the population size, make sure it is set correctly.
        If not, ensure it was set to the default."""

        self.assertEqual(self.jmoo_runner.population_size, Jmoo.DEFAULT_POPULATION_SIZE)
        pop_size = random.uniform(10, 1000)
        self.jmoo_runner.population_size = pop_size
        self.assertEqual(pop_size, self.jmoo_runner.population_size)

    def test_gen_lim_is_set_correctly(self):
        """If we set the generation limit, it is set correctly.
        If not, ensure it was set to the default."""
        self.assertEqual(self.jmoo_runner.generation_limit, Jmoo.DEFAULT_GENERATION_LIMIT)
        gen_lim = random.uniform(10, 1000)
        self.jmoo_runner.generation_limit = gen_lim
        self.assertEqual(gen_lim, self.jmoo_runner.generation_limit)

    def test_num_repeats_set_correctly(self):
        """If we set the number of repeats, it is set correctly.
        If not, ensure it was set to the default."""
        self.assertEqual(self.jmoo_runner.number_of_repeats, Jmoo.DEFAULT_NUMBER_OF_REPEATS)
        num_reps = random.uniform(10, 1000)
        self.jmoo_runner.number_of_repeats = num_reps
        self.assertEqual(num_reps, self.jmoo_runner.number_of_repeats)

    def test_rand_seed_is_set_correctly(self):
        """If we set the random seed, it is set correctly.
        If not, ensure it was set to the default."""
        self.assertEqual(self.jmoo_runner.random_seed, Jmoo.DEFAULT_RANDOM_SEED)
        ran_seed = random.uniform(10, 1000)
        self.jmoo_runner.random_seed = ran_seed
        self.assertEqual(ran_seed, self.jmoo_runner.random_seed)

if __name__ == '__main__':
    unittest.main()
