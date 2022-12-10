import re

from src.utility.reader import Reader

class Day19:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 19

    def puzzle1(self):
        commands  = self.__commands()
        molecules = { self.__medicine() }
        molecules = self.__permutate(molecules, commands)
        return len(molecules)

    def puzzle2(self):
        commands  = self.__inverted_commands()
        molecules = { self.__medicine() }
        goal      = "e"
        count     = 0
        while goal not in molecules:
            molecules = self.__permutate(molecules, commands, goal)
            count     = count + 1
            # waaaaay too slow
            if count > 3:
                break
        return count


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== MACHINE ===================================

    def __permutate(self, old_molecules, commands):
        new_molecules = set();
        for input in old_molecules:
            for k, varr in commands.items():
                for match in re.finditer(rf"({k})", input):
                    i1, i2 = match.span()
                    s1 = input[:i1]
                    s2 = input[i2:]
                    for v in varr:
                        new_molecules.add(f"{s1}{v}{s2}")
        return new_molecules;


    #========== DATA ======================================

    def __data(_):
        return Reader().to_lines("data/day19/input.txt")

    def __commands(self, invert=False):
        cmds = {}
        for line in self.__data():
            m = re.search(r'(\w+) => (\w+)', line)
            if m is not None:
                k, v = m.groups()
                if invert:
                    k, v = [v, k]
                if k not in cmds:
                    cmds[k] = []
                cmds[k].append(v)
        return cmds

    def __inverted_commands(self):
        return self.__commands(True)

    def __medicine(self):
        return self.__data().pop()
