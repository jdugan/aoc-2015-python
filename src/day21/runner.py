import itertools
import math

from src.utility.reader import Reader

class Day21:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 21

    def puzzle1(self):
        boss    = self.__boss()
        players = self.__players(100)
        players = sorted(players, key=lambda p: p["cost"])
        cost  = -1
        for p in players:
            if self.__fight(p, boss) == "player":
                cost = p["cost"]
                break
        return cost

    def puzzle2(self):
        boss    = self.__boss()
        players = self.__players(100)
        players = sorted(players, key=lambda p: p["cost"])
        cost  = -1
        for p in players:
            if self.__fight(p, boss) == "boss":
                cost = p["cost"]
        return cost


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== BATTLE ====================================

    def __fight(self, player, boss):
        b_hp     = boss["hp"]
        b_damage = max(0, boss["damage"] - player["armor"])
        p_hp     = player["hp"]
        p_damage = max(0, player["damage"] - boss["armor"])

        if b_damage == 0 and p_damage == 0:
            return "stalemate"
        elif b_damage == 0:
            return "player"
        elif p_damage == 0:
            return "boss"
        else:
            b_turns  = math.ceil(p_hp/b_damage)
            p_turns  = math.ceil(b_hp/p_damage)
            if b_turns < p_turns:
                return "boss"
            else:
                return "player"

    def __players(self, hp):
        # rings = itertools.combinations(self.__shop_rings(), 0)
        # rings = [list(tuple) for tuple in rings]
        armors      = self.__armors()
        rings       = self.__rings()
        ring_pairs  = self.__ring_pairs()
        weapons     = self.__weapons()
        players     = []
        # weapon [+ armor]
        for w in weapons:
            players.append({ "hp": hp, "damage": w["damage"], "armor": w["armor"], "cost": w["cost"] })
            for a in armors:
                damage = w["damage"] + a["damage"]
                armor  = w["armor"]  + a["armor"]
                cost   = w["cost"]   + a["cost"]
                players.append({ "hp": hp, "damage": damage, "armor": armor, "cost": cost })
        # weapon [+ armor] + ring[s]
        for p in players.copy():
            for r in rings:
                damage = p["damage"] + r["damage"]
                armor  = p["armor"]  + r["armor"]
                cost   = p["cost"]   + r["cost"]
                players.append({ "hp": hp, "damage": damage, "armor": armor, "cost": cost })
            for rp in ring_pairs:
                rpd = 0
                rpa = 0
                rpc = 0
                for r in rp:
                    rpd += r["damage"]
                    rpa += r["armor"]
                    rpc += r["cost"]
                damage = p["damage"] + rpd
                armor  = p["armor"]  + rpa
                cost   = p["cost"]   + rpc
                players.append({ "hp": hp, "damage": damage, "armor": armor, "cost": cost })



        return players



    #========== DATA ======================================

    def __data(_):
        return Reader().to_lines("data/day21/input.txt")

    def __boss(self):
        health, offense, defense = [line.split(": ").pop() for line in self.__data()]
        return {
            "hp":     int(health),
            "damage": int(offense),
            "armor":  int(defense),
        }


    #========== SHOP ======================================

    def __armors(_):
        return [
            { "name": "Leather",    "cost":  13, "damage": 0, "armor": 1 },
            { "name": "Chainmail",  "cost":  31, "damage": 0, "armor": 2 },
            { "name": "Splintmail", "cost":  53, "damage": 0, "armor": 3 },
            { "name": "Bandedmail", "cost":  75, "damage": 0, "armor": 4 },
            { "name": "Platemail",  "cost": 102, "damage": 0, "armor": 5 },
        ]

    def __rings(_):
        return [
            { "name": "Damage +1",  "cost":  25, "damage": 1, "armor": 0 },
            { "name": "Damage +2",  "cost":  50, "damage": 2, "armor": 0 },
            { "name": "Damage +3",  "cost": 100, "damage": 3, "armor": 0 },
            { "name": "Defense +1", "cost":  20, "damage": 0, "armor": 1 },
            { "name": "Defense +2", "cost":  40, "damage": 0, "armor": 2 },
            { "name": "Defense +3", "cost":  80, "damage": 0, "armor": 3 },
        ]

    def __ring_pairs(self):
        combos = itertools.combinations(self.__rings(), 2)
        pairs  = [list(c) for c in combos]
        return pairs

    def __weapons(_):
        return [
            { "name": "Dagger",     "cost":  8, "damage": 4, "armor": 0 },
            { "name": "Shortsword", "cost": 10, "damage": 5, "armor": 0 },
            { "name": "Warhammer",  "cost": 25, "damage": 6, "armor": 0 },
            { "name": "Longsword",  "cost": 40, "damage": 7, "armor": 0 },
            { "name": "Greataxe",   "cost": 74, "damage": 8, "armor": 0 },
        ]


