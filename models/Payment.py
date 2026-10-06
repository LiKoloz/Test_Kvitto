from models.Base import Base
from sqlalchemy import (
    Column, BigInteger, String, DateTime, CheckConstraint, func, SmallInteger, ForeignKey
)

from sqlalchemy.orm import relationship, validates

class Payment(Base):
    __tablename__ = "payments"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    email = Column(String, nullable=True)
    method = Column(String, nullable=False)
    installment_months = Column(SmallInteger)
    promo_code = Column(String)
    schedule = Column(BigInteger)
    tariff_id = Column(BigInteger, ForeignKey("tariffs.id"))
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    __table_args__ = (
        CheckConstraint(
            "installment_months IS NULL OR installment_months IN (3, 6, 12)",
            name="ck_payment_installment_months",
        ),
        CheckConstraint(
            "(method != 'installment' AND installment_months IS NULL) "
            "OR (method = 'installment' AND installment_months IS NOT NULL)",
            name="ck_payment_method_installment",
        ),
        CheckConstraint(
            "method IN ('card', 'sbp', 'installment')",
            name="ck_payment_method_values",
        ),
    )

    @validates("email")
    def validate_email(self, key, value):
        if not value or "@" not in value:
            raise ValueError("invalid email")
        return value.strip().lower()

    @validates("method")
    def validate_method(self, key, value):
        if value not in ("card", "sbp", "installment"):
            raise ValueError("method must be card, sbp or installment")
        return value

    @validates("installment_months")
    def validate_installment_months(self, key, value):
        if value is None:
            return None
        if value not in (3, 6, 12):
            raise ValueError("installment_months must be 3, 6 or 12")
        return value

    @validates("promo_code")
    def validate_promo(self, key, value):
        if value is None:
            return None
        value = value.strip().upper()
        if value != "KVITT010":
            raise ValueError("unknown promo code")
        return value
