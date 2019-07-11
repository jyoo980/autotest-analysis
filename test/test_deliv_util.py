from util.deliv_util import *
import pytest

def test_parse_csid_fails_gracefully():
    invalid_url: str = "https://github.ugrad.cs.ubc.ca/CPSC310-xxxx-T2/commit/83836341239fadsasdiuf3"
    assert parse_csid(invalid_url) == (None, None)

def test_parse_csid_empty_url():
    empty_url: str = ""
    assert parse_csid(empty_url) == (None, None)

def test_parse_csid_valid_url():
    some_url: str = "https://github.ugrad.cs.ubc.ca/CPSC310-2018W-T2/project_l4k0b_r2l9b/commit/6785aed12ca2181f458a074a35d6b72ea5739630"
    assert parse_csid(some_url) == ("l4k0b", "r2l9b")

def test_parse_csid_210_url():
    url_210: str = "https://github.ugrad.cs.ubc.ca/CPSC210-2018W-T2/PomoTODO_phase4_l4k0b/commit/9f496ae3ceefc50cb4d04e2b633fc74ed86f034d"
    assert parse_csid(url_210) == ("l4k0b", None)

def test_parse_csid_210_fails_gracefully():
    invalid_210_url: str = "https://github.ugrad.cs.ubc.ca/CPSC210-2018W-T2/PomoTODO_/commit/9f496ae3ceefc50cb4d04e2b633fc74ed86f034d"
    assert parse_csid(invalid_210_url) == (None, None)

def test_parse_csid_single_id():
    d0_url: str = "https://github.ugrad.cs.ubc.ca/CPSC310-2018W-T2/d0_l4k0b/commit/6785aed12ca2181f458a074a35d6b72ea5739630"
    parse_csid == ("l4k0b", None)

def test_parse_one_csid_get_empty():
    url: str = "https://github.ugrad.cs.ubc.ca/"
    assert parse_one_csid(url) == ""

def test_parse_one_csid_valid():
    url: str = "https://github.ugrad.cs.ubc.ca/CPSC210-2018W-T2/assign0_r6s7/commit/aff7f0ec5ac8304041ea4a2175fe0b8462887223"
    assert parse_one_csid(url) == "r6s7"

def test_parse_one_csid_valid():
    url: str = "https://github.ugrad.cs.ubc.ca/CPSC210-2018W-T2/assign0_l4k0b/commit/aff7f0ec5ac8304041ea4a2175fe0b8462887223"
    assert parse_one_csid(url) == "l4k0b"

def test_parse_one_csid_pomo_todo():
    url: str = "https://github.ugrad.cs.ubc.ca/CPSC210-2018W-T2/PomoTODO_phase3_l4k0b/commit/baca4a94121021dae0bf37e6f89c4710a770c839"
    assert parse_one_csid(url) == "l4k0b"

def test_csid_list_tuples_all_none():
    tuples: List[Tuple[Optional[str], Optional[str]]] = [(None, None), (None, None)]
    assert csid_list(tuples) == []

def test_csid_list_tuples_some_none():
    tuples: List[Tuple[Optional[str], Optional[str]]] = [("l4k0b", None), ("y2k0b", None)]
    csids: List[str] = csid_list(tuples)
    assert len(csids) == 2
    assert "l4k0b" in csids
    assert "y2k0b" in csids

def test_csid_list_tuples_duplicate():
    tuples: List[Tuple[Optional[str], Optional[str]]] = [("l4k0b", "y2k0b"), ("l4k0b", None)]
    csids: List[str] = csid_list(tuples)
    assert len(csids) == 2
    assert "l4k0b" in csids
    assert "y2k0b" in csids

def test_tup_to_str_both_some():
    tup = ("l4k0b", "y2k0b")
    assert tup_to_str(tup) == "l4k0b / y2k0b"

def test_tup_to_str_first_none():
    tup = (None, "l4k0b")
    assert tup_to_str(tup) == "l4k0b"

def test_tup_to_str_second_none():
    tup = ("l4k0b", None)
    assert tup_to_str(tup) == "l4k0b"

def test_parse_csid_to_list_single():
    url: str = "https://github.ugrad.cs.ubc.ca/CPSC310-2018W-T2/d0_l4k0b/commit/6785aed12ca2181f458a074a35d6b72ea5739630"
    assert parse_csid_to_list(url) == ["l4k0b"]

def test_parse_csid_to_list_double():
    url: str = "https://github.ugrad.cs.ubc.ca/CPSC310-2018W-T2/project_l4k0b_y2k0b/commit/6785aed12ca2181f458a074a35d6b72ea5739630"
    assert parse_csid_to_list(url) == ["l4k0b", "y2k0b"]

def test_parse_csid_to_list_triple():
    url: str = "https://github.ugrad.cs.ubc.ca/CPSC310-2018W-T2/project_l4k0b_y2k0b_r7p0b/commit/6785aed12ca2181f458a074a35d6b72ea5739630"
    assert parse_csid_to_list(url) == ["l4k0b", "y2k0b", "r7p0b"]
