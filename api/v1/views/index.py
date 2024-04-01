#!/usr/bin/python3
'''index file'''
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    '''return stuff'''
    return jsonify(status='OK')


@app_views.route('/stats', strict_slashes=False)
def stats():
    '''return stats'''
    classes = {"Amenity": "amenities",
               "City": "cities",
               "Place": "places",
               "Review": "reviews",
               "State": "states",
               "User": "users"}
    new_dict = {}
    for key, value in classes.items():
        new_dict[value] = storage.count(key)
    return jsonify(new_dict)
