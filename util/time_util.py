from datetime import datetime

MS_PER_MIN = 60000

def to_readable(ms: int) -> str:
    """Produces a human-readable timestamp.

    Args:
        ms: the timestamp in milliseconds since the UNIX epoch.

    Returns:
        A string in the form: YYYY-MM-DD hh:mm:ss.
    """
    return str(_to_datetime(ms))

def diff_min(start_ms: int, end_ms: int) -> float:
    """Produces the difference between two timestamps in minutes
    
    Args:
        start_ms: the starting time of the interval
        end_ms: the ending time of the interval

    Returns:
        A float representing the length of the time interval in minutes
    """
    diff_ms: int = end_ms - start_ms
    return _to_min(diff_ms)

def diff_hr(start_ms: int, end_ms: int) -> float:
    """Produces the difference between two timestamps in hours
    
    Args:
        start_ms: the starting time of the interval
        end_ms: the ending time of the interval

    Returns:
        A float representing the length of the time interval in hours
    """
    diff: float = diff_min(start_ms, end_ms)
    return diff / 60

def diff_day(start_ms: int, end_ms: int) -> float:
    """Produces the difference between two timestamps in days
    
    Args:
        start_ms: the starting time of the interval
        end_ms: the ending time of the interval

    Returns:
        A float representing the length of the time interval in days
    """
    diff: float = diff_min(start_ms, end_ms)
    return diff / (60 * 24)

def _to_datetime(ms: int) -> datetime:
    return datetime.fromtimestamp(ms // 1000).replace(microsecond=ms%1000*1000)

def _to_min(ms: int) -> float:
    return ms / MS_PER_MIN
