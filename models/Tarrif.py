from Base import Base
from sqlalchemy import (
    Column, BigInteger, String, DateTime, CheckConstraint, func
)
from sqlalchemy.orm import validates

class Tariff(Base):
    __tablename__ = "tariffs"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    price = Column(BigInteger, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    __table_args__ = (
        CheckConstraint("price > 0", name="ck_tariff_price_positive"),
        CheckConstraint("length(title) > 0", name="ck_tariff_title_not_empty"),
    )

    @validates("price")
    def validate_price(self, key, value):
        if not isinstance(value, int):
            raise ValueError("price must be int (kopecks)")
        if value <= 0:
            raise ValueError("price must be positive")
        return value

    @validates("title")
    def validate_title(self, key, value):
        if not value or not value.strip():
            raise ValueError("title must not be empty")
        return value.strip()