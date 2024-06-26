#!/usr/bin/python3
'''application file'''
import os
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_app(self):
    '''Status of your API'''
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    '''404 error'''
    return jsonify({'error': 'Not found'}), 404


if __name__ == "__main__":

    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')))
