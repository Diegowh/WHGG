from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.database import Base

if TYPE_CHECKING:
    from backend.database.models.account import Account
    


class LeagueEntry(Base):
    __tablename__ = "league_entry"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    account_id: Mapped[int] = mapped_column(ForeignKey("account.id", ondelete="CASCADE"))
    account: Mapped["Account"] = relationship(back_populates="league_entries")
    
    queue_type: Mapped[str]
    tier: Mapped[Optional[str]]
    rank: Mapped[Optional[str]]
    league_points: Mapped[int]
    wins: Mapped[int]
    losses: Mapped[int]
    
    __table_args__ = (
        UniqueConstraint("account_id", "queue_type", name="_account_id_queue_type_uc"),
    )
    
    def __repr__(self) -> str:
        return f"LeagueEntry(id={self.id!r}, account_id={self.account_id!r}, queue_type={self.queue_type!r}, tier={self.tier!r}, rank={self.rank!r}, league_points={self.league_points!r}, wins={self.wins!r}, losses={self.losses!r}"
