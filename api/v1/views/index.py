#!/usr/bin/python3
'''index file'''
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    '''return stuff'''
    test = {"status": "OK"}
    test = jsonify(test)
    return test
