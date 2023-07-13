import re

from src.day23.computer import Computer
from src.utility.reader import Reader

class Day23:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 23

    def puzzle1(self):
        computer = Computer(0, 0)
        program  = self.__program()
        computer.run(program)
        return computer.registers["b"]

    def puzzle2(self):
        computer = Computer(1, 0)
        program  = self.__program()
        computer.run(program)
        return computer.registers["b"]


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== DATA ======================================

    def __data(_):
        return Reader().to_lines("data/day23/input.txt")

    def __program(self):
        instrs = []
        for line in self.__data():
            m = re.search(r'^([a-z]{3}) (.+)$', line)
            instrs.append(m.groups())
        return instrs
