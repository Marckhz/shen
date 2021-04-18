from api.extensions import db 
from api.models.schemas.user import User
from api.models.schemas.language import Words, LearnedWords, Language
def create_user(username):
    
    obj = User(username=username)
    status = None
    try:
        db.session.add(obj)
        db.session.commit()
        obj, status = obj.id, 201

    except AssertionError as error_message:
        obj, status = error_message, 500
    return obj, status

def read_all_users():
    qs = db.session.query(User).all()
    objs = []
    for u in qs:
        objs.append({
            "username":u.username,
            "id":u.id,
            "created_at":u.created_at
        })
    return objs, 200

def read_words_to_learn_user(id):
   
    user  = db.session.query(User).get(id)
    learned_ids = [ o.word_id for o in user.learned_words ]
   
    qs = db.session.query(Words).filter(Words.id.notin_(learned_ids), Words.language_id == Language.id ).all()   
    
    words = [ {"word":o.word, "id":o.id, "language":o.language.language } for o in qs ]

    return words

def get_by_id(id):
    qs = db.session.query(User).get(id)
    if qs:
        return {'username':qs.username, 'id':qs.id}, 200
    else:
        return None, 404

def get_by_username(username):
    qs = db.session.query(User).filter(User.username == username.lower() )
    if qs is not None:
        return True
