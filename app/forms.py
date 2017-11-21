from flask_wtf import FlaskForm as Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length

# Create a Login Form class with 'fields' represented from wtforms module
class LoginForm(Form):
    # Form Validation on this field is that this is a Required Field
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

# Create an Edit Profile Form with 'fields' from wtforms module
class EditForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0,max=140)])