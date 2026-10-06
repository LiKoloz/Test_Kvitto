from models.Base import Base
from sqlalchemy import (
    Column, BigInteger, DateTime,  func, ForeignKey
)
from sqlalchemy.orm import relationship

class Bank_Status(Base):
    __tablename__ = "bank_statuses"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    payment_id = Column(BigInteger, ForeignKey("payments.id"))
    created_at = Column(DateTime, nullable=False, server_default=func.now())