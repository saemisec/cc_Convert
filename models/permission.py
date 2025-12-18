from typing import Optional
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base


class Permission(Base):
    __tablename__ = "permission"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_position_id: Mapped[int] = mapped_column(
        ForeignKey("user_position.id"), index=True, nullable=False
    )
    mian_project_id: Mapped[int] = mapped_column(
        ForeignKey("main_project.id"), index=True
    )
    form_entity_id: Mapped[int] = mapped_column(
        ForeignKey("form_entity.id"), index=True
    )
    activity_type_id: Mapped[int] = mapped_column(ForeignKey("activity.id"), index=True)

    # Relationships
    user_position: Mapped["User_position"] = relationship(back_populates="permission")
    main_project: Mapped["Main_project"] = relationship(back_populates="permission")
    form_entity: Mapped["Form_Entity"] = relationship(back_populates="permission")
    activity_type: Mapped["Activity_type"] = relationship(back_populates="permission")

    __table_args__ = (
        UniqueConstraint(
            "user_position_id",
            "mian_project_id",
            "form_entity_id",
            "activity_type_id",
            name="uq_permission_composite",
        ),
    )
