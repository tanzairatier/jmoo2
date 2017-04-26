# -*- coding: utf-8 -*-

from jmoo.JmooExperiment import JmooExperiment
from jmoo.Algorithms.NSGAII import NSGAII
from jmoo.Problems.Constrex import Constrex
from jmoo.Stats.Common import Evaluations, Mean, Median, Population
from jmoo.Criteria.Common import MaxGenerationsCriteria
from jmoo.ReturnPolicy.Common import ReturnEverything, ReturnEveryGeneration

J = JmooExperiment()
J.set_algorithms(NSGAII)
J.set_problems(Constrex)
J.set_stats_to_track(Population, Median, Mean, Evaluations)
J.set_settings({"Population Size": 100, 
                "Stopping Criteria": MaxGenerationsCriteria(10),
                "Print Stats": True, 
                "Random Seed": 1, 
                "Number of Repeats": 5,
                "Return Policy": ReturnEveryGeneration()})

experiment_results = J.run()







































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
    