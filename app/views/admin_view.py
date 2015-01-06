from app.forms import LoginForm, UpdateForm
from app.db.model import UserAdmin, Post, get_session
from flask import render_template, Blueprint, session, flash, url_for
from datetime import datetime

admin = Blueprint('admin', __name__, template_folder='../templates/admin')
sess = get_session()


@admin.route('/admin', methods=['POST'])
def adminPage():
    form = UpdateForm()
    # implement session for logging in.
    if form.validate():
        # create an api class in model to get rid of this stuff, maybe?
        # have the api take the form data, which gets passed into class
        #       in the model api
        post = Post(body=form.new_post.data,
                    title=form.title.data,
                    page=form.dropdown.data,
                    timestamp=datetime.utcnow())

        sess.add(post)
        sess.commit()
        if sess.commit() is True:
            flash('Success')

    return render_template('admin.html',
                           form=form)


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    from app.db.api import Admin
    user = form.username.data
    passwd = form.password.data

    u = Admin.get_username(user)
    p = Admin.get_password(passwd)
    if u and p:
        return redirect(url_for('adminPage'))

    return render_template('login.html',
                           form=form)