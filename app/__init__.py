from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import basedir


app = Flask(__name__)
app.config.from_object('config')

# initialize DataBase
db = SQLAlchemy(app)

# LoginManager
lm = LoginManager()
lm.init_app(app)


from app.views import default, admin
app.register_blueprint(default)
app.register_blueprint(admin)


from app import views, constants