from util.csid_util import *
from types import *
import pytest

def test_csid_list_tuples_all_none():
    tuples: List[Tuple[Optional[str], Optional[str]]] = [(None, None), (None, None)]
    assert csid_list(tuples) == []

def test_csid_list_tuples_some_none():
    tuples: List[Tuple[Optional[str], Optional[str]]] = [("l4k0b", None), ("y2k0b", None)]
    assert csid_list(tuples) == ["l4k0b", "y2k0b"]
