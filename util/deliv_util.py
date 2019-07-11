from typing import *
import re

REGEXP_310: str = "_[a-z0-9]*_[a-z0-9]*(_[a-z0-9]*)*"
REGEXP_210: str = "[a-z][0-9][a-z][0-9][a-z]*/"
DELIM_310: str = "_"
DELIM_210: str = "/"
INVALID_IDS: Set[str] = {'pcarter', 'rtholmes', 'autotest'}

def parse_csid(url: str) -> Tuple[Optional[str], Optional[str]]:
    """Parses a tuple of csids from a given commit url. As long as the given commit url contains
    the string "project", and has a sequence of csids which match the regexp: _[a-z0-9]*_[a-z0-9]*
    this function should successfully be able to produce csids.

    Args:
        url: the commit url from which a tuple of csids are to be extracted from

    Returns:
        A tuple containing at most two csids. Note that both these fields are optional.
    """
    if _contains_match(url):
        pattern, delim = (REGEXP_310, DELIM_310) if "project" in url else (REGEXP_210, DELIM_210)
        ids_match = re.search(pattern, url)
        ids: List[str] = ids_match.group(0).split(delim)
        return (ids[0], None) if pattern == REGEXP_210 else (ids[1], ids[2])
    else:
        return (None, None)

def parse_one_csid(url: str) -> str:
    """Parses a single csid from a given commit url. Best used for courses where commit urls are 
    comprised of only one student's csid (Not like 310)

    Args:
        url: the commit url from which a csid is to be extracted from
    
    Returns:
        a string representing a csid which has been extracted from a commit url
    """
    pair: Tuple[Optional[str], Optional[str]] = parse_csid(url)
    if pair == (None, None):
        return ""
    else:
        return pair[0]

def csid_list(id_tuples: List[Tuple[Optional[str], Optional[str]]]) -> List[str]:
    """Produces a list of csids from a list of tuples which may have a pair of csids, e.g.
    [(l4k0b, None), (None, None), (None, y2k0b)]

    Args:
        id_tuples: a list containing tuples of csids, which may be Optional

    Returns:
        A list containin all the csids found within the given list of tuples
    """
    ids: Set[str] = set()
    for id_tuple in id_tuples:
        if id_tuple[0]:
            ids.add(id_tuple[0])
        if id_tuple[1]:
            ids.add(id_tuple[1])
    ids = ids - INVALID_IDS
    return list(ids)

def tup_to_str(tup: Tuple[Optional[str], Optional[str]]) -> str:
    """Converts a tuple containing two optional strings representing csids to a single string
    useful for doing contains operations with dataframes

    Args:
        tup: the tuple which we want to convert into a string representation
    Returns:
        given a tuple (aaaa,bbbb), return "aaaa / bbbb"
        else return the single string
    """
    first: Optional[str] = tup[0]
    second: Optional[str] = tup[1]
    if first and second:
        return "{first} / {second}".format(first=first, second=second)
    elif first:
        return first
    else:
        return second

def list_to_str(lst: List[str]) -> str:
    return " ".join(lst)

def parse_csid_to_list(url: str) -> List[str]:
    """Parses a LIST of csids from a given commit url

    Args:
        url: the commit url from which we want to parse a list of csids
    Returns:
        given a github commit url containing 1 or more csids, return a list of 
        csids in a list form.
    """
    if _contains_match(url):
        pattern, delim = (REGEXP_310, DELIM_310) if "project" in url else (REGEXP_210, DELIM_210)
        ids_match = re.search(pattern, url)
        ids: List[str] = ids_match.group(0).split(delim)
        return ids[:1] if pattern == REGEXP_210 else ids[1:]
    else:
        return []

def flatten_ids(ids: Any):
    flattened: Set[str] = set()
    for id_list in ids:
        for csid in id_list:
            flattened.add(csid)
    flattened = flattened - INVALID_IDS
    return list(flattened)

def _contains_match(url: str) -> bool:
    return url and re.search(REGEXP_310, url) or re.search(REGEXP_210, url)
