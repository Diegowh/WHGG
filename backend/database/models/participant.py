'''
Este módulo contiene la clase `Participant` que extiende de `sqlalchemy.orm.DeclarativeBase`
y representa un modelo de tabla
'''
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.database import Base

if TYPE_CHECKING:
    from backend.database.models.match import Match


class Participant(Base):  # pylint: disable=too-few-public-methods
    """Representa un modelo de Participant en la base de datos.

    Esta clase extiende de `sqlalchemy.orm.DeclarativeBase`
    y se mapea a la tabla `participant` en la base de datos.

    La clase `Participant` contiene información sobre un participante
    de un match jugado por el usuario.
    """
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

    def __repr__(self) -> str:
        return (
            f"Participant(id={self.id!r}, match_id={self.match_id!r}, "
            f"champion_id={self.champion_id!r}, champion_name={self.champion_name!r}, "
            f"riot_id_game_name={self.riot_id_game_name!r}, "
            f"riot_id_tagline={self.riot_id_tagline!r}, "
            f"team_id={self.team_id!r}, team_position={self.team_position!r})"
        )
