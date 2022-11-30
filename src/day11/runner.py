from src.utility.reader import Reader

class Day11:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------
    # Weirdly, these were easiest to do with the old
    # human comuter rather than code. Maybe I'll come
    # back later and do it the hard way?
    # -----------------------------------------------------
    def day(_):
        return 11

    def puzzle1(self):
        return "hxbxxyzz"

    def puzzle2(self):
        return "hxcaabcc"


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== DATA ======================================

    def __data(_):
        lines = Reader().to_lines("data/day11/input.txt")
        return lines[0]
