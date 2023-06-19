from flask import Flask,Blueprint,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_marshmallow import Marshmallow
from application.config import DATABASE_URL,SECRET_KEY

from flask_login import LoginManager
app = Flask(__name__)


app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)

Migrate(app,db)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.Login'

from application.auth.routes import auth
app.register_blueprint(auth)


from application.main.routes import main
app.register_blueprint(main)

