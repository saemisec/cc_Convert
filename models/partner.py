from typing import TYPE_CHECKING, List, Optional
from .base import Base
from sqlalchemy import Boolean, String, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column

if TYPE_CHECKING:
    from .bank_account import Bank_Account
    from .pre_contract import Pre_contract
    from .bidder_list import Bidder_list


class Partner(Base):
    __tablename__ = "partner"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id: Mapped[int | None]
    full_name: Mapped[str] = mapped_column(String(100))
    national_id: Mapped[str | None] = mapped_column(String(20))
    economic_code: Mapped[str | None] = mapped_column(String(20))
    is_legal_entity: Mapped[bool]
    address: Mapped[str] = mapped_column(String(200))
    is_vendor: Mapped[bool]
    is_contructor: Mapped[bool]
    member_of_avl: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String(120), index=True, default=None)
    bank_account: Mapped[List["Bank_Account"]] = relationship(
        back_populates="partner", lazy="selectin"
    )
    pre_contract: Mapped[List["Pre_contract"]] = relationship(
        back_populates="partner", lazy="selectin"
    )
    bidder_lists: Mapped[List["Bidder_list"]] = relationship(back_populates="partner")
    # won_tenders: Mapped[List["Tender"]] = relationship(
    #     foreign_keys="[Tender.winner_id]", back_populates="winner"
    # )
    # bidders: Mapped[List["Bidder"]] = relationship(back_populates="partner")
    # inqueries: Mapped[List["Inquery"]] = relationship(back_populates="partner")

    __table_args__ = (
        UniqueConstraint(
            "national_id", "economic_code", name="uq_partner_identification"
        ),
    )
