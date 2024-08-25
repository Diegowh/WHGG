'''
Este módulo contiene la clase `Version` que extiende de `sqlalchemy.orm.DeclarativeBase`
y representa un modelo de tabla
'''
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.database import Base



class Version(Base):  # pylint: disable=too-few-public-methods
    """Representa un modelo de Version en la base de datos.

    Esta clase extiende de `sqlalchemy.orm.DeclarativeBase`
    y se mapea a la tabla `version` en la base de datos.

    La clase `Version` contiene los datos sobre una versión
    de League of Legends.
    
    # https://ddragon.leagueoflegends.com/api/versions.json
    """
    __tablename__ = "version"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    number: Mapped[str]

    def __repr__(self) -> str:
        return (
            f"Version(id={self.id!r}, number={self.number!r})"
        )
