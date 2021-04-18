from api.extensions import db
from sqlalchemy.orm import validates
from flask import jsonify

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp() )

    languages = db.relationship('Language', backref='users', lazy=True)
    learned_words = db.relationship('LearnedWords', backref='users', lazy=True)


    @validates('username')
    def validate_username(self, key, username):
        user = db.session.query(User).filter(User.username==username).first()
        if user is not None:
            raise AssertionError(f'{username} already exists  in db')
        else:
            return username 

