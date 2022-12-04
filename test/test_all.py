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

# ---------------------------------------------------------
# Daily Tests
# ---------------------------------------------------------

def test_day01():
    assert Day01().puzzle1() == 280
    assert Day01().puzzle2() == 1797

def test_day02():
    assert Day02().puzzle1() == 1606483
    assert Day02().puzzle2() == 3842356

def test_day03():
    assert Day03().puzzle1() == 2572
    assert Day03().puzzle2() == 2631

def test_day04():
    assert Day04().puzzle1() == 346386
    assert Day04().puzzle2() == 9958218

def test_day05():
    assert Day05().puzzle1() == 238
    assert Day05().puzzle2() == 69

def test_day06():
    assert Day06().puzzle1() == 543903
    assert Day06().puzzle2() == 14687245

def test_day07():
    assert Day07().puzzle1() == 956
    assert Day07().puzzle2() == 40149

def test_day08():
    assert Day08().puzzle1() == 1333
    assert Day08().puzzle2() == 2046

def test_day09():
    assert Day09().puzzle1() == 117
    assert Day09().puzzle2() == 909

def test_day10():
    assert Day10().puzzle1() == 360154
    assert Day10().puzzle2() == 5103798

def test_day11():
    assert Day11().puzzle1() == "hxbxxyzz"
    assert Day11().puzzle2() == "hxcaabcc"

def test_day12():
    assert Day12().puzzle1() == 191164
    assert Day12().puzzle2() == 87842

def test_day13():
    assert Day13().puzzle1() == 733
    assert Day13().puzzle2() == 725

def test_day14():
    assert Day14().puzzle1() == -1
    assert Day14().puzzle2() == -2
