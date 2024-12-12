from sqlalchemy import Column , String ,Integer
from .database import Base

class BlogsTable(Base):
    __tablename__ = "blogstable"

    id = Column(Integer,primary_key=True)
    body = Column(String)
    title = Column(String)

