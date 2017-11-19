from flask_wtf import FlaskForm as Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

# Create a Login Form class with 'fields' represented from wtforms module
class LoginForm(Form):
    # Form Validation on this field is that this is a Required Field
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)