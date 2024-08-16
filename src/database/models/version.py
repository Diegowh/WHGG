from sqlalchemy.orm import Mapped, mapped_column
from src.database.database import Base


# https://ddragon.leagueoflegends.com/api/versions.json
class Version(Base):
    __tablename__ = "version"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    number: Mapped[str]