from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Good(Base):
    __tablename__ = "good"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    title: Mapped[str] = mapped_column(String(100))
    measurement_unit_id: Mapped[int | None] = mapped_column(
        ForeignKey("measurement_unit.id")
    )

    measurement_unit: Mapped["Measurement_unit"] = relationship(back_populates="good")
    # spec jsonb NULL,
