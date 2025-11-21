from flask import Flask
import json
import os

# function that creates an web app
def create_app():
    # define a base project directory
    base_dir = os.path.abspath(os.path.dirname(__file__) + "/..")
    # create the Flask app and define folder for templates and static files
    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static"),
    )

    # import blueprint that contains routes
    from .routes import bp as routes_bp

    # register blueprint that adds routes defined in it to the site
    app.register_blueprint(routes_bp)
    # return the fully configured Flask app
    return app
