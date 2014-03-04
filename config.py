import os
basedir = os.path.abspath(os.path.dirname(__file__))

# database_uri is required by SQLAlchemy. it's the path of the db files
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# migrate_pro is where we will store SQLAlchemy-migrate data files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = "Change in prod"