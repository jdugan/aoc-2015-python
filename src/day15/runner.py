import itertools
import re

from src.utility.reader import Reader

class Day15:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 15

    def puzzle1(self):
        items  = self.__ingredients()
        combos = self.__combinations(100, len(items))
        best   = 0
        for i, combo in enumerate(combos):
            score, _ = self.__aggregate_combo(combo, items)
            if score > best:
                best = score
        return best

    def puzzle2(self):
        items  = self.__ingredients()
        combos = self.__combinations(100, len(items))
        best   = 0
        for i, combo in enumerate(combos):
            score, calories = self.__aggregate_combo(combo, items)
            if calories == 500 and score > best:
                best = score
        return best


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== BAKING ====================================

    def __combinations(self, num_tsps, num_items):
        combos = []
        for combo in itertools.combinations_with_replacement(range(0, num_tsps), num_items):
            if sum(combo) == num_tsps:
                for p in itertools.permutations(combo):
                    combos.append(p)
        return combos

    def __aggregate_combo(self, combo, items):
        cap = dur = fla = tex = cal = 0
        for i, v in enumerate(items):
            cap += (v["capacity"]   * combo[i])
            dur += (v["durability"] * combo[i])
            fla += (v["flavor"]     * combo[i])
            tex += (v["texture"]    * combo[i])
            cal += (v["calories"]   * combo[i])
        cap   = max([0, cap])
        dur   = max([0, dur])
        fla   = max([0, fla])
        tex   = max([0, tex])
        cal   = max([0, cal])
        score = cap * dur * fla * tex
        return (score, cal)


    #========== DATA ======================================

    def __data(_):
        lines = Reader().to_lines("data/day15/input.txt")
        return lines

    def __ingredients(self):
        items = []
        for line in self.__data():
            match = re.search(r'^(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)$', line)
            name, capacity, durability, flavor, texture, calories = match.groups()

            items.append({
                "capacity":   int(capacity),
                "durability": int(durability),
                "flavor":     int(flavor),
                "texture":    int(texture),
                "calories":   int(calories),
            })
        return items
