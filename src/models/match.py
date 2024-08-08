from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.models.account import Account
    from src.models.participant import Participant



class Match(Base):
    __tablename__ = "match"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    account: Mapped["Account"] = relationship(back_populates="matches")
    
    participants: Mapped[list["Participant"]] = relationship(back_populates="match", cascade="all, delete-orphan")

    match_id: Mapped[str]
    game_creation: Mapped[int]
    game_duration: Mapped[int]
    game_end_timestamp: Mapped[int]
    game_mode: Mapped[str]
    game_start_timestamp: Mapped[int]
    game_type: Mapped[str]
    game_version: Mapped[str]
    queue_id: Mapped[int]

    # metadata: Mapped[Metadata] = relationship(uselist=False, back_populates="match")

    # info: Mapped[Info] = relationship(uselist=False, back_populates="match")

    def __repr__(self) -> str:
        return (f"Match(id={self.id!r}, account_id={self.account_id!r}, "
                f"info_id={self.info_id!r})")