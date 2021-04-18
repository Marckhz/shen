from api.extensions import db
from sqlalchemy.orm import validates
from sqlalchemy import event


def signal_validate_lang_user_exists(mapper, connect, target):
    target.signal_validate_lang_user_exists()

def signal_validate_word_lang_exists(mapper, connect, target):
    target.signal_validate_word_lang_exists()



def signal_validate_word_user_exists(mapper, connect, target):
    target.signal_validate_word_user_exists()

class Language(db.Model):

    __tablename__ = "language"

    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp() )

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),  nullable=False)

    words = db.relationship('Words', backref='language', lazy=True)

    def signal_validate_lang_user_exists(self):
        obj = db.session.query(Language).filter(Language.language == self.language, Language.user_id == self.user_id).first()
        if obj is not None:
            raise AssertionError("this thing already exists")
        
   

class Words(db.Model):

    __tablename__= "words"

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp() )

    language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable=False )

    def signal_validate_word_lang_exists(self):
        obj = db.session.query(Words).filter(Words.word == self.word, Words.language_id == self.language_id).first()
        if obj is not None:
            raise AssertionError("this thing already exists")

 
class LearnedWords(db.Model):

    __tablename__ = "learned_words"

    id = db.Column(db.Integer, primary_key=True)
    learned = db.Column(db.Boolean, nullable=False)
    practiced = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default = db.func.current_timestamp() )
    
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    def signal_validate_word_user_exists(self):
        obj = db.session.query(LearnedWords).filter(LearnedWords.user_id == self.user_id, LearnedWords.word_id == self.word_id).first()
        if obj is not None:
            raise AssertionError("cannot duplicate")
        self.practiced = 1
        self.learned = True
        

event.listen(Language, 'before_insert', signal_validate_lang_user_exists)
event.listen(Words, 'before_insert', signal_validate_word_lang_exists)
event.listen(LearnedWords, 'before_insert', signal_validate_word_user_exists)
    





