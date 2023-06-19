from application import db,login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name =db.Column(db.String(100))
    last_name =db.Column(db.String(100))
    email = db.Column(db.String(200))
    password = db.Column(db.String(250))

    company_id = db.Column(db.ForeignKey('company.company_id'), nullable=True)
    is_admin = db.Column(db.Integer)
