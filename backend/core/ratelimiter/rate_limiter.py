'''
Modulo para un cliente HTTP con RateLimiter.

Define una clase RateLimitedClient que extiende httpx.Client
para implementarle una capa de limitacion de solicitudes.
'''

from functools import wraps
import time
import datetime as dt
import httpx
from backend.core.ratelimiter.utils import now

class RateLimitedClient(httpx.Client):
    """Cliente HTTP con Rate limit.
    Extiende httpx.Client para añadir limitacion de tasa de solicitudes,
    permitiendo realizar solicitudes HTTP mientras se respeta un límite
    dentro de un intervalo de tiempo especificado.

    Args:
        interval (datetime.timedelta | float): Intervalo de tiempo en segundos
            durante el cual se permite un número máximo de solicitudes.
        count (int): Número máximo de solicitudes permitidas dentro del intervalo especificado.
        clock (callable): Función que devuelve el tiempo actual. Por defecto, utiliza `now()` de
            `backend.core.ratelimiter.utils`.
        **kwargs: Argumentos que se pasan al inicializador de `httpx.Client`
    """
    def __init__(self, interval: dt.timedelta | float, count: int = 1, clock=now(), **kwargs):

        if isinstance(interval, dt.timedelta):
            interval = interval.total_seconds()

        self.interval = interval
        self.count = count
        self.clock = clock
        self.requests_made = 0
        self.last_reset = self.clock()
        super().__init__(**kwargs)

    def _reset_request_count(self):
        current_time = self.clock()
        elapsed_time = current_time - self.last_reset

        if elapsed_time > self.interval:
            self.requests_made = 0
            self.last_reset = current_time

    def _wait_for_slot(self):
        while True:
            self._reset_request_count()
            if self.requests_made < self.count:
                self.requests_made += 1
                break

            time_to_wait = self.interval - (self.clock() - self.last_reset)
            if time_to_wait > 0:
                print(f"Rate limit reached. Waiting for {time_to_wait:.2f} seconds...")
                time.sleep(time_to_wait)
            self._reset_request_count()

    @wraps(httpx.Client.send)
    def send(self, *args, **kwargs):
        self._wait_for_slot()
        return super().send(*args, **kwargs)
