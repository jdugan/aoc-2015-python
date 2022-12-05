import re

from src.day14.reindeer import Reindeer
from src.utility.reader import Reader

class Day14:
    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def day(_):
        return 14

    def puzzle1(self):
        return self.__best_distance()

    def puzzle2(self):

        return self.__most_points()


    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    #========== RACE ======================================

    def __best_distance(self):
        reindeer = self.__reindeer()
        for _ in range(0, self.__duration()):
            for r in reindeer:
                r.tick()
        return max([r.distance for r in reindeer])

    def __most_points(self):
        reindeer = self.__reindeer()
        for _ in range(0, self.__duration()):
            for r in reindeer:
                r.tick()
            best = max([r.distance for r in reindeer])
            for r in reindeer:
                if r.distance == best:
                    r.increment_points()
        return max([r.points for r in reindeer])

    def __duration(_):
        return 2503


    #========== DATA ======================================

    def __data(_):
        lines = Reader().to_lines("data/day14/input.txt")
        return lines

    def __reindeer(self):
        deer = []
        for line in self.__data():
            match = re.search(r'\A(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.\Z', line)
            name, speed, endurance, pause = match.groups()
            deer.append(Reindeer(name, int(speed), int(endurance), int(pause)))
        return deer
