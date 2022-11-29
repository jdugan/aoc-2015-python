from src.day01.runner import Day01
from src.day02.runner import Day02
from src.day03.runner import Day03
from src.day04.runner import Day04
from src.day05.runner import Day05
from src.day06.runner import Day06
from src.day07.runner import Day07

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
