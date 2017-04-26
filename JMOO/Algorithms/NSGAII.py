from ..Base import Algorithm
from ..Perturbation.Common import SimpleMutation
from ..Population.Common import RandomPopulator
from ..Selection.NSGAII import NSGAIISelector
from ..Reproduction.Common import SimpleCrossover

class NSGAII(Algorithm):
    """NSGA-II Algorithm."""

    NAME = "NSGAII"

    def __init__(self, problem, stat_tracker, settings):
        Algorithm.__init__(self, problem, stat_tracker, settings)

    def evolve(self):

        population = RandomPopulator(self._problem, self._settings["Population Size"]).populate()

        self._stat_tracker.collect_stats(population)

        while not self._settings["Stopping Criteria"].is_satisfied(self._stat_tracker):
            sub_pop = NSGAIISelector(int(self._settings["Population Size"]/2), population).select()
            population = sub_pop + SimpleCrossover(self._problem, sub_pop, 0.80).reproduce()
            population = SimpleMutation(0.08).mutate(population)
            
            self._stat_tracker.collect_stats(population)

        if self._settings["Print Stats"]:
            self._stat_tracker.pretty_print_stats()

        return self._settings["Return Policy"].elect_generation(self._stat_tracker)