from api.extensions import db
from operator import attrgetter
from flask import jsonify


def get_by_pk(Model, pk):

    obj = db.session.query(Model).get(pk)
    return obj

def update(Model, pk):
    pass


