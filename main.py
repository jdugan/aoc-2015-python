from src.day01.runner import Day01
from src.day02.runner import Day02
from src.day03.runner import Day03
from src.day04.runner import Day04

# ---------------------------------------------------------
# Executable
# ---------------------------------------------------------

if __name__ == "__main__":
    runner = Day04()

    print("")
    print(f"DAY {runner.day()}:")
    print("  Puzzle 1 => ", runner.puzzle1())
    print("  Puzzle 2 => ", runner.puzzle2())
    print("")
