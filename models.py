from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    boat_id = db.Column(db.String(100))
    port = db.Column(db.String(100))
    arrival_time = db.Column(db.String(100))
    departure_time = db.Column(db.String(100))