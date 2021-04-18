from api.extensions import db

from api.models.schemas.language import LearnedWords

def add_learned_word(**kwargs):

    obj = LearnedWords(
                user_id = kwargs['user_id'],
                word_id = kwargs['word_id']
                )
    try:
        db.session.add(obj)
        db.session.commit()
        return obj.id, 201

    except AssertionError as error_message:
        return str(error_message), 400


def practice_word(id):
    obj = db.session.query(LearnedWords).get(id)
    if obj is not None:
        obj.practiced+=1
        db.session.commit()
        return {
            "id":obj.id,
            "practiced":obj.practiced,
            "user_id":obj.user_id
        }
    else:
        return 