from flask import Flask

from vews import app
from modele import modele
app.config.from_object('config')

modele.db.init_app(app)

@app.cli.command()
def init__db():
    modele.init_db()

init__db()