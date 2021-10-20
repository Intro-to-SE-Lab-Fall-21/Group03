from flask_wtf import FlaskForm
from flask import session,g
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField, RadioField, TextAreaField
from wtforms.fields.core import IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, DataRequired, EqualTo, Length, ValidationError, Email
from app.models import User
from werkzeug.local import LocalProxy
        


class CompositionForm(FlaskForm):
    recipient            = EmailField("Email *",
                                validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!"),
                                    Length(min=10, max=30, message="Email must be between 10 and 30 characters long"),
                                    Email("You did not enter a valid email!")
                                ])
    subject              = StringField("Subject *",
                                validators=[
                                    InputRequired("Input is required!"),
                                    DataRequired("Data is required!"),
                                    Length(min=4, max=30, message="Subject must be between 4 and 30 characters long"),
                                ])
    body                 = StringField("Body *",
                                    validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!"),
                                        Length(min=10, max=255, message="Body must be between 10 and 255 characters long"),
                                    ])
    uid                 = IntegerField(0)
    submit              =  SubmitField("Send")


