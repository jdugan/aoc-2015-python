import itertools

from src.utility.reader import Reader

class Day10:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 10;

    def puzzle1(self):
        term = self.__data()
        for _ in range(40):
            term = self.__look_say(term)
        return len(term)

    def puzzle2(self):
        term = self.__data()
        for _ in range(50):
            term = self.__look_say(term)
        return len(term)


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== HELPERS ===================================

    def __look_say(self, input):
        terms      = list(input)
        counts     = []
        curr_count = 1
        curr_term  = terms.pop(0)

        for next_term in terms:
            if curr_term == next_term:
                curr_count += 1
            else:
                counts.append((curr_count, curr_term))
                curr_count = 1
                curr_term  = next_term
        counts.append((curr_count, curr_term))

        digits = [str(d) for d in list(itertools.chain(*counts))]
        return "".join(digits)


    #========== DATA ======================================

    def __data(_):
        lines = Reader().to_lines("data/day10/input.txt")
        return lines[0]
