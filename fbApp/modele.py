from flask_sqlalchemy import SQLAlchemy

from .vews import app

db  = SQLAlchemy(app)

class content(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    descriptoin  = db.Column(db.String(200), nullable = False)
    gender = db.Column(db.Integer, nullable = False)

    def __init__(self, description, gender) -> None:
        self.descriptoin = description
        self.gender = gender
db.create_all()