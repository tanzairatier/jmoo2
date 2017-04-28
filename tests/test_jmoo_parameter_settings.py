# -*- coding: utf-8 -*-

"""Tests for the Jmoo Core module."""

import unittest
import random
from jmoo.JmooExperiment import JmooExperiment
from jmoo.Errors import ImproperInputError

class TestParameterSettings(unittest.TestCase):
    """Tests for parameter settings to the Jmoo Core module."""

    def setUp(self):
        """Setup a JMOO Object"""
        self.jmoo_runner = JmooExperiment()

    def tearDown(self):
        pass

    def test_pop_size_is_set_correctly(self):
        """If we set the population size, make sure it is set correctly.
        If not, ensure it was set to the default."""

        self.assertEqual(self.jmoo_runner._settings["Population Size"], JmooExperiment.DEFAULT_SETTINGS["Population Size"])
        pop_size = int(random.uniform(10, 1000))
        self.jmoo_runner.set_settings({"Population Size": pop_size})
        self.assertEqual(self.jmoo_runner._settings["Population Size"], pop_size)
        self.assertRaises(ImproperInputError, self.jmoo_runner.set_settings, settings = {"Population Size": "invalid thing"})
        self.assertRaises(ImproperInputError, self.jmoo_runner.set_settings, settings = {"Population Size": -9}), 

    def test_num_repeats_set_correctly(self):
        """If we set the number of repeats, it is set correctly.
        If not, ensure it was set to the default."""
        self.assertEqual(self.jmoo_runner._settings["Number of Repeats"], JmooExperiment.DEFAULT_SETTINGS["Number of Repeats"])
        num_repeats = int(random.uniform(10, 1000))
        self.jmoo_runner.set_settings({"Number of Repeats": num_repeats})
        self.assertEqual(self.jmoo_runner._settings["Number of Repeats"], num_repeats)

    def test_rand_seed_is_set_correctly(self):
        """If we set the random seed, it is set correctly.
        If not, ensure it was set to the default."""
        self.assertEqual(self.jmoo_runner._settings["Random Seed"], JmooExperiment.DEFAULT_SETTINGS["Random Seed"])
        random_seed = int(random.uniform(10, 1000))
        self.jmoo_runner.set_settings({"Random Seed": random_seed})
        self.assertEqual(self.jmoo_runner._settings["Random Seed"], random_seed)

if __name__ == '__main__':
    unittest.main()
