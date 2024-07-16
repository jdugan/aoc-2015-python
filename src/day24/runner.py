import itertools
import math

from src.utility.reader import Reader

class Day24:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 24

    def puzzle1(self):
        weights = self.__weights()
        groups  = self.__coziest_groups(weights, 3)
        qes     = [math.prod(g[0]) for g in groups]
        return min(qes)

    def puzzle2(self):
        weights = self.__weights()
        groups  = self.__coziest_groups(weights, 4)
        qes     = [math.prod(g[0]) for g in groups]
        return min(qes)


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== PACKING ===================================

    def __coziest_groups(self, weights, size):
        count    = len(weights)
        avg      = sum(weights)//size
        groups   = []
        for i in range(1, count + 1):
            cs = []
            for c in itertools.combinations(weights, i):
                if sum(c) == avg:
                    if size > 1:
                        ws = list(filter(lambda w: w not in c, weights))
                        gs = self.__coziest_groups(ws, size - 1)
                        if len(gs):
                            for g in gs:
                                cs.append([c] + g)
                            break
                    else:
                        cs.append([c])
                        break
            if len(cs):
                groups = [list(c) for c in cs]
                break
        return groups


    #========== DATA ======================================

    def __data(_):
        return Reader().to_lines("data/day24/input.txt")

    def __weights(self):
        ws = [int(w) for w in self.__data()]
        ws.sort()
        return ws