from app.forms import LoginForm, UpdateForm
from app.model import UserAdmin, Post, get_session
from flask import (render_template, Blueprint, flash, url_for, redirect,
                   session, request)
from datetime import datetime

admin = Blueprint('admin', __name__, template_folder='../templates/admin')
s = get_session()


@admin.route('/admin', methods=['GET', 'POST'])
def adminPage():
    form = UpdateForm()
    if not session['logged_in']:
        return redirect(url_for('admin.login'))
    else:
        if form.validate():
            post = Post(body=form.new_post.data,
                        title=form.title.data,
                        page=form.dropdown.data,
                        timestamp=datetime.utcnow())

            s.add(post)
            s.commit()
            if s.commit() is True:
                flash('Success')

        return render_template('admin.html',
                               form=form)


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    admin = s.query(UserAdmin).first()

    if request.method == 'POST':
        if request.form['username'] != admin.username:
            error = 'Invalid Credentials'
        elif request.form['password'] != admin.password:
            error = 'Invalid Credentials'
        else:
            session['logged_in'] = True
            flash('Logged in!')
            return redirect(url_for('admin.adminPage'))
    return render_template('login.html', form=form, error=error)


@admin.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('admin.login'))
