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

"""Common utilities for methods related to populations."""

def get_local_frontier(population):
    """Extracts the local optimal frontier from a population.  This is defined
    as the set of individuals from the population that are dominated by no other.

    Args:
        population: The population of individuals to extract local frontier from.

    Returns:
        A list of individuals representing the local frontier.

    Raises:
        Nothing.
    """

    local_frontier = []

    for individual in population:
        #Whether or not this individual is dominated
        is_dominated = False

        #Whether or not this individual has an identical twin
        has_twin = False

        #The list of other individuals that this individual dominates
        to_remove = []

        for index,other in enumerate(local_frontier):
            if other.dominates(individual):
                is_dominated = True
                break
            elif individual.dominates(other):
                to_remove.append(index)
            elif individual == other:
                has_twin = True
                break     
                  
        for index in reversed(to_remove): 
            del local_frontier[index]

        if not is_dominated and not has_twin:
            local_frontier.append(individual)

    return local_frontier