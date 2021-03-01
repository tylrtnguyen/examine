import os
import flask
import flask_sqlalchemy
import flask_marshmallow
import flask_praetorian
import flask_cors
import connexion
from flask_swagger_ui import get_swaggerui_blueprint


# Initialize flask app

basedir = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask(__name__)

SWAGGER_URL = "/api/v1"
API_URL = "/static/swagger.yml"
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name':"Examine REST API V1"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

# Create the SQLite URL for SQLAlchemy
sqlite_url = "sqlite:///" + os.path.join(basedir, "database.db")

app.config['SECRET_KEY'] = 'secretpassword'
app.config['JWT_ACCESS_LIFESPAN'] = { 'hours': 24 } 
app.config['JWT_REFRESH_LIFESPAN'] = { 'days': 7 }
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

guard = flask_praetorian.Praetorian()
cors = flask_cors.CORS()


# Create the SQLAlchemy db instance
db = flask_sqlalchemy.SQLAlchemy()
db.init_app(app)
cors.init_app(app)
# Initilizes Marshmallow
ma = flask_marshmallow.Marshmallow(app)

from models import User

# Initialize the flask-preaetorian instance
guard.init_app(app, User)


import routes


# Create an admin user for testing purpose
with app.app_context():
    db.create_all()
    if db.session.query(User).filter_by(email='admin@examine.com').count() < 1:
        db.session.add(User(
            first_name = 'Thong',
            last_name = 'Nguyen',
            email = 'admin@examine.com',
            password = guard.hash_password('password'),
            role = 'admin'
        ))
    db.session.commit()




