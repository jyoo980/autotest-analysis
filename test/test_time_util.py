from util.time_util import *
import pytest

def test_to_readable():
    sample_timestamp: int = 1561849200000
    assert to_readable(sample_timestamp) == "2019-06-29 16:00:00"

def test_to_readable_midnight():
    midnight: int = 1561791600000
    assert to_readable(midnight) == "2019-06-29 00:00:00"

def test_diff_min_same_day():
    start: int = 1561791600000
    end: int = 1561793400000
    assert diff_min(start, end) == 30

def test_diff_min_diff_days():
    day_before: int = 1561877940000
    day_after: int = 1561878000000
    assert diff_min(day_before, day_after) == 1

def test_diff_hr_same_day():
    start: int = 1561878000000
    end: int = 1561923000000
    assert diff_hr(start, end) == 12.5

def test_diff_hr_diff_days():
    day_before: int = 1561923000000
    day_after: int = 1562009400000
    assert diff_hr(day_before, day_after) == 24

def test_diff_day_same_day():
    start: int = 1561878000000
    end: int = 1561923000000
    assert diff_day(start, end) == pytest.approx(0.5, 0.1)

def test_diff_hr_diff_days():
    day_before: int = 1561923000000
    day_after: int = 1562009400000
    assert diff_day(day_before, day_after) == 1