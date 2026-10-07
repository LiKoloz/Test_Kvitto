FROM python:3

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi "uvicorn[standard]" "sqlalchemy[asyncio]" asyncpg python-dotenv greenlet alembic pytest pytest-asyncio httpx
# изменить номер миграции
CMD ["sh", "-c", "pytest -v && python -m alembic revision --autogenerate -m M1_Name && python -m alembic upgrade head && python main.py"]

