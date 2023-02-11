from . import db
from flask_login import UserMixin 
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(200))
    prenom = db.Column(db.String(200))  
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100)) 



