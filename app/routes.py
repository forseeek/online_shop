from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Product

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

@bp.route("/products")
def products():
    # gets products from database
    products = Product.query.all()
    # render product_list.html
    return render_template("products_list.html",
                           products=products)

@bp.route("/add", methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':

        name = request.form['name']
        price = request.form['price']

        product = Product(name=name, price=float(price))
        db.session.add(product)
        db.session.commit()

        flash('Product added!')
        return redirect(url_for('routes.products'))
    return render_template('product_form.html', action='Add', product=None)