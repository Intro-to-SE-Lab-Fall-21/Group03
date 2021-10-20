from flask import Blueprint, render_template, session,g
from app import db, email
from app.models import Email,User
from werkzeug.local import LocalProxy

main = Blueprint('main', __name__, template_folder='templates')

current_user = LocalProxy(lambda: get_current_user())


@main.route('/')
def home():
	
	user_id  = session.get("user_id")
	print(type(user_id))
	#user_email=  User.query(email).filter_by(id=user_id)
	user = db.session.query(User).filter_by(id=user_id).all()
	user_email = ""
	for row in user:
		user_email = row.email
	emails = db.session.query(Email).filter_by(recipient=user_email)
	return render_template('home.html', emails=emails)



def get_current_user():
    _current_user = getattr(g,"_current_user",None)
    if _current_user is None and session.get("user_id"):
        user = User.query.get(session.get("user_id"))
        if user:
            _current_user = g._current_user = user
    if _current_user is None:
        _current_user = User()
    return _current_user