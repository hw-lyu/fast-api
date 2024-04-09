# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker, declarative_base
#
# ASYNC_DB_URL = "mysql+aiomysql://test:test_pass@db:3306/demo?charset=utf8"
# async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
# async_session = sessionmaker(
#     autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
# )
#
# Base = declarative_base()
#
#
# async def get_db():
#     async with async_session() as session:
#         yield session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "mysql+pymysql://test:test_pass@db:3306/demo?charset=utf8"

db_engine = create_engine(DB_URL, echo=True)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()


def get_db():
    with db_session() as session:
        yield session
