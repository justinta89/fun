from sqlalchemy import Column, String, Integer
from .db import Base


class UserAdmin(Base):
    __tablename__ = 'useradmin'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

    def __repr__(self):
        return "<User: {0}>".format(self.username)
