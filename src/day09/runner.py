import itertools
import re

from src.utility.reader import Reader

class Day09:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 9

    def puzzle1(self):
        return self.__best_distance(999999999, min)

    def puzzle2(self):
        return self.__best_distance(-999999999, max)


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== CALCULATION ===============================

    def __best_distance(self, limit, comparator):
        nodes  = self.__nodes()
        cities = list(nodes.keys())
        paths  = [list(path) for path in list(itertools.permutations(cities))]
        best   = limit

        for path in paths:
            curr = 0
            orig = path.pop(0)
            for dest in path:
                if dest in nodes[orig]:
                    curr += nodes[orig][dest]
                else:
                    curr = limit
                    break
                orig = dest
            best = comparator([curr, best])

        return best


    #========== DATA ======================================

    def __data(_):
        lines = Reader().to_lines("data/day09/input.txt")
        return lines

    def __nodes(self):
        nodes = {}
        for line in self.__data():
            match     = re.findall(r'^(\w+) to (\w+) = (\d+)$', line)
            c1, c2, d = match[0]

            n1        = nodes[c1] if c1 in nodes else {}
            n1[c2]    = int(d)
            nodes[c1] = n1

            n2        = nodes[c2] if c2 in nodes else {}
            n2[c1]    = int(d)
            nodes[c2] = n2
        return nodes
