from __future__ import annotations
from typing import Optional, List, Union
from src.models.account.account import Account
from dataclasses import dataclass


@dataclass
class Metadata:
    dataVersion: str
    matchId: str
    participants: Union[str]
    