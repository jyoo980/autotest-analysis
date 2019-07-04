from typing import Tuple, Optional, List, Set
import re

REGEXP_310: str = "_[a-z0-9]*_[a-z0-9]*"
REGEXP_210: str = "[a-z][0-9][a-z][0-9][a-z]*/"
DELIM_310: str = "_"
DELIM_210: str = "/"

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
    return list(ids)

def _contains_match(url: str) -> bool:
    return url and re.search(REGEXP_310, url) or re.search(REGEXP_210, url)
