import itertools
import re

from src.utility.reader import Reader

class Day13:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 13

    def puzzle1(self):
        guests       = self.__guests()
        anchor       = guests.pop(0)
        arrangements = []
        for perm in list(itertools.permutations(guests)):
            a = list(perm)
            a.insert(0, anchor)
            a.append(anchor)
            arrangements.append(a)

        return self.__best_score(arrangements)

    def puzzle2(self):
        guests       = self.__guests()
        arrangements = [list(perm) for perm in list(itertools.permutations(guests))]

        return self.__best_score(arrangements)


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== GUESTS ====================================

    def __guests(self):
        return list(self.__scale().keys())


    #========== SCORING ===================================

    def __best_score(self, arrangements):
        scale = self.__scale()
        best  = -9999999
        for arrangement in arrangements:
            partner = arrangement.pop(0)
            curr    = 0
            for person in arrangement:
                curr += self.__score_pair(scale, partner, person)
                partner = person
            if curr > best:
                best = curr
        return best

    def __score_pair(self, scale, name1, name2):
        dir1  = scale[name1][name2]
        dir2  = scale[name2][name1]
        return dir1 + dir2


    #========== DATA ======================================

    def __data(_):
        lines = Reader().to_lines("data/day13/input.txt")
        return lines

    def __scale(self):
        scale = {}
        curr  = None

        for line in self.__data():
            match = re.search(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)', line)
            name1, sign, amount, name2 = match.groups()

            if name1 != curr:
                curr = name1
                scale[name1] = {}

            if sign == "gain":
                scale[name1][name2] = int(amount)
            else:
                scale[name1][name2] = 0 - int(amount)

        return scale
