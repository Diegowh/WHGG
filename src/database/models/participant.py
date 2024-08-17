from sqlalchemy import ForeignKey
from src.database.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.database.models.match import Match
    

class Participant(Base):
    __tablename__ = "participant"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    match_id: Mapped[int] = mapped_column(ForeignKey("match.id"))
    match: Mapped["Match"] = relationship(back_populates="participants")


    champion_id: Mapped[int]
    champion_name: Mapped[str]
    riot_id_game_name: Mapped[str]
    riot_id_tagline: Mapped[str]
    team_id: Mapped[int]
    team_position: Mapped[str]
