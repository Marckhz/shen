from api.models.schemas.language import Language
from api.extensions import db

def read_all_langauge():

    objs = []
    qs = db.session.query(Language).all()
    for lang in qs:
        objs.append({
            "language":lang.language,
            "user_id":lang.user_id,
            "created_at":lang.created_at
        })

    return objs, 200

def create_language(*args, **kwargs):
    
    obj = Language(language=kwargs['language'].lower()  ,
                    user_id=kwargs['user_id'])

    try:
        db.session.add(obj)
        db.session.commit()
        return obj.id, 201
    except AssertionError as error_message:
        return str(error_message), 400



def read_user_lang_rel(user_id):
    qs = db.session.query(Language).filter(Language.user_id == user_id)

    objs = []
    for o in qs:
        objs.append({
            "language":o.language,
            "user_id":o.user_id
        })

    return objs