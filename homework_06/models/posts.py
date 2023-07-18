from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from typing import TYPE_CHECKING
from .database import db

if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)


    if TYPE_CHECKING:
        query: Query

