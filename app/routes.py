from flask import Blueprint, render_template

# create a blueprint class, that allows to organize app routes into separate files
bp = Blueprint("routes", __name__)

# define a route for the main page
@bp.route("/")
def index():
    # return the html file for page
    return render_template("index.html")

@bp.route("/contacts")
def contacts():
    return render_template("contacts.html")