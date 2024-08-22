from collections import deque
import threading
import time


class RateLimiter:
    def __init__(self, max_requests: int, per_time_unit: float):
        self.token_bucket = TokenBucket(max_requests, max_requests / per_time_unit)
        
    def allow_request(self) -> bool:
        return self.token_bucket.get_token()
    

class TokenBucket:
    def __init__(self, max_tokens: int, refill_rate: float) -> None:
        self.max_tokens = max_tokens
        self.refill_rate = refill_rate
        self.tokens = max_tokens
        self.last_refill_time = time.time()
        self.lock = threading.Lock()
        
    
    def _refill(self) -> None:
        current_time = time.time()
        elapsed_time = current_time - self.last_refill_time
        
        self.tokens = min(self.max_tokens, self.tokens + elapsed_time * self.refill_rate)
        self.last_refill_time = current_time
        
    
    def get_token(self) -> bool:
        with self.lock:
            self._refill()
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False