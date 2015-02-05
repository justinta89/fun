from flask import render_template, Blueprint
from app.model import Post, get_session
from app.constants import SOCIALLIST

default = Blueprint('default', __name__, template_folder='../templates')
session = get_session()


@default.route('/')
def index():
    post = session.query(Post).all()
    return render_template('index.html',
                           SOCIALLIST=SOCIALLIST,
                           post=post)


@default.route('/resume')
def resume():
    github = {'irc': 'https://github.com/justinta89/AL-MTG/blob/master/' +
              'mtgcard_request.py'}
    return render_template('resume.html',
                           SOCIALLIST=SOCIALLIST,
                           github=github)
