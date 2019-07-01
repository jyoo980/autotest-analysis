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