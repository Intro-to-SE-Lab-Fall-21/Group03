from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from secrets import token_urlsafe
from datetime import datetime

def generate_token():
    return token_urlsafe(20)

def generate_hash(token):
    return generate_password_hash(token)

def _check_token(hash,token):
    return check_password_hash(hash,token)

class Role:
    ADMIN   = 1
    CLIENT  = 2

class Remember(db.Model):
    __tablename__= "remembers"
    id                 = db.Column(db.Integer(), primary_key=True)
    remember_hash      = db.Column(db.String(255), nullable=False)
    user_id            = db.Column(db.Integer(), db.ForeignKey("users.id"), index=True, nullable=False)

    def __init__(self,user_id):
        self.token         = generate_token()
        self.remember_hash = generate_hash(self.token)
        self.user_id       = user_id

    def check_token(self,token):
        return _check_token(self.remember_hash,token)

class User(db.Model):
    __tablename__ = "users"

    id                 = db.Column(db.Integer(), primary_key=True)
    username           = db.Column(db.String(64), unique=True, nullable=False)
    email              = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password_hash      = db.Column(db.String(255), nullable=False)
    remember_hashes    = db.relationship("Remember", backref="user",lazy="dynamic",cascade="all,delete-orphan")
    role_id            = db.Column(db.Integer(),default=0)
    
    
    def __init__(self, username="", email="", password="",role_id=Role.ADMIN):
        self.username         = username
        self.email            = email
        self.password_hash    = generate_password_hash(password)
        self.role_id          = role_id
        
        if role_id ==  Role.ADMIN:
            self.activated    = True
        else:
            self.activated    = False

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError("Password should not be read like this")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_authenticated(self):
        return not  "" == self.username

    def is_anonymous(self):
        return "" == self.username

    def get_remember_token(self):
        remember_instance = Remember(self.id)
        db.session.add(remember_instance)
        return remember_instance.token

    def check_remember_token(self,token):
        if token:
            for remember_hash in self.remember_hashes:
                if remember_hash.check_token(token):
                    return True
        return False
    
    def forget(self):
        self.remember_hashes.delete()

    def is_admin(self):
        return self.role_id == Role.ADMIN

    def is_role(self,role):
        return self.role_id == role

    



class Email(db.Model):
    __tablename__ = "emails"

    id                  = db.Column(db.Integer(), primary_key=True)
    recipient           = db.Column(db.String(64), nullable=False)
    subject             = db.Column(db.String(64), index=True, nullable=False)
    body                = db.Column(db.String(255), nullable=False)
    filename            = db.Column(db.String(64),nullable=True)
    uid                 = db.Column(db.Integer(), nullable=False)
    #deleted            = db.Column(db.Boolean,nullable=False,default=False)

    def __init__(self, recipient="", subject="", body="",filename = "",uid=0):
        self.recipient      = recipient
        self.subject        = subject
        self.body           = body
        self.filename       = filename
        self.uid            = uid
        #self.deleted        = deleted


    #def is_deleted(self,deleted):
        #return self.role_id == deleted

class Deleted_Email(db.Model):
    __tablename__ = "deleted_emails"

    id                  = db.Column(db.Integer(), primary_key=True)
    recipient           = db.Column(db.String(64), nullable=False)
    subject             = db.Column(db.String(64), index=True, nullable=False)
    body                = db.Column(db.String(255), nullable=False)
    filename            = db.Column(db.String(64),nullable=True)
    uid                 = db.Column(db.Integer(), nullable=False)
    #deleted            = db.Column(db.Boolean,nullable=False,default=False)

    def __init__(self, recipient="", subject="", body="",filename = "",uid=0):
        self.recipient      = recipient
        self.subject        = subject
        self.body           = body
        self.filename       = filename
        self.uid            = uid
