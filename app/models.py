from flask_sqlalchemy import SQLAlchemy

# create db object
db = SQLAlchemy()

# create product table in database
class Product(db.Model):
    # give name of table
    __tablename__ = "products"
    # define attributes of table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    stock = db.Column(db.Integer, default=0, nullable=True)
    is_active = db.Column(db.Boolean, default=True, nullable=True)
    category = db.Column(db.String(50), nullable=True)
    rating = db.Column(db.Float, default=0, nullable=True)
    sale = db.Column(db.Boolean, default=False, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())