import math

from src.utility.reader import Reader

class Day18:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 18

    def puzzle1(self):
        grid = self.__grid()
        for i in range(100):
            grid = self.__step(grid)
        return self.__count_lights(grid)

    def puzzle2(self):
        grid = self.__grid()
        for i in range(100):
            grid = self.__step(grid)
            grid = self.__force_corners(grid)
        return self.__count_lights(grid)


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== GRID ======================================

    def __count_lights(self, grid):
        count = 0
        for k, v in grid.items():
            if v == "#":
                count += 1
        return count

    def __count_neighbors(self, grid, key):
        x, y  = [int(s) for s in key.split(",")]
        nkeys = [
            f"{x-1},{y-1}",     # nw
            f"{x},{y-1}",       # n
            f"{x+1},{y-1}",     # ne
            f"{x+1},{y}",       # e
            f"{x+1},{y+1}",     # se
            f"{x},{y+1}",       # s
            f"{x-1},{y+1}",     # sw
            f"{x-1},{y}",       # w
        ]
        vals = [grid.get(k, ".") for k in nkeys]
        vals = list(filter(lambda k: k == "#", vals))
        return len(vals)

    def __force_corners(self, grid):
        size = int(math.sqrt(len(grid))) - 1
        keys = [f"0,0", f"0,{size}", f"{size},0", f"{size},{size}"]
        for k in keys:
            grid[k] = "#"
        return grid

    def __step(self, curr_grid):
        grid = {}
        for k, v in curr_grid.items():
            nc = self.__count_neighbors(curr_grid, k)
            if v == "#":
                v = "#" if nc in [2,3] else "."
            else:
                v = "#" if nc == 3 else "."
            grid[k] = v
        return grid


    #========== DATA ======================================

    def __data(_):
        return Reader().to_lines("data/day18/input.txt")

    def __grid(self):
        grid = {}
        for y, line in enumerate(self.__data()):
            for x, str in enumerate(line):
                grid[f"{x},{y}"] = str
        return grid
