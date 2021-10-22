from flask_wtf import FlaskForm
from flask import session,g
from wtforms import validators
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField, RadioField, TextAreaField
from wtforms.fields.core import IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, DataRequired, EqualTo, Length, ValidationError, Email
from app.models import User
from werkzeug.local import LocalProxy


class SearchForm(FlaskForm):
    subject = StringField("Subject",validators = [Length(max=30)])
    submit  = SubmitField("Search")