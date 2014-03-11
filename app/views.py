from flask import Blueprint, render_template, redirect, flash
from flask import session, url_for, request, abort
from flask.ext.login import login_required, login_user
from sqlalchemy import desc, asc
from datetime import datetime, date
from app import db
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


# Admin Routes
@admin.route('/admin', methods=['GET', 'POST'])
def adminPage():
    form = updateForm()

    if not session.get('logged_in'):
        return redirect(url_for('admin.login'))

    if form.validate_on_submit():
        post = Post(body=form.newPost.data,
                    title=form.title.data,
                    timestamp=datetime.utcnow())
        db.session.add(post)
        db.session.commit()
        flash("Post successfull")
        return redirect(url_for('admin.adminPage'))

    return render_template('admin.html',
                           form=form)


@admin.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    error = None

    creds = userAdmin.query.first()
    user = creds.uname
    passwd = creds.passwd

    if request.method == 'POST':
        if request.form['username'] != user:
            error = "Invalid credentials"
        elif request.form['password'] != passwd:
            error = "Invalid credentials"
        else:
            session['logged_in'] = True
            return redirect(url_for('admin.adminPage'))

    return render_template('login.html',
                           form=form,
                           error=error)


@admin.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('admin.login'))