"""
    This is the user module which includes the REST actions for user data
"""

from flask import make_response, abort
from models import User, UserSchema
from config import db


def user_login(email, password):
    # Ignore the mimetype and always try to parse JSON
    user = User.query.filter_by(email=email).first()
    if user:
        user = guard.authenticate(email, password)
        res = {'success': True, 'role': user.role,  'access_token': guard.encode_jwt_token(user)}
        return res


def get_all():
    """
    @route: /api/v1/user
    @method: GET
    @return: json string of list of user
    """
    # Create the list of user
    users = User.query.order_by(User.last_name).all()

    # Serialize the data for the response
    user_schema = UserSchema(many=True)
    data = user_schema.dump(users)
    return data


def get_one(user_id):
    """
    @route: /api/v1/user/:id
    @method: GET
    @return: user that matches the given id
    """
    # Get the user requested
    user = User.query.filter(User.id == user_id).one_or_none()

    # Check if user exists
    if user is not None:
        #Serialize the data for the response
        user_schema = UserSchema()
        data = user_schema.dump(user)
        return data
    else:
        abort(
            404,
            "Couldn't find any user with ID: {user_id}".format(user_id=user_id)
        )


def create_user(user):
    """
    @route: /api/v1/register
    @method: POST
    @return: created user
    """

    email = user.get('email')

    existing_user = (
        User.query.filter(User.email == email)
        .one_or_none()
    )

    # Can we insert this person?
    if existing_user is None:

        # Create a user instance using the schema and the passed in user
        schema = UserSchema()
        new_user = schema.load(user, session=db.session)

        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()

        # Serialize and return the new created user in the response
        data = schema.dump(new_user)

        return data, 201


def update_user(user_id, user):
    """
    @route: /api/v1/user/:id
    @method: PUT
    @return: updated user
    """
    update_user = User.query.filter(
        User.id == user_id
    ).one_or_none()

    # Get existing person to avoid duplicate record after update
    email = user.get('email')
    existing_user = User.query.filter(User.email == email).one_or_none()

    # Check if the user to update exist
    if update_user is None:
        abort(
            404,
            "Couldn't find any user with the ID: {user_id}".format(user_id=user_id)
        )
    # If the update create a duplicate of a existing user
    elif ( existing__user is not None and existing_user.id != user_id ):
        abort(
            409,
            "User with {email} exists already".format(
                email=email
            )
        )
    else:
        # turn the passed into user into a db object
        schema = UserSchema()
        update = schema.load(user, session=db.session)

        # Set the id to the user we want to update
        update.id = update_user.id

        # Merge the new object into the old and commit to db
        db.session.merge(update)
        db.session.commit()

        # return updated user in the sponse
        data = schema.dump(update_user)

        return data, 200


def delete_user(user_id):
    """
    @route: /api/v1/user/:id
    @method: DELETE
    @return: 200 on successful delete, 404 if not found
    """

    # Get the user requested
    user = User.query.filter(User.id == user_id).one_or_none()

    # Check if the user exists
    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return make_response(
            "User {user_id} deleted".format(user_id=user_id), 200
        )
    else:
        abort(
            404,
            "Couldn't find any user with the ID: {user_id}".format(user_id=user_id)
        )

