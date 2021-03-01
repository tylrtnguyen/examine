from datetime import datetime
from config import db, ma
from marshmallow_sqlalchemy import ModelSchema


# A generic user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    role = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @classmethod
    def lookup(cls, email):
        return cls.query.filter_by(email=email).one_or_none()

    @property
    def identity(self):
        return self.id


class UserSchema(ModelSchema):
    class Meta:
        model = User
        sqla_session = db.session