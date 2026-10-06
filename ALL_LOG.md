Использовал DEEPSEEK

Alembic - расскажи мне про него, как его настроить?

from Base import Base
from sqlalchemy import  Column,BigInteger, String, DateTime
class Tariff(Base):
    __tablename__ = "tareffs"

    id = Column(BigInteger, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(BigInteger, nullable=False)
    created_at = Column(DateTime, nullable=False)
Как добавить сюда валидацию?