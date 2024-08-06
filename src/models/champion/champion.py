from __future__ import annotations
from src.models.account.account import Account
from src.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.champion.champion_info import ChampionInfo
from src.models.champion.champion_image import ChampionImage
from src.models.champion.champion_stats import ChampionStats
from src.models.champion.champion_tags import ChampionTags

# Archivo que contiene una lista de los campeones con un breve resumen
# https://ddragon.leagueoflegends.com/cdn/14.15.1/data/en_US/champion.json

# JSON individual de cada campeon con datos adicionales como el lore, tips, etc.
# https://ddragon.leagueoflegends.com/cdn/14.15.1/data/en_US/champion/Aatrox.json

class Champion(Base):
    __tablename__ = "champion"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str]
    title: Mapped[str]
    blurb: Mapped[str]
    info: Mapped[ChampionInfo]
    image: Mapped[ChampionImage]
    tags: Mapped[ChampionTags]
    partype: Mapped[str]
    stats: Mapped[ChampionStats]
