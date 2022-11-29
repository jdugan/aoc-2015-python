import re
from src.utility.reader import Reader

class Day05:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 5

    def puzzle1(self):
        count = 0
        for line in self.__data():
            if self.__original_check(line):
                count += 1
        return count

    def puzzle2(self):
        count = 0
        for line in self.__data():
            if self.__adjusted_check(line):
                count += 1
        return count


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== CHECKERS ==================================

    def __adjusted_check(self, str):
        m1 = re.search(r'(..).*\1', str) is not None
        m2 = re.search(r'(.).\1', str) is not None
        return m1 and m2

    def __original_check(_, str):
        m1 = len(re.findall("a|e|i|o|u", str)) > 2
        m2 = re.search(r'(.)\1', str) is not None
        m3 = re.search("ab|cd|pq|xy", str) is not None
        return m1 and m2 and not m3


    #========== DATA ======================================

    def __data(_):
        lines = Reader().to_lines("data/day05/input.txt")
        return lines
