import re
from src.utility.reader import Reader

class Day08:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 8

    def puzzle1(self):
        diff = 0
        for line in self.__data():
            length = len(line)
            line   = re.sub(r'\\\\', "*", line)
            line   = re.sub(r'\\\"', "*", line)
            line   = re.sub(r'\\x\w{2}', "*", line)
            line   = re.sub(r'\"', "", line)
            diff  += (length - len(line))
        return diff

    def puzzle2(self):
        diff = 0
        for line in self.__data():
            length = len(line)
            line   = re.sub(r'\\', r'\\\\', line)
            line   = re.sub(r'\"', r'\\"', line)
            line   = f"\"{line}\""
            diff  += (len(line) - length)
        return diff


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== DATA ======================================

    def __data(_):
        lines = Reader().to_lines("data/day08/input.txt")
        return lines
