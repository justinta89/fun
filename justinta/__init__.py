from justinta.views import default, admin
from flask import Flask

app = Flask(__name__)

app.register_blueprint(default)
app.register_blueprint(admin)