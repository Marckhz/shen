from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from api.models.crud.users.users_actions import (
                                                read_all_users, 
                                                create_user, 
                                                get_by_id, 
                                                read_words_to_learn_user,
                                               
                                                )

from api.models.crud.users import users_actions
from api.models.schemas.user import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
def resolve_all_users():
    qs, status = read_all_users()
    return {'data':qs}, status

@users_bp.route('/register', methods=['POST'])
def resolve_create_user():

    body = request.json
    if 'username' in body:
        obj, status = create_user(username = body['username'])
    else:
        obj, status = 'body not found', 500

    return {'data':obj} , status

@users_bp.route('/user/', methods=['GET'])
@jwt_required()
def resolve_by_id_users():
    id = request.args['id']
    qs, status = get_by_id(id)
    return {'data':qs}, status

@users_bp.route('/learn/', methods=['GET'])
@jwt_required()
def resolve_words_user_to_learn():
    id = request.args['id']
    
    qs = read_words_to_learn_user(id)
    return {"data":qs}

