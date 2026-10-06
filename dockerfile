CMD pip install sqlalchemy
CMD pip install python-dotenv
CMD pip install greenlet
CMD pip install asyncpg
# изменить номер миграции
CMD python -m alembic revision --autogenerate -m "N1_0" 
CMD python -m alembic upgrade head

