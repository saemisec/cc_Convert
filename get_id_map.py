from typing import Type, TypeVar, Dict
from sqlalchemy.orm import Session
from sqlalchemy import select

T = TypeVar("T")

def get_id_map(
    session: Session,
    model: Type[T],
    old_id_field_name: str = "old_id",
    new_id_field_name: str = "id",
) -> Dict[int, int]:
    """
    ساخت mapping بین old_id و id برای یک مدل مشخص.

    Args:
        session: جلسه‌ی فعال SQLAlchemy
        model: مدل SQLAlchemy (مثلاً Parent)
        old_id_field_name: نام فیلد کلید قدیمی (پیش‌فرض 'old_id')
        new_id_field_name: نام فیلد کلید جدید (پیش‌فرض 'id')

    Returns:
        dict مثل {old_id: new_id}
    """
    old_id_attr = getattr(model, old_id_field_name)
    new_id_attr = getattr(model, new_id_field_name)

    result = session.execute(select(old_id_attr, new_id_attr)).all()
    return {old: new for old, new in result}
