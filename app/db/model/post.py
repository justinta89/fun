from sqlalchemy import String, Column, Integer, DateTime
from .db import Base


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    body = Column(String)
    title = Column(String)
    page = Column(String)
    timestamp = Column(DateTime)

    def __init__(self, body, title, page, timestamp):
        self.body = body
        self.title = title
        self.page = page
        self.timestamp = timestamp

    def __str__(self):
        return self.title

    def __repr__(self):
        return "<Title: {0}\nBody: {1}".format(self.title, self.body)