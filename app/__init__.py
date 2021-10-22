import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/app/uploads'

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("FLASK_SECRET_KEY") or 'prc9FWjeLYh_KsPGm0vJcg',
        SQLALCHEMY_DATABASE_URI='sqlite:///'+ os.path.join(basedir, 'snailmail.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        DEBUG=True
    )
    app.config['UPLOAD_FOLDER'] = os.path.join(basedir,"/app/uploads")

    db.init_app(app)

    migrate = Migrate(app,db)

    from app.auth.views import auth
    from app.main.views import main
    from app.email.views import email
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(email)

    from app.main.errors import page_not_found
    app.register_error_handler(404, page_not_found)

    return app