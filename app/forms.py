from flask.ext.wtf import Form
from wtforms import (TextField, PasswordField, BooleanField, SubmitField,
                     TextAreaField, SelectField)
from wtforms.validators import Required


class LoginForm(Form):
    username = TextField('username', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('remember_me')


class updateForm(Form):
    newPost = TextAreaField('newPost', validators=None)
    title = TextField('title', validators=[Required()])
    dropdown = SelectField('Page', choices=[('m', 'Main'), ('s', 'Security')])
    submit = SubmitField('Submit')