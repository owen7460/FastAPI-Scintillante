from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Index, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        comment="created_at"
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        comment="updated_at"
    )

class Composers(Base):
    __tablename__ = "composers"

    id: Mapped[ int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[ str] = mapped_column(String(100), unique=True, nullable=False, comment="composer name")

    def __repr__(self):
        return f"<Composers(id={self.id}, name={self.name})>"

class Works(Base):
    __tablename__ = "works"

    __table_args__ = (Index("pk_work_idx","id"),
                      Index("fk_composer_idx", "composer_id")
                      )

    id: Mapped[ int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    composer_id: Mapped[ int] = mapped_column(Integer,  ForeignKey("composers.id"), comment="composer id")
    title: Mapped[ str] = mapped_column(String(255), comment="work name")
    genre: Mapped[ str] = mapped_column(String(100), comment="work genre")

    def __repr__(self):
        return f"<Works(id={self.id}, composer_id={self.composer_id}, title={self.title}, genre={self.genre})>"