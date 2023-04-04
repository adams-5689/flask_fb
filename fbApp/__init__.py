from flask import Flask

from vews import app
from . import modele

modele.db.init_app(app)

@app.cli.command()
def init__db():
    modele.init_db()

init__db()