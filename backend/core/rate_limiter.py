
from functools import wraps
import time
import httpx
import datetime as dt

class RateLimitedClient(httpx.Client):
    
    def __init__(self, interval: dt.timedelta | float, count: int = 1, **kwargs):
        
        if isinstance(interval, dt.timedelta):
            interval = interval.total_seconds()
            
        self.interval = interval
        self.count = count
        self.requests_made = 0
        self.last_reset = time.time()
        super().__init__(**kwargs)
    
    def _reset_if_needed(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_reset
        
        if elapsed_time > self.interval:
            self.requests_made = 0 
            self.last_reset = current_time
    
    def _acquire(self):
        while True:
            self._reset_if_needed()
            if self.requests_made < self.count:
                self.requests_made += 1
                break
            
            else:
                time_to_wait = self.interval - (time.time() - self.last_reset)
                if time_to_wait > 0:
                    print(f"Rate limit reached. Waiting for {time_to_wait:.2f} seconds...")
                    time.sleep(time_to_wait)
                self._reset_if_needed()
    
    @wraps(httpx.Client.send)
    def send(self, *args, **kwargs):
        self._acquire()
        return super().send(*args, **kwargs)
    