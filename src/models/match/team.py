from src.models.match.ban import Ban
from src.models.match.objectives import Objectives
from src.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.models.match.info import Info


class Team(Base):
    __tablename__ = "team"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    info_id = Mapped[int] = mapped_column(ForeignKey("info.id"))
    info = Mapped[Info] = relationship(back_populates="teams")

    bans: list[Ban]
    objectives: Objectives
    teamId: int
    win: bool
