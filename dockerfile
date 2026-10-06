CMD pip install python-dotenv
CMD pip install greenlet
CMD pip install asyncpg
CMD python -m alembic revision --autogenerate -m "Create initial tables"
CMD python -m alembic upgrade head