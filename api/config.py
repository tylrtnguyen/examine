import os
import flask
import flask_sqlalchemy
import flask_praetorian
import flask_cors
import flask_marshmallow

# Initialize flask app
app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'secretpassword'
app.config['JWT_ACCESS_LIFESPAN'] = { 'hours': 24 } 
app.config['JWT_REFRESH_LIFESPAN'] = { 'days': 7 }

# Initilizes Marshmallow
ma = flask_marshmallow.Marshmallow(app)

db = flask_sqlalchemy.SQLAlchemy()
guard = flask_praetorian.Praetorian()
cors = flask_cors.CORS()




from models import User
# Initialize the flask-preaetorian instance
guard.init_app(app, User)

# Initialize a local database
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.getcwd(), 'database.db')}"
db.init_app(app)

# Initializes CORS
cors.init_app(app)



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







