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
    return render_template("products_list.html", products=products)


# route for page and request to add a new product
@bp.route("/add", methods=["GET", "POST"])
def add_product():
    # if method type is post, then add a new product
    if request.method == "POST":

        # get data from form and save them in variables
        name = request.form["name"]
        price = request.form["price"]

        description = request.form["description"]
        stock = int(request.form["stock"])
        is_active = request.form.get("is_active") == "on"
        category = request.form["category"]
        rating = float(request.form["rating"])
        sale = request.form.get("sale") == "on"

        print (f'''[DEBUG]: name={name}, price={price}, description={description}, stock={stock}, is_active={is_active}, category={category}, rating={rating}, sale={sale}''')

        # create a new product class
        product = Product(
            name=name,
            price=float(price),
            description=description,
            stock=int(stock),
            is_active=is_active,
            category=category,
            rating=float(rating),
            sale=sale,
        )
        # add product to db
        db.session.add(product)
        # commit changes
        db.session.commit()

        # show message, that product was added
        flash("Product added!")
        # redirect to products page
        return redirect(url_for("routes.products"))
    # if method type is get, then render page with variables action and product
    return render_template("product_form.html", action="Add", product=None)

# route for deleting a product
# <int:product_id> - <type of variable:name variable>
@bp.route("/delete/<int:product_id>", methods=["POST"])
def delete_product(product_id):
    # finding by product_id a product from a database, if not exist - redirect to a 404 error (not founded) page
    product = Product.query.get_or_404(product_id)
    # delete a product from database
    db.session.delete(product)
    # committing a change
    db.session.commit()
    flash("Product deleted!")
    # redirect user to products page
    return redirect(url_for("routes.products"))

# route for updating a product info
# <int:product_id> - <type of variable:name variable>
@bp.route("/update/<int:product_id>", methods=["GET", "POST"])
def update_product(product_id):
    # finding by product_id a product from a database, if not exist - redirect to a 404 error (not founded) page
    product = Product.query.get_or_404(product_id)
    # if method is "POST" - update values in database
    if request.method == "POST":
        # getting values from form
        product.name = request.form["name"]
        product.price = float(request.form["price"])

        product.description = request.form["description"]
        product.stock = int(request.form["stock"])
        product.is_active = request.form.get("is_active") == "on"
        product.category = request.form["category"]
        product.rating = float(request.form["rating"])
        product.sale = request.form.get("sale") == "on"

        print (f'''[DEBUG]: name={product.name}, price={product.price}, description={product.description}, stock={product.stock}, is_active={product.is_active}, category={product.category}, rating={product.rating}, sale={product.sale}''')

        # committing a change
        db.session.commit()
        flash("Product updated!")
        # redirect to a products page
        return redirect(url_for("routes.products"))
    # if method is "GET" - render a page product_form with product info
    return render_template("product_form.html", action="Update", product=product)
