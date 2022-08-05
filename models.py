"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)

class Pet(db.model):
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.text,
                     nullable=False)
    species = db.Column(db.text,
                        nullable=False)
    photo_url = db.Column(db.text,
                          nullable=False,
                          default='')
    age = db.Column(db.text,
                    nullable=False)
    notes = db.Column(db.text,
                    nullable=True)
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=1)
    