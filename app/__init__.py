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

    # load config from JSON file
    config_path = os.path.join(base_dir, 'config.json')
    with open(config_path) as f:
        config = json.load(f)
    app.config.update(config)

    # set up SQLAlchemy with absolute DB path
    db_path = os.path.abspath(os.path.join(base_dir, config['DB_PATH']))

    # ensure the DB directory exists so SQLite can create the file
    db_dir = os.path.dirname(db_path)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
    # set up SQLAlchemy
    # sets path to database
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    # disable unnecessary message
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # import db and init db
    from .models import db
    db.init_app(app)

    # import blueprint that contains routes
    from .routes import bp as routes_bp

    # register blueprint that adds routes defined in it to the site
    app.register_blueprint(routes_bp)
    # return the fully configured Flask app
    return app
