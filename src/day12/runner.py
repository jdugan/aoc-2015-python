import json
import re
from src.utility.reader import Reader

class Day12:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 12

    def puzzle1(self):
        data = self.__data()
        return self.__calculate_sum(data)

    def puzzle2(self):
        parsed   = json.loads(self.__data())
        adjusted = self.__remove_red_dicts(parsed)
        data     = json.dumps(adjusted)
        return self.__calculate_sum(data)


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== HELPERS ===================================

    def __calculate_sum(_, data):
        scrubbed = re.sub(r'[^-\d]', " ", data)
        vals     = [int(s) for s in re.split(r'\s+', scrubbed.strip())]
        return sum(vals)

    def __remove_red_dicts(self, data):
        if isinstance(data, dict):
            if "red" in data.values():
                return 0
            else:
                tmp = {}
                for k, v in data.items():
                    tmp[k] = self.__remove_red_dicts(v)
                return tmp
        elif isinstance(data, list):
            return [self.__remove_red_dicts(item) for item in data]
        else:
            return data


    #========== DATA ======================================

    def __data(_):
        lines = Reader().to_lines("data/day12/input.txt")
        return lines[0]
