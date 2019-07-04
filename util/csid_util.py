from typing import *

def csid_list(id_tuples: List[Tuple[Optional[str], Optional[str]]]) -> List[str]:
    """Produces a list of csids from a list of tuples which may have a pair of csids, e.g.
    [(l4k0b, None), (None, None), (None, y2k0b)]

    Args:
        id_tuples: a list containing tuples of csids, which may be Optional

    Returns:
        A list containin all the csids found within the given list of tuples
    """
    ids: List[str] = []
    for id_tuple in id_tuples:
        if id_tuple[0]:
            ids.append(id_tuple[0])
        if id_tuple[1]:
            ids.append(id_tuple[1])
    return ids