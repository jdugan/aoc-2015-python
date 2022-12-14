from src.day01.runner import Day01
from src.day02.runner import Day02
from src.day03.runner import Day03
from src.day04.runner import Day04
from src.day05.runner import Day05
from src.day06.runner import Day06
from src.day07.runner import Day07
from src.day08.runner import Day08
from src.day09.runner import Day09
from src.day10.runner import Day10
from src.day11.runner import Day11
from src.day12.runner import Day12
from src.day13.runner import Day13
from src.day14.runner import Day14
from src.day15.runner import Day15
from src.day16.runner import Day16

# ---------------------------------------------------------
# Executable
# ---------------------------------------------------------

if __name__ == "__main__":
    runner = Day16()

    print("")
    print(f"DAY {runner.day()}:")
    print("  Puzzle 1 => ", runner.puzzle1())
    print("  Puzzle 2 => ", runner.puzzle2())
    print("")
