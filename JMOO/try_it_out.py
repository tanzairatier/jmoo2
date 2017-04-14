# -*- coding: utf-8 -*-

import random
from Problems.Schaffer import Schaffer
from Problems.Constrex import Constrex
from Problems.Fonseca import Fonseca
from StatTracker import StatTracker
from Stats.Common import Median, Mean, Evaluations
from Stats.MeasuresOfSpread import Diversity


random.seed(1)


import core
from Algorithms.Random_Evolution import Random_Evolution



#Random_Evolution(None, Constrex(), StatTracker([Median, Mean, Evaluations])).evolve()



J = core.Jmoo()
J.set_algorithms(Random_Evolution)
J.set_problems(Fonseca(num_variables=10), Constrex, Schaffer())
J.set_stats_to_track(Median, Mean, Evaluations, Diversity)
J.run()
    