from __future__ import annotations
from src.models.account.account import Account
from src.models.base import Base
from sqlalchemy import ForeignKey, Mapped, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.match.metadata import Metadata
from src.models.match.info import Info



class Match(Base):
    
    __tablename__ = "match"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    account_id: Mapped[str] = mapped_column(ForeignKey("account.id"))
    account: Mapped[Account] = relationship(Account, back_populates="matches")

    metadata_id: Mapped[int] = mapped_column(ForeignKey("metadata.id"))
    metadata: Mapped[Metadata] = relationship(Metadata, uselist=False, back_populates="match")

    info_id: Mapped[int] = mapped_column(ForeignKey("info.id"))
    info: Mapped[Info] = relationship(
        Info, 
        uselist=False, 
        back_populates="match"
    )

    def __repr__(self) -> str:
        return (f"Match(id={self.id!r}, account_id={self.account_id!r}, "
                f"metadata_id={self.metadata_id!r}, info_id={self.info_id!r})")