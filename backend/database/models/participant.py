from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.database import Base

if TYPE_CHECKING:
    from backend.database.models.match import Match
    

class Participant(Base):
    __tablename__ = "participant"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    match_id: Mapped[int] = mapped_column(ForeignKey("match.id", ondelete="CASCADE"))
    match: Mapped["Match"] = relationship(back_populates="participants")


    champion_id: Mapped[int]
    champion_name: Mapped[str]
    riot_id_game_name: Mapped[str]
    riot_id_tagline: Mapped[str]
    team_id: Mapped[int]
    team_position: Mapped[str]
