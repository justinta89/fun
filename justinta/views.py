from flask import Blueprint, render_template, redirect
default = Blueprint('default', __name__)
admin = Blueprint('admin', __name__)

LST = ["index", "blog"]
SOCIALLIST = ["facebook", "twitter", "linkedin", "github"]


@default.route('/')
def index():
    return render_template('index.html', LST = LST, SOCIALLIST = SOCIALLIST)


@default.route('/blog')
def blog():
    return render_template('blog.html', LST = LST, SOCIALLIST = SOCIALLIST)

@admin.route('/admin')
def adminPage():
    return render_template('admin.html')