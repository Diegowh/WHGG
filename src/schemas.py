from re import L
from typing import Optional
from pydantic import BaseModel, Field, field_validator, model_validator


server_mappings: dict[str, tuple[str, str]] = {
    "NA": ("americas", "na1"),
    "EUW": ("europe", "euw1"),
    "EUNE": ("europe", "eun1"),
    "OCE": ("sea", "oc1"),
    "KR": ("asia", "kr1"),
    "JP": ("asia", "jp1"),
    "BR": ("americas", "br1"),
    "LAN": ("americas", "la1"),
    "LAS": ("americas", "la2"),
    "RU": ("europe", "ru"),
    "TR": ("europe", "tr1"),
    "SG": ("sea", "sg2"),
    "PH": ("sea", "ph2"),
    "TW": ("sea", "tw2"),
    "VN": ("sea", "vn2"),
    "TH": ("sea", "th2"),
}

class RiotServerDto(BaseModel):
    name: str
    platform: Optional[str] = None
    region: Optional[str] = None


    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str) -> str:
        if v not in server_mappings:
            raise ValueError(f"'{v}' is not a valid server name.")
        return v

    @model_validator(mode='after')
    def set_platform_and_region(self):
        server_name = self.name
        if server_name:
            region, platform = server_mappings[server_name]
            self.region = region
            self.platform = platform
        return self


class RiotIdDto(BaseModel):
    game_name: str
    tag_line: str


    @field_validator('game_name')
    @classmethod
    def validate_game_name(cls, v: str) -> str:
        if not(3 <= len(v) <= 16):
            raise ValueError("game_name must be between 3 and 16 characters long.")
        if not v.isalnum():
            raise ValueError("game_name must contain only alphanumeric characters.")
        return v


    @field_validator('tag_line')
    @classmethod
    def validate_tag_line(cls, v: str) -> str:
        if not (3 <= len(v) <= 5):
            raise ValueError('tag_line must be between 3 and 5 characters long.')
        if not v.isalnum():
            raise ValueError('tag_line must contain only alphanumeric characters.')
        return v
    


class RequestDto(BaseModel):
    riot_id: RiotIdDto
    server: RiotServerDto


class ResponseDto(BaseModel):
    ...