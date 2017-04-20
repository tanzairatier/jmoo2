# This file is part of JMOO.
#
#    JMOO is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    JMOO is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with JMOO.  If not, see < http: // www.gnu.org / licenses / >.

"""The selector for NSGA-II."""

from Base import Selector
from collections import defaultdict
from itertools import chain
from Errors import ImproperInputError

def do_NSGAII_select(num_to_select, population):
    """Selection scheme for identifying the best individuals in the population."""

    if num_to_select == 0:
        return []
    elif num_to_select < 0:
        raise ImproperInputError("Parameter *num_to_select* must not be negative.")

    #sort the population into bands
    sorted_bands = nondominated_sorting(num_to_select, population)

    #assign crowding distances for tie breakers
    for band in sorted_bands:
        assign_crowding_distance(band)
    
    #chain the bands (flatten the lists) into a single list
    selected_individuals = list(chain(*sorted_bands[:-1]))
    num_selected_individuals = len(selected_individuals)
    num_to_select = num_to_select - num_selected_individuals
    
    #break ties within bands using crowding distance
    if num_to_select - num_selected_individuals > 0:
        sorted_bands = sorted(sorted_bands[-1], key=lambda r: r.crowding_distance, reverse=True)
        selected_individuals.extend(sorted_bands[:num_to_select])    
    
    return selected_individuals

def nondominated_sorting(num_to_select, population):
    """Split the population into bands and sort the bands according to
    how they dominate each other."""
 
    individuals_grouping = defaultdict(list)
    nondominated_front = []
    next_best_front = []
    num_dominations_of = defaultdict(int)
    dominated_by = defaultdict(list)
    sorted_nondominated_fronts = [[]]

    #group fitnesses of individuals into groups based on their fitness
    for individual in population:
        if not individual.is_evaluated:
            individual.evaluate()
        individuals_grouping[individual].append(individual)
    bands = list(individuals_grouping.keys())
    
    #grab the first nondominated frontier and score the individuals
    #based on number of others they dominate
    for i, band_i in enumerate(bands):
        for band_j in bands[i+1:]:
            if band_i.dominates(band_j):
                num_dominations_of[band_j] += 1
                dominated_by[band_i].append(band_j)
            elif band_j.dominates(band_i):
                num_dominations_of[band_i] += 1
                dominated_by[band_j].append(band_i)
        if num_dominations_of[band_i] == 0:
            nondominated_front.append(band_i)
      
    for individual in nondominated_front:
        sorted_nondominated_fronts[-1].extend(individuals_grouping[individual])
    num_individuals_sorted = len(sorted_nondominated_fronts[-1])

    # Continue sorting until everyone's sorted or *num_to_select* is reached
    max_num_individuals_to_sort = min(len(population), num_to_select)
    while num_individuals_sorted < max_num_individuals_to_sort:
        sorted_nondominated_fronts.append([])
        for fit_p in nondominated_front:
            for fit_d in dominated_by[fit_p]:
                num_dominations_of[fit_d] -= 1
                if num_dominations_of[fit_d] == 0: #dominated only by one other
                    next_best_front.append(fit_d)
                    num_individuals_sorted += len(individuals_grouping[fit_d])
                    sorted_nondominated_fronts[-1].extend(individuals_grouping[fit_d])
        nondominated_front = next_best_front
        next_best_front = []
    
    return sorted_nondominated_fronts

def assign_crowding_distance(band):
    """Computes and assigns a crowding distance to a band of individuals."""

    distances = [0.0 for individual in band]
    crowd = [individual for individual in band]   
    number_of_objectives = len(band[0].fitness)
    
    for i in range(number_of_objectives):
        crowd.sort(key=lambda r: r.fitness[i])
        
        if crowd[-1].fitness[i] == crowd[0].fitness[i]:
            continue

        distances[0] = float("inf")
        distances[-1] = float("inf")

        norm = number_of_objectives * float(crowd[-1].fitness[i] - crowd[0].fitness[i])

        index = 1
        for prev, cur, next in zip(crowd[:-2], crowd[1:-1], crowd[2:]):
            distances[index] += (next.fitness[i] - prev.fitness[i]) / norm
            index += 1

    for i, distance in enumerate(distances):
        band[i].crowding_distance = distance

class NSGAIISelector:
    """Class that implements a selector base class for NSGA-II."""

    def __init__(self, population_size_desired, population):
        self._population_size_desired = population_size_desired
        self._population = population

    def select(self):
        return do_NSGAII_select(self._population_size_desired, self._population)

