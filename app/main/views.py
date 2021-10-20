from flask import Blueprint, render_template, session,g,request
from app import db, email
from app.main.forms import SearchForm
from app.models import Email,User
from werkzeug.local import LocalProxy

main = Blueprint('main', __name__, template_folder='templates')

current_user = LocalProxy(lambda: get_current_user())


@main.route('/')
def home():

	form = SearchForm(request.args,meta={"csrf": False})
	user_id  = session.get("user_id")
	user = db.session.query(User).filter_by(id=user_id).all()
	user_email = ""
	for row in user:
		user_email = row.email
	emails = db.session.query(Email).filter_by(recipient=user_email)
	if form.validate():
		if form.subject.data.strip():
			search_subject  = form.subject.data
			search_subject = "%" + search_subject +"%"
			print(type(search_subject))
			emails = db.session.query(Email).filter(Email.subject.like(search_subject),Email.uid.like(user_id)).all()
			print(emails)

	
	return render_template('home.html', emails=emails,form=form)



def get_current_user():
    _current_user = getattr(g,"_current_user",None)
    if _current_user is None and session.get("user_id"):
        user = User.query.get(session.get("user_id"))
        if user:
            _current_user = g._current_user = user
    if _current_user is None:
        _current_user = User()
    return _current_user