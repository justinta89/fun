from flask import Blueprint, render_template, redirect, flash
from flask import session, url_for, request
from app import constants
from .forms import LoginForm, updateForm
from .model import userAdmin


"""Blueprints"""
default = Blueprint('default', __name__, template_folder='templates')
admin = Blueprint('admin', __name__, template_folder='templates/admin')


"""Default Routes"""
@default.route('/')
def index():
    return render_template('index.html', LST = constants.LST, SOCIALLIST = constants.SOCIALLIST)


@default.route('/resume')
def resume():
    return render_template('resume.html', LST = constants.LST, SOCIALLIST = constants.SOCIALLIST)


@default.route('/security')
def security():
    return render_template('security.html', LST = constants.LST, SOCIALLIST = constants.SOCIALLIST)


"""Admin Routes"""
@admin.route('/admin')
def adminPage():

    form = updateForm()

    if 'username' in session:
        return render_template('admin.html', form=form)
    else:
        return redirect(url_for('login'))


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

    return render_template('login.html', form=form, error=error)


@admin.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))