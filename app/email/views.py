from os.path import join,dirname,realpath
from flask import Blueprint,session,g, render_template, flash, redirect, url_for,request
from app.email.forms import CompositionForm
from app import db
from app.models import Email,User
from werkzeug.utils import secure_filename


email = Blueprint("email", __name__, template_folder="templates")

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

UPLOADS_PATH = join(dirname(realpath(__file__)), 'uploads\\')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@email.route("/compose", methods=["GET", "POST"])
def compose():
    form = CompositionForm()
    
    if form.validate_on_submit():
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(form.file.data.filename)
            form.file.data.save(UPLOADS_PATH + filename)
            
        recipient    = form.recipient.data
        subject      = form.subject.data
        body         = form.body.data
        file         = form.file.data.filename
        uid         = session.get('user_id')
        
        email = Email(recipient, subject, body,file,uid)
        db.session.add(email)
        db.session.commit()
        flash("Email sent succesfully", "success")
        return redirect(url_for("main.home"))

    return render_template("new_email.html", form=form)

@email.route("/view_email/<int:email_id>",methods=["GET"])
def view_email(email_id):
    email_from_db = db.session.query(Email).filter_by(id=email_id)
    if email_from_db:
        for row in email_from_db:
            sender_id = row.uid
            email_filename = row.filename
            email_subject = row.subject
            email_body = row.body
    sender  = db.session.query(User).filter_by(id=sender_id)

    uploads = UPLOADS_PATH
    print(email_filename)
    if sender:
        for row in sender:
            sender_email = row.email
        return render_template("email.html",sender_email=sender_email,email_filename=email_filename,email_subject=email_subject,email_body=email_body,uploads=uploads)
    
    return redirect(url_for("main.home"))

    

    

    


