from flask import Blueprint, request, jsonify
from api.models.crud.learnwords.learn_words_actions import add_learned_word, practice_word

from flask_jwt_extended import jwt_required


learn_words = Blueprint('learn_words', __name__)

@learn_words.route('/add/', methods=['POST'])
@jwt_required()
def add_learn_word():
    body = request.json
    if body is not None:
        word_id = body['word_id']
        user_id = body['user_id']

    obj, status = add_learned_word(word_id = word_id, user_id=user_id)

    return {"data":obj}, status

@learn_words.route('/practice/', methods=['POST'])
@jwt_required()
def update_practiced_word():

    word = request.args['id']
    qs = practice_word(word) 
    
    return {"data":qs}