from flask import Flask
from .extensions import db, jwt

from .views.UserView.user import users_bp
from .views.LanguageView.language import language_bp
from .views.WordsView.word import words_bp
from .views.WordsLearnView.words_learn import learn_words
from .views.Auth.auth import auth

def create_app(config):
    
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(language_bp, url_prefix='/languages')
    app.register_blueprint(words_bp, url_prefix='/words')
    app.register_blueprint(learn_words, url_prefix='/learn')
    app.register_blueprint(auth, url_prefix='/auth')


    from .models.schemas import user, language

    with app.app_context():

        jwt.init_app(app)
        db.init_app(app)
        db.create_all()

    return app

