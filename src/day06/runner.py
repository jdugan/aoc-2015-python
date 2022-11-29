import re
from src.utility.reader import Reader

class Day06:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 6

    def puzzle1(self):
        grid = set()
        for instr in self.__instructions():
            grid = self.__simple_alteration(grid, instr)
        return len(grid)

    def puzzle2(self):
        grid = {}
        for instr in self.__instructions():
            grid = self.__complex_alteration(grid, instr)
        return sum(list(grid.values()))


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== GRID ======================================

    def __complex_alteration(_, grid, instr):
        cmd, x0, y0, x1, y1 = instr
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                key = f"{x},{y}"
                val = grid.pop(key, 0)
                match cmd:
                    case "turn off":
                        if (val > 1):
                            grid[key] = val - 1
                    case "turn on":
                        grid[key] = val + 1
                    case "toggle":
                        grid[key] = val + 2
        return grid

    def __simple_alteration(_, grid, instr):
        cmd, x0, y0, x1, y1 = instr
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                key = f"{x},{y}"
                match cmd:
                    case "turn off":
                        grid.discard(key)
                    case "turn on":
                        grid.add(key)
                    case "toggle":
                        if key in grid:
                            grid.discard(key)
                        else:
                            grid.add(key)
        return grid


    #========== DATA ======================================

    def __data(_):
        lines = Reader().to_lines("data/day06/input.txt")
        return lines

    def __instructions(self):
        raw_lines = self.__data()
        instrs    = []

        for line in raw_lines:
            match    = re.findall(r'(toggle|turn on|turn off) (\d\d?\d?),(\d\d?\d?) through (\d\d?\d?),(\d\d?\d?)', line)
            captures = match[0]
            instr    = (captures[0], int(captures[1]), int(captures[2]), int(captures[3]), int(captures[4]))
            instrs.append(instr)

        return instrs
