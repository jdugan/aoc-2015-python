import hashlib
from src.utility.reader import Reader

class Day04:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 4

    def puzzle1(self):
        found = False
        seed  = self.__data()
        num   = 0
        while (not found):
            num   += 1
            found  = self.__test(seed, num, 5)
        return num


    def puzzle2(self):
        found = False
        seed  = self.__data()
        num   = 0
        while (not found):
            num   += 1
            found  = self.__test(seed, num, 6)
        return num


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== HASHING ===================================

    def __test(self, seed, num, size):
        str = f"{seed}{num}"
        res = hashlib.md5(str.encode())
        hex = res.hexdigest()
        return hex[:size] == "0"*size


    #========== DATA ======================================

    def __data(_):
        lines = Reader().to_lines("data/day04/input.txt")
        return lines[0]
