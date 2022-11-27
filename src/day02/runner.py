from src.utility.reader import Reader

class Day02:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 2

    def puzzle1(self):
        sizes = [self.__calculate_paper_size(dims) for dims in self.__data()]
        return sum(sizes)

    def puzzle2(self):
        sizes = [self.__calculate_ribbon_size(dims) for dims in self.__data()]
        return sum(sizes)


    # -----------------------------------------------------
    # Private Methods
    # ------------------------------------------------------

    #========== CALCULATIONS ===============================

    def __calculate_paper_size(self, dims):
        base  = (2 * dims[0] * dims[1]) + (2 * dims[0] * dims[2]) + (2 * dims[1] * dims[2])
        extra = dims[0] * dims[1]
        return base + extra

    def __calculate_ribbon_size(self, dims):
        base  = (2 * dims[0]) + (2 * dims[1])
        extra = dims[0] * dims[1] * dims[2]
        return base + extra


    #========== DATA ======================================

    def __data(self):
        lines = Reader().to_lines("data/day02/input.txt")
        dims  = []
        for line in lines:
            strs = line.split("x")
            ints = [int(s) for s in strs]
            ints.sort()
            dims.append(ints)
        return dims
