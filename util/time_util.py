from datetime import datetime

def to_readable(ms: int) -> str:
    """Produces a human-readable timestamp.

    Args:
        ms: the timestamp in milliseconds since the UNIX epoch.

    Returns:
        A string in the form: YYYY-MM-DD hh:mm:ss.
    """
    time_in_sec: int = ms // 1000
    return datetime.fromtimestamp(time_in_sec)

print(to_readable.__doc__)