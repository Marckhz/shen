from flask import Blueprint, request
from api.models.crud.users.users_actions import get_by_username

from flask_jwt_extended import create_access_token


auth = Blueprint('auth', __name__)


@auth.route('/token/')
def request_token():
    access_token = None
    body = request.json
    if body is not None:
        user = get_by_username( body['username']  )
        if user is not None:
            access_token = create_access_token(identity=user)
    return {'token':access_token}

