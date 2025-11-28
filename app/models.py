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