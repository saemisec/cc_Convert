from typing import TYPE_CHECKING, List
from sqlalchemy import String, ForeignKey, Identity, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from models.base import Base

if TYPE_CHECKING:
    from models.main_project import Main_project
    from models.mdr_details import Mdr_details
    from models.cbs_element import Cbs_element
    from models.mr_item import MrItem
    from models.mdr_extra_cost import MdrExtraCost


class Mdr(Base):
    """مدل مدارک فنی - MDR (Material Data Record)"""

    __tablename__ = "mdr"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    main_project_id: Mapped[int] = mapped_column(
        ForeignKey("main_project.id"), index=True
    )
    document_no: Mapped[str] = mapped_column(String(50))
    title: Mapped[str] = mapped_column(String(255))
    type: Mapped[str] = mapped_column(String(50))
    last_rev: Mapped[str] = mapped_column(String(10))
    discipline: Mapped[str] = mapped_column(String(4))
    cbs_element_id: Mapped[int | None] = mapped_column(
        ForeignKey("cbs_element.id"), index=True, nullable=True
    )
    last_status: Mapped[str] = mapped_column(String(50))

    __table_args__ = (
        UniqueConstraint(
            "cbs_element_id",
            "main_project_id",
            "document_no",
            name="uq_mdr_project_doc_no",
        ),
    )

    main_project: Mapped["Main_project"] = relationship(back_populates="mdr")
    cbs_element: Mapped["Cbs_element"] = relationship(back_populates="mdr")
    mdr_details: Mapped[List["Mdr_details"]] = relationship(back_populates="mdr")
    # tbe_requests: Mapped[List["TBE_Request"]] = relationship(back_populates="mdr")
    mr_items: Mapped[List["MrItem"]] = relationship(
        foreign_keys="[MrItem.mdr_id]", back_populates="mdr"
    )
    related_mr_items: Mapped[List["MrItem"]] = relationship(
        foreign_keys="[MrItem.related_datasheet_id]", back_populates="related_datasheet"
    )
