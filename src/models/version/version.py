from sqlalchemy.orm import Mapped, mapped_column

# https://ddragon.leagueoflegends.com/api/versions.json
class Version:
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    number: Mapped[str]