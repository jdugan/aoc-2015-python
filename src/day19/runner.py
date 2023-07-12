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
        molecules = self.__expand({ self.__medicine() }, commands)
        return len(molecules)

    def puzzle2(self):
        commands  = self.__commands()
        medicine  = self.__medicine()
        shortest  = 1000000
        steps     = 0
        molecules = { "e": 0 }
        # while len(molecules) > 0:
        #     molecules = self.__expand(molecules, commands, limit)
        #     steps     = steps + 1
        #     print(steps, molecules)
        return -2


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== MACHINE ===================================

    def __expand(self, molecules, commands):
        new_molecules = set();
        for molecule in molecules:
            for k, varr in commands.items():
                for match in re.finditer(rf"({k})", molecule):
                    i1, i2 = match.span()
                    s1 = molecule[:i1]
                    s2 = molecule[i2:]
                    for v in varr:
                        new_molecules.add(f"{s1}{v}{s2}")
        return new_molecules;


    #========== DATA ======================================

    def __data(_):
        return Reader().to_lines("data/day19/input.txt")

    def __commands(self):
        cmds = {}
        for line in self.__data():
            m = re.search(r'(\w+) => (\w+)', line)
            if m is not None:
                k, v = m.groups()
                if k not in cmds:
                    cmds[k] = []
                cmds[k].append(v)
        return cmds

    def __medicine(self):
        return self.__data().pop()
