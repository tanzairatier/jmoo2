# -*- coding: utf-8 -*-

import JmooExperiment
from Algorithms.Common import SGA, Random
from Algorithms.NSGAII import NSGAII
from Problems.Fonseca import Fonseca
from Problems.Constrex import Constrex
from Stats.Common import Evaluations, Mean, Median, Population
from Stats.MeasuresOfSpread import Diversity
from Criteria.Common import MaxGenerationsCriteria
from Population.Utils import get_local_frontier
J = JmooExperiment.JmooExperiment()
J.set_algorithms(NSGAII)#SGA, Random)
J.set_problems(Fonseca(num_variables=2))
J.set_stats_to_track(Population, Median, Mean, Evaluations, Diversity)
J.set_settings({"Population Size": 100, "Stopping Criteria": MaxGenerationsCriteria(10),"Print Stats": True})
run_stats = J.run()


"""
population = get_local_frontier(run_stats["NSGAII"]["Fonseca"][0])
import seaborn  as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_context("notebook", font_scale=1.1)
sns.set_style("ticks")

df = pd.DataFrame({'x': [ind.fitness[0] for ind in population],
                    'y': [ind.fitness[1] for ind in population]})
sns.lmplot('x', 'y',
            data=df,
            fit_reg=False
            )

plt.title('Fonseca - NSGAII')
plt.xlabel('f1')
plt.ylabel('f2')
plt.show()
"""
    