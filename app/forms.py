from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField, SubmitField
from wtforms import TextAreaField
from wtforms.validators import Required


class LoginForm(Form):
    username = TextField('username', validators = [Required()])
    password = PasswordField('password', validators = [Required()])
    remember_me = BooleanField('remember_me')
    submit = SubmitField('Login')


class updateForm(Form):
    newPost = TextAreaField('newPost', validators=None)
    submit = SubmitField('Submit')