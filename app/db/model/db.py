from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = scoped_session(sessionmaker(bind=engine))
get_session = lambda: Session()


from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()