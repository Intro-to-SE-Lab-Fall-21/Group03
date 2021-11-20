from flask_wtf import FlaskForm
from wtforms.fields import PasswordField,SubmitField
from wtforms.validators import InputRequired, DataRequired, Length

class UpdateAccountForm(FlaskForm):
	password 	= PasswordField("Password",
                                    validators=[
                                        InputRequired("Input is required!"),
                                        DataRequired("Data is required!"),
                                        Length(min=10,max=40,message="Password must be at least 10 characters")
                                    ])
	submit  	= SubmitField("Update")