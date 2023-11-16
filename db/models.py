import uuid

from sqlalchemy import Column, String, TIMESTAMP, func, Integer
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class UserHistory(Base):
    __tablename__ = "user_history"
    id = Column(Integer, primary_key=True)
    link = Column(String, nullable=False)
    time_visited = Column(TIMESTAMP(), default=func.now())
