class jmoo(object):
    DEFAULT_POPULATION_SIZE = 100
    DEFAULT_GENERATION_LIMIT = 20
    DEFAULT_NUMBER_OF_REPEATS = 1
    DEFAULT_RANDOM_SEED = None

    def __init__(self):
        self._population_size = jmoo.DEFAULT_POPULATION_SIZE
        self._generation_limit = jmoo.DEFAULT_GENERATION_LIMIT
        self._number_of_repeats = jmoo.DEFAULT_NUMBER_OF_REPEATS
        self._random_seed = jmoo.DEFAULT_RANDOM_SEED

    """ Population Size: the number of candidate solutions within each population."""
    @property
    def population_size(self):
        return self._population_size

    @population_size.setter
    def population_size(self, N):
        self._population_size = N

    """ Generation Limit: the maximum number of generations that an EA searcher will run for before stopping."""
    @property
    def generation_limit(self):
        return self._generation_limit

    @generation_limit.setter
    def generation_limit(self, N):
        self._generation_limit = N

    """ Number of Repeats: the number of times to repeat the algorithm for statistical consideration."""
    @property
    def number_of_repeats(self):
        return self._number_of_repeats

    @number_of_repeats.setter
    def number_of_repeats(self, N):
        self._number_of_repeats = N

    """ Random Seed: the seed to propagate throughout the system for testing purposes."""
    @property
    def random_seed(self):
        return self._random_seed

    @random_seed.setter
    def random_seed(self, N):
        self._random_seed = N


