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
            

    def pretty_print_stats(self):
        printables = []
        header = ["Generation"] + list(self._stat_containers.keys())
        #print(",".join(header))
        printables.append(header)
        for generation in range(self.num_generations):
            row_printables = []
            for col_name in header:
                if col_name == "Generation":
                    row_printables.append(str("%d" % generation))
                else:
                    if isinstance(self._stat_containers[col_name][generation], list):
                        row_printables.append(str([str("%5f" %  value) for value in self._stat_containers[col_name][generation]]))
                    else:
                        row_printables.append(str("%d" % self._stat_containers[col_name][generation]))
            #print(",".join(row_printables))
            printables.append(row_printables)

        printables_by_column = [ [printable[i] for printable in printables]  for i in range(len(printables[0]))]
        max_char_widths_by_column = [len(max(printable_column, key=lambda r: len(r))) for printable_column in printables_by_column]

        print("┏" + "━" * (sum(max_char_widths_by_column)+2*len(max_char_widths_by_column)+3) + "┓")
        for i,printable in enumerate(printables):
            print("┃" + "┃".join([" " + ("{0: >"+str(max_char_widths_by_column[c])+"}").format(cell) + " " for c,cell in enumerate(printable)]) + "┃")
            if i == 0:
                print("┃" + "━" * (sum(max_char_widths_by_column)+2*len(max_char_widths_by_column)+3) + "┃")
        print("┗" + "━" * (sum(max_char_widths_by_column)+2*len(max_char_widths_by_column)+3) + "┛")