from app import create_app
from flask import Flask
import os

# create an app
app = create_app()

# main function that start if file is executed directly
if __name__ == "__main__":
    # start an app in debug mode
    app.run(debug=True)