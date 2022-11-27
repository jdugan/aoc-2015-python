from src.day01.runner import Day01
from src.day02.runner import Day02

# ---------------------------------------------------------
# Daily Tests
# ---------------------------------------------------------

def test_day01():
    assert Day01().puzzle1() == 280
    assert Day01().puzzle2() == 1797

def test_day02():
    assert Day02().puzzle1() == 1606483
    assert Day02().puzzle2() == 3842356
