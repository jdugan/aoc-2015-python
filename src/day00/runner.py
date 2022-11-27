from src.utility.reader import Reader

class Day00:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(self):
        return 0

    def puzzle1(self):
        return -1

    def puzzle2(self):
        return -2


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    def __data(self):
        lines = Reader().to_lines("data/day00/input.txt")
        return lines
