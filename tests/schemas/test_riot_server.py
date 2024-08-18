from sys import exc_info
from pydantic_core import ValidationError
import pytest
from backend.schemas.riot_server import RiotServer



def test_parsing_valid_server_names():
    server_data = [
        ("NA", "americas", "na1"),
        ("EUW", "europe", "euw1"),
        ("KR", "asia", "kr1"),
        ("BR", "americas", "br1")
    ]
    for name, expected_region, expected_platform in server_data:
        server = RiotServer(name=name)
        assert server.region == expected_region
        assert server.platform == expected_platform


def test_invalid_server_name():
    with pytest.raises(ValidationError) as exc_info:
        RiotServer(name="INVALID")
    assert "is not a valid server name" in str(exc_info.value)


def test_case_sensitivity():
    with pytest.raises(ValidationError):
        RiotServer(name="euw")