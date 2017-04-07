
import random
from Problems.Schaffer import Schaffer
from Problems.Constrex import Constrex
from Problems.Fonseca import Fonseca
from StatTracker import StatTracker
from Stats.Median import Median
from Stats.Mean import Mean
from Stats.Evaluations import Evaluations

random.seed(1)



from Algorithms.Random_Evolution import Random_Evolution



Random_Evolution(None, Fonseca(), StatTracker([Median, Mean, Evaluations])).evolve()
    