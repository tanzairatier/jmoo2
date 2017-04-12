from decimal import Decimal

class StatTracker:
    def __init__(self, stats_to_track):
        self._stats_to_track = stats_to_track
        self._stat_containers = {stat.STAT_NAME: [] for stat in stats_to_track}
        self.num_generations = -1

    def collect_stats(self, population, problem):
        self.num_generations += 1
        for stat in self._stats_to_track:
            if stat.STAT_NAME == "Evaluations":
                self._stat_containers[stat.STAT_NAME].append(problem.num_evaluations)
            else:
                self._stat_containers[stat.STAT_NAME].append(stat(population).collect())
            
    def get_latest_stat(self, stat_name):
        """ Returns the requested stat's last collected data point.
        """
        return self._stat_containers[stat_name][-1]

    def pretty_print_stats(self):
        printables = []
        header = ["Generation"] + list(self._stat_containers.keys())
        printables.append(header)
        for generation in range(self.num_generations+1):
            row_printables = [str("%d" % generation)]

            for stat in self._stats_to_track:
                vals = self._stat_containers[stat.STAT_NAME][generation]
                if isinstance(vals, list):
                    row_printables.append(str([(str(stat.FORMATTER % value)) for value in vals]).replace("'", ""))
                else:
                    row_printables.append(str(stat.FORMATTER % vals).strip('"\''))
            printables.append(row_printables)

        printables_by_column = [ [printable[i] for printable in printables]  for i in range(len(printables[0]))]
        max_char_widths_by_column = [len(max(printable_column, key=lambda r: len(r))) for printable_column in printables_by_column]
        print("┏" + "┳".join(["━" + ("{0:━>"+str(max_char_widths_by_column[c])+"}").format("") + "━" for c,cell in enumerate(printables[0])]) + "┓")
        for i,printable in enumerate(printables):
            print("┃" + "┃".join([" " + ("{0: >"+str(max_char_widths_by_column[c])+"}").format(cell) + " " for c,cell in enumerate(printable)]) + "┃")
            if i == 0:
                print("┣" + "╋".join(["━" + ("{0:━>"+str(max_char_widths_by_column[c])+"}").format("") + "━" for c,cell in enumerate(printables[0])]) + "┫")
        print("┗" + "┻".join(["━" + ("{0:━>"+str(max_char_widths_by_column[c])+"}").format("") + "━" for c,cell in enumerate(printables[0])]) + "┛")