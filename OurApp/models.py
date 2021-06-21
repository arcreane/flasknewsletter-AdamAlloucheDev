from datetime import datetime
from flask_login import UserMixin
from OurApp import login_manager, db


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    firstname = db.Column(db.String(128), nullable=False)
    lastname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime(1), default=datetime.utcnow)
    is_admin = db.Column(db.Integer, default=0, nullable=False)


class Categories(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=False, nullable=False)
    description = db.Column(db.String(256), unique=False, nullable=True)
    img = db.Column(db.Text, unique=False, nullable=False)


class Subscriptions(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=False, nullable=False)
    category_id = db.Column(db.Integer, unique=False, nullable=False)
