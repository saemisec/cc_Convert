from sqlalchemy import Column, ForeignKey, Integer, String,UniqueConstraint,Boolean
from sqlalchemy.orm import relationship,Mapped, mapped_column
from .base import Base
from .activity import Activity
from .user import User
from .main_project import Main_project
from .permission import Permission


class UserProjectPermission(Base):
    __tablename__ = "user_project_permission"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"),index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("main_project.id"),index=True)
    permission_id: Mapped[int] = mapped_column(ForeignKey("permission.id"),index=True)
    activity_id: Mapped[int] = mapped_column(ForeignKey("activity.id"),index=True)
    results: Mapped[bool] = mapped_column(Boolean)
    user: Mapped[User] = relationship(back_populates="user_project_permission")
    main_project: Mapped[Main_project] = relationship(back_populates="user_project_permission")
    permission: Mapped[Permission] = relationship(back_populates="user_project_permission")
    activity: Mapped[Activity] = relationship(back_populates="user_project_permission")
    __table_args__ = (
        UniqueConstraint("user_id", "project_id", "permission_id","activity_id", name="uq_user_proj_perm"),
    )