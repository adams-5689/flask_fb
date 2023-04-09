from flask_sqlalchemy import SQLAlchemy
import logging as lg
from vews import app
app.config.from_object('config')

db  = SQLAlchemy(app)

class content(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    descriptoin  = db.Column(db.String(200), nullable = False)
    gender = db.Column(db.Integer, nullable = False)

    def __init__(self, description, gender) -> None:
        self.descriptoin = description
        self.gender = gender
    db.create_all()


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(content("THIS IS SPARTAAAAAAA!!!", 1))
    db.session.add(content("What's your favorite scary movie?", 0))
    db.session.commit()
    lg.warning('Database initialized!')