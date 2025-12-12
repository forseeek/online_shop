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

# route for page and request to add a new product
@bp.route("/add", methods=['GET', 'POST'])
def add_product():
    # if method type is post, then add a new product
    if request.method == 'POST':

        # get data from form and save them in variables
        name = request.form['name']
        price = request.form['price']
        
        description = request.form['description']
        stock = request.form['stock']
        is_active = request.form.get('is_active') == 'on'
        category = request.form['category']
        rating = request.form['rating']
        sale = request.form.get('sale') == 'on'

        # create a new product class
        product = Product(
            name=name, 
            price=float(price),
            description=description,
            stock=int(stock),
            is_active=is_active,
            category=category,
            rating=float(rating),
            sale=sale)
        # add product to db
        db.session.add(product)
        # commit changes
        db.session.commit()

        # show message, that product was added
        flash('Product added!')
        # redirect to products page
        return redirect(url_for('routes.products'))
    # if method type is get, then render page with variables action and product
    return render_template('product_form.html', action='Add', product=None)