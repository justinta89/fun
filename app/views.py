from flask import Blueprint, render_template, redirect, flash
from flask import session, url_for, request
from flask.ext.login import login_required, login_user
from sqlalchemy import desc, asc
from datetime import datetime, date
from app import db, lm
from app import constants
from .forms import LoginForm, updateForm
from .model import userAdmin, Post


# Blueprints
default = Blueprint('default', __name__, template_folder='templates')
admin = Blueprint('admin', __name__, template_folder='templates/admin')


# Default Routes
@default.route('/', methods=['GET', 'POST'])
def index():
    posts = Post.query.order_by(desc(Post.timestamp)).all()
    return render_template('index.html',
                           LST=constants.LST,
                           SOCIALLIST=constants.SOCIALLIST,
                           posts=posts)


@default.route('/resume')
def resume():
    github = {
        'irc': 'https://github.com/justinta89/AL-MTG',
        'site': 'https://github.com/justinta89/fun'
    }

    return render_template('resume.html',
                           LST=constants.LST,
                           SOCIALLIST=constants.SOCIALLIST,
                           github=github)


@default.route('/security')
def security():
    return render_template('security.html',
                           LST=constants.LST,
                           SOCIALLIST=constants.SOCIALLIST)


# LoginManager
@lm.user_loader
def load_user(userid):
    return userAdmin.get(userAdmin.id)


# Amin Routes
@admin.route('/admin', methods=['GET', 'POST'])
def adminPage():
    form = updateForm()

    if form.validate_on_submit():
        post = Post(body=form.newPost.data,
                    title=form.title.data,
                    timestamp=datetime.utcnow())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('admin.adminPage'))

    return render_template('admin.html',
                           form=form)


@admin.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    error = None

    if request.method == 'POST':
        session['username'] = request.form['username']
        password = request.form['password']

        res = userAdmin.query.first()

        uname = res.uname
        passwd = res.passwd

        if session['username'] == uname and password == passwd:
            return redirect('/admin')
        else:
            error = "Invalid Credentials"

    return render_template('login.html',
                           form=form,
                           error=error)


@admin.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))