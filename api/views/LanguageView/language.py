from flask import Blueprint, request, jsonify
import json

from api.models.crud.languages.language_actions import (
                                                        read_all_langauge, 
                                                        create_language, 
                                                        read_user_lang_rel
                                                    )
from api.models.crud.crud import get_by_pk
from api.models.schemas.language import Language
from flask_jwt_extended import jwt_required

language_bp = Blueprint('language', __name__)

@language_bp.route('/', methods=['GET'])
def resolve_all_language():

    lang,status = read_all_langauge()
    return {'data': lang}, status


@language_bp.route('/add_language', methods=['POST'])
@jwt_required()
def resolve_create_language():
    
    body = request.json

    if body is not None:
        obj, status = create_language(language = body['language'], user_id = body['user_id'])
    else:
        obj, status = 'None', 400   
    return json.dumps({'data':obj}) , status

@language_bp.route('/language/', methods=['GET'])
def resolve_get_language():

    id = request.args['id']
    
    obj = get_by_pk(Language, pk=id)
    
    obj_dict = {"language":obj.language, "user_id":obj.user_id }

    return { 'data':obj_dict }

@language_bp.route('/language/user_languages', methods=['GET'])
@jwt_required()
def resolve_get_user_language_rel():
    id = request.args['id']
    obj_dict = read_user_lang_rel(id)
    return {"data":obj_dict}

