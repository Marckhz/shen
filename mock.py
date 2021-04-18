
import csv
import os
from random import randint

from flask_script import Command
from api.extensions import db
from api.models.schemas.user import User
from api.models.schemas.language import Language, LearnedWords, Words


class LoadData(Command):

    def run(self):
        path  = 'data/'
        files_ = os.listdir('data/')
        #with app.app_context():
        print("starting loading data")
        objects = {'users':[], 'language':[], 'words':[], 'learned':[]}
        for file in ['user_mock.csv', 'lang_mock.csv', 'words_mock.csv', 'words_learned_mock.csv']:
            with open(path+file, 'r',  encoding="utf8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if file == 'user_mock.csv':
                        objects['users'] += [ User(username = row['username']) ]
                    if file == 'lang_mock.csv':
                        objects['language'] += [ Language(language=row['language'], user_id = row['user_id']) ] 
                    if file == 'words_mock.csv':
                        objects['words'] += [ Words(word = row['word'], language_id = row['language_id']) ]
                    if file == 'words_learned_mock.csv':
                        practiced = 0
                        learned = True if row['learned'] == 'true' else False
                        if learned:
                            practiced = randint(0,100)
                        objects['learned'] += [ LearnedWords( learned = learned, 
                                                word_id = row['word_id'],
                                                user_id = row['user_id'], 
                                                practiced=practiced
                                                )
                                    ]
        for k,v  in objects.items():
            print(f"inserting {k}")
            db.session.bulk_save_objects(v)
            db.session.commit()
            


if __name__ == "__main__":
    path  = 'data/'
    files_ = os.listdir('data/')
    with app.app_context():
        print("starting loading data")
        objects = []
        for file in files_:
            with open(path+file, 'r',  encoding="utf8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if file == 'user_mock.csv':
                        objects += [ User(username = row['username']) ]
                    if file == 'lang_mock.csv':
                        objects += [ Language(language=row['language'], user_id = row['user_id']) ] 
                    if file == 'words_mock.csv':
                        objects += [ Words(word = row['word'], language_id = row['language_id']) ]
                    if file == 'words_learned_mock.csv':
                        practiced = 0
                        if row['learned'] == True:
                            practiced = randint(0,100)
                        objects += [ LearnedWords(learned = row['learned'], 
                                                word_id = row['word_id'],
                                                user_id = row['user_id'], 
                                                practiced=practiced
                                                )
                                    ]
        db.bulk_save_objects(objects)

    print("end")

        #for obj in objects:
        #    print(obj)
