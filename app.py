"""Flask app for adopt app."""

from flask import Flask, render_template, request, redirect

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def display_homepage():
    """display homepage"""

    pets = Pet.query.all()

    return render_template('index.html',pets=pets)

@app.route("/add", methods= ["GET","POST"])
def add_pet():
    """Show pet form and add pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name = name, species = species, photo_url = photo_url, age= age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("addpet.html", form=form)

@app.route("/<int:pet_id>", methods = ["GET", "POST"])
def edit_pet(pet_id):
    """Edit animal Form """
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj = pet)

    if form.validate_on_submit():

        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(photo_url = photo_url, notes=notes, available = available)
        db.session.commit()
        return redirect(f'/{pet_id}')
    else:
        return render_template("petinfo.html", pet=pet, form=form)

