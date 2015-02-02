from flask import render_template, Blueprint
from app.model import UserAdmin, Post, get_session
from app.constants import LST, SOCIALLIST

default = Blueprint('default', __name__, template_folder='../templates')
session = get_session()


@default.route('/')
def index():
    return render_template('index.html',
                           LST=LST,
                           SOCIALLIST=SOCIALLIST)


@default.route('/resume')
def resume():
    github = {'irc': 'https://github.com/justinta89/AL-MTG/blob/master/' +
              'mtgcard_request.py'}
    return render_template('resume.html',
                           LST=LST,
                           SOCIALLIST=SOCIALLIST,
                           github=github)


@default.route('/security')
def security():
    return render_template('security.html',
                           LST=LST,
                           SOCIALLIST=SOCIALLIST)
