import os
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, declared_attr


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True)


PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://username:passwd@localhost/postgres"
)

engine = create_engine(url=PG_CONN_URI, echo=False)
async_engine = create_async_engine(
    url=PG_CONN_URI,
    echo=False,
)

Base = declarative_base(cls=Base, bind=engine)
Session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


class User(Base):
    __tablename__ = "users"
    name = Column(String)
    username = Column(String)
    email = Column(String)
    posts = relationship("Post", back_populates="user", uselist=True)


class Post(Base):
    __tablename__ = "posts"
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=False)
    title = Column(String)
    body = Column(String)

    user = relationship("User", back_populates="posts", uselist=False)
