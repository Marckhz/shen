from flask import Blueprint, jsonify, request


from api.models.schemas.language import Words
from api.models.crud.words.word_actions import read_all_words, create_word, read_words_by_language

words_bp = Blueprint('words', __name__)

@words_bp.route('/', methods=['GET'])
def resolve_all_words():
    
    objs = read_all_words()

    return {"data":objs}


@words_bp.route('/add_word/', methods=['POST'])
def resolve_create_word():

    body = request.json

    if body is not None:
        word = body['word']
        language = body['language_id']
        obj, status = create_word(word=word, language_id = language)
    return {"data":obj}, status

@words_bp.route('/words_by_language/', methods=['GET'])
def resolve_word_by_language():

    lang = request.args['language']
    objs = read_words_by_language(lang)
    return {"data":objs}, 200