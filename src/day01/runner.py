from src.utility.reader import Reader

class Day01:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 1

    def puzzle1(self):
        increments = [self.__char_to_increment(c) for c in self.__data()]
        return sum(increments)

    def puzzle2(self):
        floor = 0
        step  = 0

        for c in self.__data():
            step  += 1
            floor += self.__char_to_increment(c)
            if (floor == -1):
                break

        return step


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    def __char_to_increment(self, c):
        if c == "(":
            return 1
        return -1

    def __data(self):
        lines = Reader().to_lines("data/day01/input.txt")
        return [s for s in lines[0]]
