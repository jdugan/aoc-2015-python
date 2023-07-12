import re

from src.utility.reader import Reader

class Day25:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 25

    def puzzle1(self):
        row, col = self.__coords()
        offset   = self.__offset(row, col)
        pos      = 1
        val      = 20151125
        while pos < offset:
            pos += 1
            val  = (val * 252533) % 33554393
        return val

    def puzzle2(self):
        return -2


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== PAPER =====================================

    def __offset(self, row, column):
        rect  = row * column
        upper = self.__triangle_area(row - 2)
        lower = self.__triangle_area(column - 1)
        return rect + upper + lower

    def __triangle_area(self, side):
        area = (side * (side + 1))//2
        return max([0, area])


    #========== DATA ======================================

    def __data(_):
        return Reader().to_lines("data/day25/input.txt")

    def __coords(self):
        m    = re.search(r'To continue, please consult the code grid in the manual.  Enter the code at row (\d+), column (\d+).', self.__data().pop())
        r, c = m.groups()
        return [int(r), int(c)]