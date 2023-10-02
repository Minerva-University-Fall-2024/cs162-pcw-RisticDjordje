from . import db
from flask_login import UserMixin
from flask_login import LoginManager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    column = db.Column(db.String(25))


