from api.models.schemas.language import Words, Language

from api.extensions import db



def read_all_words():
    qs = db.session.query(Words).all()
    objs = []
    for o in qs:
        objs.append({
            "word":o.word,
            "language":o.language_id
        })
    return objs

    
def create_word(**kwargs):
    obj = Words(word = kwargs['word'].lower(), language_id = kwargs['language_id'])
    try:
        db.session.add(obj)
        db.session.commit()
        return obj.id, 201
    except AssertionError as message_error:
        return message_error, 400



def read_words_by_language(language):
    qs = db.session.query(Language).filter(Language.language == language.lower() ).all()

    words = [w.word  for o  in qs  for w in o.words ]

    objs = {
        "language":language,
        "words":words
    }
    return objs




    
