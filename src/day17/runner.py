import itertools

from src.utility.reader import Reader

class Day17:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 17

    def puzzle1(self):
        containers = self.__containers()
        limit      = 150
        max        = self.__max_items(containers, limit)
        min        = self.__min_items(containers, limit)
        count      = 0
        for i in range(min, max):
            for c in itertools.combinations(containers, i):
                if sum(c) == limit:
                    count += 1
        return count

    def puzzle2(self):
        containers = self.__containers()
        limit      = 150
        max        = self.__max_items(containers, limit)
        min        = self.__min_items(containers, limit)
        count      = 0
        for i in range(min, max):
            for c in itertools.combinations(containers, i):
                if sum(c) == limit:
                    count += 1
            if count > 0:
                break
        return count


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== HELPERS ===================================

    def __max_items(self, list, limit):
        sum = 0
        num = 0
        for idx, item in enumerate(list):
            sum += item
            if sum >= limit:
                num = idx + 1
                break
        return num

    def __min_items(self, list, limit):
        sum = 0
        num = 0
        list.reverse()
        for idx, item in enumerate(list):
            sum += item
            if sum >= limit:
                num = idx + 1
                break
        return num


    #========== DATA ======================================

    def __data(_):
        lines = Reader().to_lines("data/day17/input.txt")
        return lines

    def __containers(self):
        containers = [int(s) for s in self.__data()]
        containers.sort()
        return containers
