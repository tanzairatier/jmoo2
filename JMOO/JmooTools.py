from .Base import Algorithm, StoppingCriteria, Problem, ReturnPolicy, Stat
from .Core import ControlledExecution, StatTracker
from .Errors import ImproperInputError, DuplicateStatError, NonUniqueStatError
from .Criteria.Common import MaxEvaluationsCriteria
from .ReturnPolicy.Common import ReturnLastGeneration
from .Stats.Common import Evaluations, Mean, Median, Population
from .JmooExperiment import JmooExperiment
from .Population.Utils import get_local_frontier
import os, uuid

class JmooParetoFrontierGenerator:
    def __init__(self, problem, algorithm, settings = None):
        """Constructor."""
        self._settings = {"Population Size": 10000,
                          "Stopping Criteria": MaxEvaluationsCriteria(10000000),
                          "Return Policy": ReturnLastGeneration(),
                          "Random Seed": None,
                          "Number of Repeats": 1,
                          "Print Stats": True}
        experiment = JmooExperiment()
        experiment.set_algorithms(algorithm)
        experiment.set_problems(problem)
        experiment.set_stats_to_track(Population, Median, Mean, Evaluations)
        experiment.set_settings(self._settings)

        experiment_results = experiment.run()
        population = get_local_frontier(experiment_results[algorithm.NAME][problem.NAME][0])
       
        directory = "ParetoFrontiers"
        if not os.path.exists(directory):
            os.makedirs(directory)

        subdirectory = "ParetoFrontiers" + "/" + problem.NAME
        if not os.path.exists(subdirectory):
            os.makedirs(subdirectory)

        filename = subdirectory + "/" + algorithm.NAME + "(" + str(uuid.uuid1()) + ")" + ".txt"
        with open(filename, 'w') as out:
            for individual in population:
                out.write(",".join([str(fit) for fit in individual.fitness]) + "\n")


                


