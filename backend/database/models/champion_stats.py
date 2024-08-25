'''
Este módulo contiene la clase `Account` que extiende de `sqlalchemy.orm.DeclarativeBase`
y representa un modelo de tabla.
'''

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.database import Base

if TYPE_CHECKING:
    from backend.database.models.account import Account


class ChampionStats(Base):  # pylint: disable=too-few-public-methods
    """Representa un modelo de ChampionStats en la base de datos.

    Esta clase extiende de `sqlalchemy.orm.DeclarativeBase`
    y se mapea a la tabla `champion_stats` en la base de datos.

    La clase `ChampionStats` contiene información sobre las estadisticas
    de un usuario en clasificatoria con un campeon de League of Legends.
    """
    __tablename__ = "champion_stats"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    account_id: Mapped[int] = mapped_column(ForeignKey("account.id", ondelete="CASCADE"))
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
                f"name={self.name!r}, games_played={self.games_played!r}, "
                f"kill_avg={self.kill_avg!r}, death_avg={self.death_avg!r}, "
                f"assist_avg={self.assist_avg!r}, kda={self.kda!r}, "
                f"wins={self.wins!r}, losses={self.losses!r}, winrate={self.winrate!r})")
