from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.models.account import Account
    


class LeagueEntry(Base):
    __tablename__ = "league_entry"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    account_id: Mapped[str] = mapped_column(ForeignKey("account.id"))
    account: Mapped["Account"] = relationship(back_populates="league_entries")
    
    queue_type: Mapped[str]
    tier: Mapped[str]
    rank: Mapped[str]
    league_points: Mapped[int]
    wins: Mapped[int]
    losses: Mapped[int]
    
    def __repr__(self) -> str:
        return f"LeagueEntry(id={self.id!r}, summonerId={self.summonerId!r}, tier={self.tier!r}, rank={self.rank!r})"