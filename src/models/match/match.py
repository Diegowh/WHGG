from __future__ import annotations
from src.models.match.metadata import Metadata
from src.models.match.info import Info
from dataclasses import dataclass


@dataclass
class Match:
    metadata: Metadata
    info: Info