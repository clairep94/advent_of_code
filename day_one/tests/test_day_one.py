from lib.day_one import *

def test_1abc2():
    assert calibration_finder("1abc2") == 12


def pqr3stu8vwx():
    assert calibration_finder("pqr3stu8vwx") == 38

def a1b2c3d4e5f():
    assert calibration_finder("a1b2c3d4e5f") == 15

def treb7uchet():
    assert calibration_finder("treb7uchet") == 77
