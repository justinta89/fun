from wtforms import (Form, TextField, PasswordField, SubmitField,
                     TextAreaField, SelectField)
from wtforms.validators import Required


class LoginForm(Form):
    username = TextField('username', validators=[Required()])
    password = PasswordField('password', validators=[Required()])


class UpdateForm(Form):
    new_post = TextAreaField('newPost', validators=None)
    title = TextField('title', validators=[Required()])
    dropdown = SelectField('Page', choices=[('m', 'Main'), ('s', 'Security')])
    submit = SubmitField('Submit')
