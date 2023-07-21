from src.day22.battle   import Battle
from src.utility.reader import Reader

class Day22:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 22

    def puzzle1(self):
        return self.__find_lowest_mana('easy')

    def puzzle2(self):
        return self.__find_lowest_mana('hard')


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== SOLVERS ===================================

    def __find_lowest_mana(self, mode='easy'):
        player_stats = (50, 500, 0)
        boss_stats   = self.__boss_stats()
        seed         = Battle(player_stats, boss_stats)
        penalty      = 1 if mode == 'hard' else 0
        best         = 10000000
        battles      = [seed]
        while len(battles) > 0:
            new_battles = []
            for b in battles:
                b.player_hp -= penalty
                if b.winner() != 'boss':
                    b.apply_effects()
                    for s in b.available_spells():
                        b1 = b.clone()
                        b1.cast(s)
                        if b1.winner() != 'player':
                            b1.apply_effects()
                        if b1.winner() != 'player':
                            b1.melee()
                        if b1.winner() == 'player':
                            if b1.mana_spent < best:
                                best = b1.mana_spent
                        elif b1.winner() is None:
                            new_battles.append(b1)
            battles = new_battles
        return best


    #========== DATA ======================================

    def __data(_):
        return Reader().to_lines("data/day22/input.txt")

    def __boss_stats(self):
        data   = self.__data()
        hp     = data[0].split(': ')[1]
        damage = data[1].split(': ')[1]
        return (int(hp), int(damage))