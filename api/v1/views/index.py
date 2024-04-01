#!/usr/bin/python3
'''index file'''
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


@app_views.route('/status', strict_slashes=False)
def status():
    '''return stuff'''
    return jsonify(status='OK')


@app_views.route('/stats', strict_slashes=False)
def stats():
    '''return stats'''
    classes = {'states': State, 'users': User,
               'amenities': Amenity, 'cities': City,
               'places': Place, 'reviews': Review}
    new_dict = {}
    for key, value in classes.items():
        new_dict[key] = storage.count(value)
    return jsonify(new_dict)
