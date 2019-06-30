from typing import Tuple, Optional
import re

def parse_csid(url: str) -> Tuple[Optional[str], Optional[str]]:
    """Parses a tuple of csids from a given commit url. As long as the given commit url contains
    the string "project", and has a sequence of csids which match the regexp: _[a-z0-9]*_[a-z0-9]*
    this function should successfully be able to produce csids.

    Args:
        url: the commit url from which a tuple of csids are to be extracted from

    Returns:
        A tuple containing at most two csids. Note that both these fields are optional.    
    """
    if not str or "project" not in url:
        return (None, None)
    else:
        ids_match = re.search("_[a-z0-9]*_[a-z0-9]*", url)
        ids = ids_match.group(0).split("_")
        return (ids[1], ids[2])