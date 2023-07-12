from src.utility.reader import Reader

class Day20:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------
    # NB! The methods work from 0 and stepping by 1. The
    # non-standard values were added after the answer was
    # known to speed up regression tests.
    #------------------------------------------------------

    def day(_):
        return 20

    def puzzle1(self):
        limit = self.__data()
        step  = 10
        num   = 825000 - step
        hsum  = 0
        while (hsum * 10) < limit:
            num  += step
            hs    = self.__factors(num)
            hsum  = sum(hs)
        return num

    # 887040 => too high
    def puzzle2(self):
        limit      = self.__data()//11 + 1
        step       = 1
        num        = 850000 - step
        hsum       = 0
        while hsum < limit:
            num       += step
            elf_floor  = num//50
            hs         = list(filter(lambda h: h >= elf_floor, self.__factors(num)))
            hsum       = sum(hs)
        return num


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== CALCULATIONS ==============================

    def __factors(self, num):
        factors = []
        step    = 1 if num % 2 == 0 else 2
        for i in range(1, int(num**0.5) + 1, step):
            j = num//i
            if num == i * j:
                factors.append(i)
                factors.append(j)
        factors.sort()
        return factors


    #========== DATA ======================================

    def __data(_):
        lines = Reader().to_lines("data/day20/input.txt")
        return int(lines[0])
