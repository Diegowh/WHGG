import pytest
import time
import httpx
import datetime as dt
from unittest.mock import patch

from backend.core.ratelimiter.rate_limiter import RateLimitedClient


@patch('time.time')
def test_single_request_within_limit(mock_time):
    interval = 1
    count = 1
    mock_time.return_value = 0
    client = RateLimitedClient(interval=interval, count=count)
    
    with patch.object(httpx.Client, 'send', return_value="response") as mock_send:
        response = client.send("GET", "http://example.com")
        mock_send.assert_called_once()
        assert response == "response"
