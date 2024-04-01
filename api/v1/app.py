#!/usr/bin/python3
'''application file'''
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_app(self):
    '''Status of your API'''
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    '''404 error'''
    return jsonify({'error': 'Not found'}), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True)
