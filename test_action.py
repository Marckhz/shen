import unittest
import json

from flask_script import Command

from config import config
from api import create_app
from api.extensions import db

class Base(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config['test'])
        self.client = self.app.test_client

        self.headers = {
            'Content-Type':'application/json',
            'Authorization': None
        }
        self.username = 'marck'
        self.serialized_user = json.dumps({'username':'marck'})

        with self.app.app_context():
            db.create_all()
    
    def test_add_user(self):
        data = json.dumps({'username':'marck'})
        res = self.client().post('/users/register', data=data, headers=self.headers)
        res_json = json.loads(res.data)
       
        self.assertEqual(res.status_code, 201)
        self.assertEqual(int(), res_json['data'])


    def test_request_token(self):
        res = self.client().get('/auth/token/', data=self.serialized_user, headers=self.headers )
        res_json = json.loads(res.data)        
        
        self.assertIsNotNone(res_json['token'])
        return res_json


    def test_get_user_list(self):
        """Test retrieve all users"""
        res = self.client().get('/users/')
        res_json = json.loads(res.data)
        if res_json:
            for r in res_json['data']:
                self.assertListEqual(['created_at', 'id','username'], list(r.keys() ))
        else:
            self.assertEqual([], res_json['data'])



    def test_get_user_by_id(self):
    
        """Test get user by id """

        token = self.test_request_token()

        self.headers['Authorization'] = 'Bearer '+  token['token']

        res = self.client().get('/users/user/', query_string={'id':1}, headers=self.headers)
        res_json = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(self.username,res_json['data']['username'])
        self.assertEqual(1, res_json['data']['id'])


    def test_get_words(self):
        """Test get all words"""
        
        res = self.client().get('/words/',  headers=self.headers)
        res_json = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        if res_json:
            for r in res_json['data']:
                self.assertListEqual(['language', 'word'], list(r.keys() ) )
        else:
            self.assertEqual([], res_json['data'])

    def test_word_by_language(self):

        """Test word given a language """
        res = self.client().get('/words/words_by_language/', query_string={'language':'english'})

        res_json = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertNotEqual([], res_json['data'])

    def test_practice_word(self):

        """Test add practiced times """
        
        self.headers['Authorization'] = 'Bearer '+ self.test_request_token()['token']

        res = self.client().post('/learn/practice/', query_string={'id':1}, headers=self.headers)
        res_json = json.loads( res.data )

        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(res_json)

    def test_add_learned_word(self):

        body = json.dumps( {'user_id':1, 'word_id':1} )
        self.headers['Authorization'] = 'Bearer ' + self.test_request_token()['token']
        
        res = self.client().post("/learn/add/", data=body, headers=self.headers)
        res_json = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual({'id':1}, res_json)

    def test_add_word(self):

        self.headers['Authorization'] = 'Bearer ' + self.test_request_token()['token']
        
        body = json.dumps({'word':'Hello', 'language_id':'1'})

        res = self.client().post("/words/add_word/", data=body, headers=self.headers)

        res_json = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(1, res_json['data'])



        
    def test_all_languages(self):
        """Test get all languages """

        res = self.client().get('/languages/', headers=self.headers)
        res_json = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        if res_json is not None:
            for r in res_json['data']:
                self.assertListEqual(['created_at', 'language', 'user_id'], list( r.keys() ) )
        else:
            self.assertEqual([], res_json['data'])




    def test_add_language(self):
        """Test add language with user_id"""
        self.headers['Authorization'] = 'Bearer '+ self.test_request_token()['token']
        
        body = json.dumps({"language":"english", "user_id":"1"})

        res = self.client().post('/languages/add_language', data=body, headers=self.headers)

        res_json  = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(1, res_json['data'] )

    def test_get_language_by_id(self):
        self.headers['Authorization'] = 'Bearer '+ self.test_request_token()['token']

        res = self.client().get('/languages/language/user_languages', query_string={'id':1}, headers=self.headers)
        res_json = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual({'language':'english','user_id':1}, res_json['data'][0])



if __name__ == "__main__":
    unittest.main()