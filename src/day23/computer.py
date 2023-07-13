class Computer:
    # -----------------------------------------------------
    # Configuration
    # -----------------------------------------------------

    def __init__(self, a, b):
        self.registers = { "a": a, "b": b }
        self.index     = 0


    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def run(self, program):
        length = len(program)
        while self.index < length:
            cmd, args = program[self.index]
            match cmd:
                case 'hlf':
                    self.__hlf(args)
                case 'inc':
                    self.__inc(args)
                case 'jie':
                    self.__jie(args)
                case 'jio':
                    self.__jio(args)
                case 'jmp':
                    self.__jmp(args)
                case 'tpl':
                    self.__tpl(args)


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    def __hlf(self, r):
        cv = self.registers[r]
        self.registers[r]  = cv//2
        self.index        += 1

    def __inc(self, r):
        cv = self.registers[r]
        self.registers[r]  = cv + 1
        self.index        += 1

    def __jie(self, args):
        r, offset = args.split(", ")
        if self.registers[r] % 2 == 0:
            self.index += int(offset)
        else:
            self.index += 1

    def __jio(self, args):
        r, offset = args.split(", ")
        if self.registers[r] == 1:
            self.index += int(offset)
        else:
            self.index += 1

    def __jmp(self, offset):
        self.index += int(offset)

    def __tpl(self, r):
        cv = self.registers[r]
        self.registers[r]  = cv * 3
        self.index        += 1