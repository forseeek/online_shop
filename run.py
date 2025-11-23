from app import create_app
from app.models import db
from flask import Flask
import os

# create an app
app = create_app()

# main function that start if file is executed directly
if __name__ == "__main__":
    # Create DB tables if not exist
    with app.app_context():
        db.create_all()

    # start an app in debug mode
    app.run(debug=True)