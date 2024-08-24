'''
Funciones para el rate limiter
'''

import time

def now():
    """
    Utiliza el tiempo monotónico `time.monotonic` si está disponible,
    de lo contrario, utiliza el reloj del sistema.
    """
    if hasattr(time, 'monotonic'):
        return time.monotonic
    return time.time
