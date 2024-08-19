from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.database import Base

if TYPE_CHECKING:
    from backend.database.models.account import Account


class ChampionStats(Base):
    __tablename__ = "champion_stats"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    account: Mapped["Account"] = relationship(back_populates="champion_stats")

    name: Mapped[str]
    games_played: Mapped[int]
    kill_avg: Mapped[float]
    death_avg: Mapped[float]
    assist_avg: Mapped[float]
    kda: Mapped[float]
    wins: Mapped[int]
    losses: Mapped[int]
    winrate: Mapped[int]

    def __repr__(self) -> str:
        return (f"ChampionStats(id={self.id!r}, account_id={self.account_id!r}, "
                f"name={self.name!r}, kda={self.kda!r}, kill_avg={self.kill_avg!r}, "
                f"death_avg={self.death_avg!r}, assist_avg={self.assist_avg!r}, "
                f"winrate={self.winrate!r}, games_played={self.games_played!r})")