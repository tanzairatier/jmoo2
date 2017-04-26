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

"""Core classes for building and running Jmoo Experiments."""

import logging
import math
import random
import sys
from .Errors import ImproperInputError

class ControlledExecution:
    def __enter__(self):
        return ""
    def __exit__(self, type, value, trace):
        if type:
            print("An ERROR of type " + type.__name__ + " occurred:")
            print(" * " + value.args[0])
            print(" * ")
            print(" * Stack Trace:")
            frame = trace.tb_frame
            frame_count = 0
            while frame:# and frame_count < 3:
                print(" * * " + frame.f_code.co_filename + ":" + str(frame.f_code.co_firstlineno))
                frame = frame.f_back       
                frame_count += 1 
            #logging.error('- ERROR: ' + type.__name__ + ".  " + value.args[0]) 
            sys.exit(1)

class Variable(object):
    """Core class that stores a variable that can have a boundary and description."""

    def __init__(self, lower=None, upper=None, descript=""):
        """Initializes a variable object with boundary and description.

        Args:
            lower: A float/int representing the lower boundary (inclusive)
            upper: A float/int representing the upper boundary (inclusive)
            descript: A string that describes the variable

        Returns:
            None

        Raises:
            ImproperInputError: If boundaries are not float/int, or if
            description is not a string, or if upper <= lower.
        """

        if not isinstance(lower, int) and not isinstance(lower, float):
            raise ImproperInputError("Lower boundary must be a float or int.")

        if not isinstance(upper, int) and not isinstance(upper, float):
            raise ImproperInputError("Upper boundary must be a float or int.")

        if not isinstance(descript, str):
            raise ImproperInputError("Description must be a string.")

        if upper <= lower:
            raise ImproperInputError("Upper boundary must be greater than lower \
                boundary.")

        self.lower_bound = lower
        self.upper_bound = upper
        self.description = descript

class Decision(Variable):
    """Core class that stores a decision to a problem.  Decisions must subscribe to a
    decision variable and they must also have a value that falls within the
    legal boundaries of the decision variable it subscribes to."""

    def __init__(self, decision_structure, decision_value):
        #The structure of the decision
        self.structure = decision_structure

        #The value of the decision
        self.value = decision_value

    def __str__(self):
        return str(self.value)
    
class DecisionVariable(Variable):
    """Core class that sores the structure of a decision to a problem.

    Decision variables are not meant to hold a value, however, for temporary
    purposes, it can.
    """

    def __init__(self, lower=None, upper=None, descript=""):
        Variable.__init__(self, lower, upper, descript)

    def generate_random_value(self):
        """Generates a random, legal value that falls within the legal boundaries
        of this decision variable, on a uniform distribution.

        Args:
            self: A reference to this decision variable.

        Returns:
            A floating point number that falls within the legal boundaries
            of this decision variable.

        Raises:
            Nothing
        """

        return random.uniform(self.lower_bound, self.upper_bound)

class Individual:
    """Core individual class for defining an individual that subscribes to a problem, can be evaluated
    to have a fitness and can dominate other individuals."""

    def __init__(self, problem, decisions, fitness = None):
        self._problem = problem
        self._decisions = decisions
        self._fitness = fitness
        self._set_weighted_fitness()

    def _set_weighted_fitness(self):
        if self._fitness:
            self._weighted_fitness = [-1.0 * fitness if objective.less_is_more else 1.0 * fitness for fitness,objective in zip(self._fitness, self._problem.objectives)]

    def rounded(self, n):
        return [round(decision.value, n) for decision in self._decisions]

    def evaluate(self):
        if self._fitness is None:
            self._fitness = self._problem.evaluate(input = self.get_decision_values())
            self._set_weighted_fitness()
            self._problem.num_evaluations += 1

    def get_decision_values(self):
        return [decision.value for decision in self._decisions]

    def dominates(self, other):
        """self dominates other if self is not worse on any objective than other and better on at least one"""
        better_than = False
        for me,him in zip(self._weighted_fitness, other.weighted_fitness):
            if me > him:
                better_than = True
            elif me < him:
                return False
        return better_than

    def __hash__(self):
        return hash(tuple(self._fitness))

    def __eq__(self, other):
        return self.fitness == other.fitness

    def __str__(self):
        return "[" + ",".join([str(decision) for decision in self._decisions]) + "]"

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return self._decisions

    def __getitem__(self, i):
        return self._decisions[i]

    def __len__(self):
        return len(self._decisions)

    """ Decisions: an individual's decisions to its problem."""
    @property
    def decisions(self):
        return self._decisions

    """ Determines if the individual has been evaluated or not."""
    @property
    def is_evaluated(self):
        return self._fitness is not None

    """ Fitness: objective score evaluations for an individual's decisions."""
    @property
    def fitness(self):
        return self._fitness

    """ Weighted Fitness: objective score evaluations with -1 or +1 weights to control which is better."""
    @property
    def weighted_fitness(self):
        return self._weighted_fitness

class Objective(Variable):
    """Core class for storing objectives for problems."""

    def __init__(self, descript="", less_is_more=True):
        Variable.__init__(self, -math.inf, math.inf, descript)
        self.less_is_more = less_is_more

class StatTracker:
    def __init__(self, stats_to_track, problem, algorithm):
        """Initializes the stat tracker with a list of stats to track along with
        the problem and algorithm to monitor.

        Args:
            self: A reference to this stat tracker object.
            stats_to_track: A list of stats to track.  Each one must be a Stat object.
            problem: A problem reference of type *Problem*.
            algorithm: An algorithm reference of type *Algorithm*.

        Returns:
            None

        Raises:
            ImproperInputError: if the provided problem is not a Problem type or if
            the provided algorithm is not an Algorithm type or if any provided stat
            is not a *Stat* type.
        """

        self._stats_to_track = stats_to_track
        self._stat_containers = {stat.STAT_NAME: [] for stat in stats_to_track}
        self.num_generations = -1
        self._problem = problem
        self._algorithm = algorithm

    def collect_stats(self, population):
        self.num_generations += 1
        for stat in self._stats_to_track:
            if stat.STAT_NAME == "Evaluations":
                self._stat_containers[stat.STAT_NAME].append(
                    self._problem.num_evaluations)
            else:
                self._stat_containers[stat.STAT_NAME].append(
                    stat(population).collect())

    def get_latest_stat(self, stat_name):
        """ Returns the requested stat's last collected data point.
        """
        return self._stat_containers[stat_name][-1]

    def get_every(self, stat_name):
        return self._stat_containers[stat_name]

    def get_everything(self):
        return self._stat_containers

    def pretty_print_stats(self):
        printables = []
        header = ["Generation"] + [stat.STAT_NAME for stat in self._stats_to_track if not stat.FORMATTER == "DND"]
        printables.append(header)
        for generation in range(self.num_generations + 1):
            row_printables = [str("%d" % generation)]

            for stat in self._stats_to_track:
                vals = self._stat_containers[stat.STAT_NAME][generation]
                if not stat.FORMATTER == "DND": #code for do not display
                    if isinstance(vals, list):
                        row_printables.append(
                            str([(str(stat.FORMATTER % value)) for value in vals]).replace("'", ""))
                    else:
                        row_printables.append(
                            str(stat.FORMATTER % vals).strip('"\''))
            printables.append(row_printables)

        printables_by_column = [
            [printable[i] for printable in printables] for i in range(len(printables[0]))]

        max_char_widths_by_column = [len(max(printable_column, key=lambda r: len(
            r))) for printable_column in printables_by_column]

        full_row_width = sum(max_char_widths_by_column) + \
            len(max_char_widths_by_column) * 3 - 1

        print("┏" + "━".join(["━" + ("{0:━>" + str(max_char_widths_by_column[c]) + "}").format(
            "") + "━" for c, cell in enumerate(printables[0])]) + "┓")
        description = "Algorithm Used: " + self._algorithm.NAME + \
            ", Problem Used: " + self._problem.NAME + "."
        print("┃" + " " * (int(math.floor(full_row_width / 2) - math.floor(len(description) / 2))) +
              description + " " *
              (int(math.ceil(full_row_width / 2) - math.ceil(len(description) / 2))) + "┃")
        print("┣" + "┳".join(["━" + ("{0:━>" + str(max_char_widths_by_column[c]) + "}").format(
            "") + "━" for c, cell in enumerate(printables[0])]) + "┫")
        for i, printable in enumerate(printables):
            print("┃" + "┃".join([" " + ("{0: >" + str(max_char_widths_by_column[c]) + "}").format(
                cell) + " " for c, cell in enumerate(printable)]) + "┃")
            if i == 0:
                print("┣" + "╋".join(["━" + ("{0:━>" + str(max_char_widths_by_column[c]) + \
                    "}").format(
                    "") + "━" for c, cell in enumerate(printables[0])]) + "┫")
        print("┗" + "┻".join(["━" + ("{0:━>" + str(max_char_widths_by_column[c]) + "}").format(
            "") + "━" for c, cell in enumerate(printables[0])]) + "┛")

