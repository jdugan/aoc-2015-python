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
        match = re.findall(r'^(\w+) -> ([a-z]+)$', line)
        if (len(match)):
            key, wire = match[0]
            try:
                return (wire, "assign", set(), int(key))
            except:
                return (wire, "assign", set({key}), None)

        # and
        match = re.findall(r'^(\w+) AND ([a-z]+) -> ([a-z]+)$', line)
        if (len(match)):
            key1, key2, wire = match[0]
            keys = set({key2})
            val  = None
            try:
                val = int(key1)
            except:
                keys.add(key1)

            return (wire, "and", keys, val)

        # or
        match = re.findall(r'^([a-z]+) OR ([a-z]+) -> ([a-z]+)$', line)
        if (len(match)):
            key1, key2, wire = match[0]
            return (wire, "or", set({key1, key2}), None)

        # lshift
        match = re.findall(r'^([a-z]+) LSHIFT (\d+) -> ([a-z]+)$', line)
        if (len(match)):
            key, val, wire = match[0]
            return (wire, "lshift", set({key}), int(val))

        # rshift
        match = re.findall(r'^([a-z]+) RSHIFT (\d+) -> ([a-z]+)$', line)
        if (len(match)):
            key, val, wire = match[0]
            return (wire, "rshift", set({key}), int(val))

        # not
        match = re.findall(r'^NOT ([a-z]+) -> ([a-z]+)$', line)
        if (len(match)):
            key, wire = match[0]
            return (wire, "not", set({key}), None)

        print(line)
        return None
