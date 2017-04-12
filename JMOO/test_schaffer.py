
import random
from Problems.Schaffer import Schaffer
from Problems.Constrex import Constrex
from Problems.Fonseca import Fonseca
from StatTracker import StatTracker
from Stats.Median import Median
from Stats.Mean import Mean
from Stats.Evaluations import Evaluations

random.seed(1)


import jmoo
from Algorithms.Random_Evolution import Random_Evolution



#Random_Evolution(None, Constrex(), StatTracker([Median, Mean, Evaluations])).evolve()



J = jmoo.jmoo()
J.set_algorithms(Random_Evolution)

"""can provide problem classes (will be instanced to default params) or problem instances (with specified params)"""
J.set_problems([Fonseca(num_variables=10), Constrex, Schaffer()])

J.run()
    