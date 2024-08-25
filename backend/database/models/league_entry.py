'''
Este módulo contiene la clase `LeagueEntry` que extiende de `sqlalchemy.orm.DeclarativeBase`
y representa un modelo de tabla
'''
from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.database import Base

if TYPE_CHECKING:
    from backend.database.models.account import Account



class LeagueEntry(Base):  # pylint: disable=too-few-public-methods
    """Representa un modelo de LeagueEntry en la base de datos.

    Esta clase extiende de `sqlalchemy.orm.DeclarativeBase`
    y se mapea a la tabla `league_entry` en la base de datos.

    La clase `LeagueEntry` contiene información sobre los datos de
    un usuario en una cola clasificatoria de League of Legends.
    """
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
        return (f"LeagueEntry(id={self.id!r}, account_id={self.account_id!r}, "
                f"queue_type={self.queue_type!r}, tier={self.tier!r}, rank={self.rank!r}, "
                f"league_points={self.league_points!r}, wins={self.wins!r}, "
                f"losses={self.losses!r})")
