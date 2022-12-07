import re

from src.utility.reader import Reader

class Day16:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 16

    def puzzle1(self):
        match = 0
        for id, sue in self.__sues().items():
            if self.__simple_matcher(sue):
                match = id
                break
        return match

    def puzzle2(self):
        match = 0
        for id, sue in self.__sues().items():
            if self.__complex_matcher(sue):
                match = id
                break
        return match


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== HELPERS ===================================

    def __complex_matcher(self, sue):
        result = True
        truth  = self.__ticker_tape()
        for k, v in sue.items():
            match k:
                case 'cats' | 'trees':
                    if truth[k] >= v:
                        result = False
                        break
                case 'goldfish' | 'pomeranians':
                    if truth[k] <= v:
                        result = False
                        break
                case _:
                    if truth[k] != v:
                        result = False
                        break
        return result

    def __simple_matcher(self, sue):
        result = True
        truth  = self.__ticker_tape()
        for k, v in sue.items():
            if truth[k] != v:
                result = False
                break
        return result


    #========== DATA ======================================

    def __data(_):
        lines = Reader().to_lines("data/day16/input.txt")
        return lines

    def __sues(self):
        sues = {}
        for line in self.__data():
            mline   = re.search(r'^Sue (\d+): (.+)$', line)
            id, str = mline.groups()
            traits  = list(str.split(", "))
            sue     = {}
            for t in traits:
                mtrait = re.search(r'^(\w+): (\d+)$', t)
                k, v   = mtrait.groups()
                sue[k] = int(v)
            sues[int(id)] = sue
        return sues

    def __ticker_tape(_):
        return {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1,
        }
