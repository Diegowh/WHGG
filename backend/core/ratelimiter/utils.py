import time

def now():
    """
    Use monotonic time if available, otherwise fall back to the system clock.
    """
    if hasattr(time, 'monotonic'):
        return time.monotonic
    return time.time