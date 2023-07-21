import random
import re

from src.utility.reader import Reader

class Day19:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 19

    def puzzle1(self):
        medicine  = self.__medicine()
        commands  = self.__commands()
        molecules = self.__expand(medicine, commands)
        return len(molecules)

    def puzzle2(self):
        molecule  = self.__medicine()
        commands  = self.__commands()
        index     = 0
        steps     = 0
        while molecule != "e":
            try:
                v, k = commands[index]
                m    = molecule.replace(k, v, 1)
                if m == molecule:
                    index += 1
                else:
                    molecule = m
                    index    = 0
                    steps   += 1
            except IndexError:
                random.shuffle(commands)
                molecule  = self.__medicine()
                index     = 0
                steps     = 0
        return steps


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== MACHINE ===================================

    def __expand(self, molecule, commands):
        new_molecules = set();
        for k, v in commands:
            for match in re.finditer(rf"({k})", molecule):
                i1, i2 = match.span()
                s1 = molecule[:i1]
                s2 = molecule[i2:]
                new_molecules.add(f"{s1}{v}{s2}")
        return new_molecules


    #========== DATA ======================================

    def __data(_):
        return Reader().to_lines("data/day19/input.txt")

    def __commands(self):
        cmds = []
        for line in self.__data():
            m = re.search(r'(\w+) => (\w+)', line)
            if m is not None:
                k, v = m.groups()
                cmds.append((k, v))
        return cmds

    def __medicine(self):
        return self.__data().pop()
