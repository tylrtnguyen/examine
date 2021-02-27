import flask
import sqlite3 as sql
import flask_praetorian
import json
import collections
from config import db, guard, app
from flask import jsonify
from models import User
from user import get_all, get_one, create_user, update_user, delete_user

# Set up routes
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
    Examinee = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password, role=assigned_role)
    db.session.add(Examinee)
    db.session.commit()
    return { 'success': True, 'examinee': f"{first_name} {last_name}"}, 200
    

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
    user = User.query.filter_by(email=email).first()
    if user:
        user = guard.authenticate(email, password)
        res = {'status': 'success', 'role': user.role,  'access_token': guard.encode_jwt_token(user)}
        return res, 200
    return {'success': False }, 401


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
    return {"success": True, "data": users}, 200



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
    # Get 
