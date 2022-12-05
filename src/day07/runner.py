import re
from src.utility.reader import Reader

class Day07:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 7

    def puzzle1(self):
        circuit = {}
        cmds    = self.__data()
        while len(cmds) > 0:
            circuit, cmds = self.__map_circuit(circuit, cmds)
        return circuit["a"]

    def puzzle2(self):
        circuit = {}
        cmds    = list(map(self.__override_cmd, self.__data()))
        while len(cmds) > 0:
            circuit, cmds = self.__map_circuit(circuit, cmds)
        return circuit["a"]


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== CIRCUIT ===================================

    def __map_circuit(self, circuit, original_cmds):
        known = set(circuit.keys())
        cmds  = []

        for cmd in original_cmds:
            wire, type, keys, val = cmd
            result = None

            if (keys == keys.intersection(known)):
                vals = [circuit[k] for k in keys]
                if val is not None:
                    vals.append(val)

                match type:
                    case "assign":
                        result = vals[0]
                    case "and":
                        result = vals[0] & vals[1]
                    case "or":
                        result = vals[0] | vals[1]
                    case "lshift":
                        result = vals[0] << vals[1]
                    case "rshift":
                        result = vals[0] >> vals[1]
                    case "not":
                        result = ~vals[0]

                circuit[wire] = (result + 65536) % 65536
                known.add(wire)
            else:
                cmds.append(cmd)

        return (circuit, cmds)

    def __override_cmd(self, cmd):
        wire, type, keys, val = cmd
        if (wire == "b"):
            val = self.puzzle1()
        return (wire, type, keys, val)


    #========== DATA ======================================

    def __data(self):
        lines = Reader().to_lines("data/day07/input.txt")
        return [self.__parse(line) for line in lines]

    def __parse(self, line):
        # assignment
        match = re.search(r'^(\w+) -> ([a-z]+)$', line)
        if (match):
            key, wire = match.groups()
            try:
                return (wire, "assign", set(), int(key))
            except:
                return (wire, "assign", set({key}), None)

        # and
        match = re.search(r'^(\w+) AND ([a-z]+) -> ([a-z]+)$', line)
        if (match):
            key1, key2, wire = match.groups()
            keys = set({key2})
            val  = None
            try:
                val = int(key1)
            except:
                keys.add(key1)

            return (wire, "and", keys, val)

        # or
        match = re.search(r'^([a-z]+) OR ([a-z]+) -> ([a-z]+)$', line)
        if (match):
            key1, key2, wire = match.groups()
            return (wire, "or", set({key1, key2}), None)

        # lshift
        match = re.search(r'^([a-z]+) LSHIFT (\d+) -> ([a-z]+)$', line)
        if (match):
            key, val, wire = match.groups()
            return (wire, "lshift", set({key}), int(val))

        # rshift
        match = re.search(r'^([a-z]+) RSHIFT (\d+) -> ([a-z]+)$', line)
        if (match):
            key, val, wire = match.groups()
            return (wire, "rshift", set({key}), int(val))

        # not
        match = re.search(r'^NOT ([a-z]+) -> ([a-z]+)$', line)
        if (match):
            key, wire = match.groups()
            return (wire, "not", set({key}), None)

        print(line)
        return None
