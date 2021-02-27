import flask
import sqlite3 as sql
import flask_praetorian
import json
import collections
from config import db, guard, app
from flask import jsonify
from models import User
from user import get_all, get_one, create_user, update_user, delete_user, user_login

# Set up routes
@app.route('/')
def home():
    return {"Success": True, "message": "Welcome to api.examine.com"}


@app.route('/api/v1')
def index():
    """
        The root of the API
    """
    return { "success": True, "message": "Your API is working properly" }, 200

"""
    ADD A NEW USER TO THE DATABASE
    @route: /api/v1/register
    @method: POST
    @return: status, user's info
"""
@app.route('/api/v1/register', methods=['POST'])
def register():
    """
        Registers a new user using the credentials that they send
    """
    # Get the data from client
    req = flask.request.get_json(force=True)
    first_name = req.get('firstName', None)
    last_name = req.get('lastName', None)
    email = req.get('email', None)
    password = req.get('password', None)
    # Hash password using flask_praetorian guard
    hashed_password = guard.hash_password(password)
    assigned_role = 'examinee'
    user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password, role=assigned_role)
    # Create a new user
    new_user = create_user(user)
    return { 'success': True, 'user': f"{first_name} {last_name}"}, 201
    

"""
    LOGS A USER IN THE SYSTEM AND ISSUES A TOKEN
    @route: /api/v1/login
    @method: POST
    @return: status, access_token
"""
@app.route('/api/v1/login', methods=['POST'])
def login():
    """
        Logs a user in by parsing the data sending from a POST request then issue a corresponding JWT for user
    """
    # Ignore the mimetype and always try to parse JSON
    req = flask.request.get_json(force=True)
    email = req.get('email', None)
    password = req.get('password', None)
    user = user_login(email, password)
    if user:
        return user
   


"""
    GET ALL USERS
    @route: /api/v1/user
    @method: GET
    @return: json string of list of user
"""
@app.route('/api/v1/user', methods=['GET'] )
@flask_praetorian.auth_required
def get_all_user():
    users = get_all()
    return {"success": True, "data": users}


"""
    GET A SPECIFIC USER
    @route: /api/v1/user/:id
    @method: GET
    @return: user that matches the given id
"""
@app.route('/api/v1/user/<int:user_id>', methods=['GET'])
@flask_praetorian.auth_required
def get_one_user(user_id):
    user = get_one(user_id)
    return {"success": True, "data": user}, 200


"""
    UPDATE A USER GIVEN USER_ID
    @route: /api/v1/user/:id
    @method: PUT
    @return: updated user
"""
@app.route('/api/v1/user/<int:user_id>', methods=['PUT'])
@flask_praetorian.auth_required
def update_user(user_id):
    # Get user's info
    req = flask.request.get_json(force=True)
    first_name = req.get('firstName', None)
    last_name = req.get('lastName', None)
    email = req.get('email', None)
    password = req.get('password', None)
    # Hash password using flask_praetorian guard
    hashed_password = guard.hash_password(password)
    assigned_role = 'examinee'
    # Create an object for new examinee
    user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password, role=assigned_role)
    update_user = update_user(user)
    return { "success": True, "user": update_user }, 200


"""
    DELETE A USER
    @route: /api/v1/user/:id
    @method: DELETE
    @return: status
"""
@app.route('/api/v1/user/<int:user_id>', methods=['DELETE'])
@flask_praetorian.auth_required
def delete(user_id):
    res = delete_user(user_id)
    return { "success": True }, 200



