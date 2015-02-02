from flask import Flask

app = Flask(__name__)
app.config.from_object('config.Dev')

from app.views.default_view import default
from app.views.admin_view import admin
app.register_blueprint(admin)
app.register_blueprint(default)

from .model.post import Post
from .model.user_admin import UserAdmin
