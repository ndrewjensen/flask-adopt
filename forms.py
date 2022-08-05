"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class AddPetForm(FlaskForm):
    """Form for adding a pet"""

#FIXME: This is NOT DONE
    name = StringField("Name")
    Species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = StringField("Age")
    notes = StringField("Notes")
    