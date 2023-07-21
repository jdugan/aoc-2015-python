class Battle:
    # -----------------------------------------------------
    # Configuration
    # -----------------------------------------------------

    def __init__(self, player_stats, boss_stats, timer_stats=(0, 0, 0), mana_spent=0):
        self.boss_hp        = boss_stats[0]
        self.boss_attack    = boss_stats[1]
        self.player_hp      = player_stats[0]
        self.player_mana    = player_stats[1]
        self.player_defense = player_stats[2]
        self.timer_poison   = timer_stats[0]
        self.timer_recharge = timer_stats[1]
        self.timer_shield   = timer_stats[2]
        self.mana_spent     = mana_spent


    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    # ========== FIGHTING =================================

    def apply_effects(self):
        if self.timer_poison > 0:
            self.__apply_poison()
        if self.timer_recharge > 0:
            self.__apply_recharge()
        if self.timer_shield > 0:
            self.__apply_shield()

    def cast(self, spell):
        match spell:
            case 'drain':
                self.__cast_drain()
            case 'missile':
                self.__cast_missile()
            case 'poison':
                self.__cast_poison()
            case 'recharge':
                self.__cast_recharge()
            case 'shield':
                self.__cast_shield()

    def melee(self):
        damage          = max([self.boss_attack - self.player_defense, 1])
        self.player_hp -= damage


    # ========== BRANCHING ================================

    def available_spells(self):
        spells = []
        if self.player_mana >= 73:
            spells.append('drain')
        if self.player_mana >= 53:
            spells.append('missile')
        if self.player_mana >= 173 and self.timer_poison == 0:
            spells.append('poison')
        if self.player_mana >= 229 and self.timer_recharge == 0:
            spells.append('recharge')
        if self.player_mana >= 113 and self.timer_shield == 0:
            spells.append('shield')
        return spells

    def clone(self):
        p_stats = (self.player_hp, self.player_mana, self.player_defense)
        b_stats = (self.boss_hp, self.boss_attack)
        t_stats = (self.timer_poison, self.timer_recharge, self.timer_shield)
        return Battle(p_stats, b_stats, t_stats, self.mana_spent)

    def winner(self):
        if self.boss_hp < 1:
            return 'player'
        elif self.player_hp < 1:
            return 'boss'
        else:
            return None

    def print(self):
        print('----------------------------------')
        print('player: ', self.player_hp, self.player_mana, self.player_defense)
        print('boss:   ', self.boss_hp, self.boss_attack)
        print('timers: ', self.timer_poison, self.timer_recharge, self.timer_shield)


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    # ========== FIGHT ====================================





    # ========== EFFECTS ==================================

    def __apply_poison(self):
        self.timer_poison -= 1
        self.boss_hp      -= 3

    def __apply_recharge(self):
        self.timer_recharge -= 1
        self.player_mana    += 101

    def __apply_shield(self):
        self.timer_shield   -= 1
        if self.timer_shield == 0:
            self.player_defense -= 7


    # ========== SPELLS ===================================

    def __cast_drain(self):
        self.__use_mana(73)
        self.boss_hp   -= 2
        self.player_hp += 2

    def __cast_missile(self):
        self.__use_mana(53)
        self.boss_hp -= 4

    def __cast_poison(self):
        self.__use_mana(173)
        self.timer_poison = 6

    def __cast_recharge(self):
        self.__use_mana(229)
        self.timer_recharge = 5

    def __cast_shield(self):
        self.__use_mana(113)
        self.player_defense += 7
        self.timer_shield    = 6

    def __use_mana(self, amount):
        self.player_mana -= amount
        self.mana_spent  += amount