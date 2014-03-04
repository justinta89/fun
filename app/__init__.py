from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import basedir


app = Flask(__name__)
app.config.from_object('config')

# initialize DataBase
db = SQLAlchemy(app)


from app.views import default, admin
app.register_blueprint(default)
app.register_blueprint(admin)


from app import views, constants