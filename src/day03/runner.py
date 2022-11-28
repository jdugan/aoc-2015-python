from src.utility.reader import Reader

class Day03:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 3

    def puzzle1(self):
        grid = {"0,0": 1}
        grid = self.__deliver("0,0", grid, self.__data())
        return len(grid.keys())

    def puzzle2(self):
        a1, a2 = self.__split()
        grid   = {"0,0": 1}
        grid   = self.__deliver("0,0", grid, a1)
        grid   = self.__deliver("0,0", grid, a2)
        return len(grid.keys())


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== GRID ======================================

    def __deliver(self, pos, grid, instrs):
        for cmd in instrs:
            pos = self.__move(pos, cmd)
            if pos in grid.keys():
                grid[pos] += 1
            else:
                grid[pos] = 1
        return grid

    def __move(self, pos, cmd):
        x, y = [int(s) for s in pos.split(",")]
        match cmd:
            case "^":
                y += 1
            case "v":
                y += -1
            case ">":
                x += 1
            case "<":
                x += -1
        return f"{x},{y}"


    #========== DATA ======================================

    def __data(self):
        lines = Reader().to_lines("data/day03/input.txt")
        return [s for s in lines[0]]

    def __split(self):
        a1 = []
        a2 = []
        for idx, cmd in enumerate(self.__data()):
            if (idx % 2 == 1):
                a1.append(cmd)
            else:
                a2.append(cmd)
        return [a1, a2]
