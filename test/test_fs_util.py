from util.fs_util import *
import pytest

def test_get_path_empty():
    assert get_path("") == "../data/"

def test_get_path_non_empty():
    fname: str = "some_data.csv"
    assert get_path(fname) == "../data/some_data.csv"
