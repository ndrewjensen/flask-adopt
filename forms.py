"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField, RadioField
from wtforms.validators import InputRequired, Optional, URL, DataRequired

class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField("Name",
                        validators=[InputRequired()])
    species = SelectField("Species",
                        choices=[("cat", "Cat"),
                        ("dog","Dog"),
                        ("porqupine", "Porqupine")],
                        validators=[InputRequired()])
    photo_url = StringField("Photo URL",
                        validators=[InputRequired(),
                        URL()])
    age = SelectField("Age",
                        choices=[("baby", "Baby"),
                        ("young", "Young"),
                        ("adult", "Adult"),
                        ("senior", "Senior")],
                        validators=[InputRequired()])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """Form for editing a pet"""

    photo_url = StringField("Photo URL",
                        validators=[InputRequired(),
                        URL()])

    notes = StringField("Notes")

    available = BooleanField("Availability")