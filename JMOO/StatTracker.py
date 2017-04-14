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

"""This module contains a stat tracker approach to maintaining and collecting
stats for a population of individuals as they are evolved through some
algorithm.

StatTracker accepts Stat objects as a list of measurements to be taken after
every generation in an evolutionary algorithm.
"""

import math

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

    def pretty_print_stats(self):
        printables = []
        header = ["Generation"] + list(self._stat_containers.keys())
        printables.append(header)
        for generation in range(self.num_generations + 1):
            row_printables = [str("%d" % generation)]

            for stat in self._stats_to_track:
                vals = self._stat_containers[stat.STAT_NAME][generation]
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
