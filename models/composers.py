from datetime import datetime

from sqlalchemy import DateTime, Integer, String
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
