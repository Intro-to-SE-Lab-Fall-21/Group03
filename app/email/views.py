from flask import Blueprint,session,g, render_template, flash, redirect, url_for
from app.email.forms import CompositionForm
from app import db
from app.models import Email
from werkzeug.local import LocalProxy


email = Blueprint("email", __name__, template_folder="templates")


@email.route("/compose", methods=["GET", "POST"])
def compose():
    form = CompositionForm()

    if form.validate_on_submit():
        recipient    = form.recipient.data
        subject      = form.subject.data
        body         = form.body.data
        uid         = session.get('user_id')
        
        email = Email(recipient, subject, body,uid)
        db.session.add(email)
        db.session.commit()
        flash("Email sent succesfully", "success")
        return redirect(url_for("main.home"))

    return render_template("new_email.html", form=form)

@email.route("/view_email/<int:email_id>",methods=["GET"])
def view_email(email_id):

    email_from_db = db.session.query(Email).filter_by(id=email_id)

    


