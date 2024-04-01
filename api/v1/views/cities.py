#!/usr/bin/python3
'''City file'''
from api.v1.views import app_views
from flask import jsonify, request
from models import storage
from models.city import City
from models.state import State


@app_views.route('/states/<string:state_id>/cities', strict_slashes=False)
def all_cities(state_id):
    the_state = storage.get(State, state_id)
    if the_state is None:
        return jsonify({'error': 'Not found'}), 404
    all_data = storage.all(City)
    new_list = []
    for city in all_data.values():
        if city.state_id == state_id:
            new_list.append(city.to_dict())
    return jsonify(new_list)

@app_views.route('/cities/<string:city_id>', strict_slashes=False)
def one_city(city_id):
    the_city = storage.get(City, city_id)
    if the_city is None:
        return jsonify({'error': 'Not found'}), 404
    the_city = the_city.to_dict()
    return jsonify(the_city)

@app_views.route('/cities/<string:city_id>',
                    methods=['DELETE'],
                    strict_slashes=False)
def delete_city(city_id):
    the_city = storage.get(City, city_id)
    if the_city is None:
        return jsonify({'error': 'Not found'}), 404
    storage.delete(the_city)
    storage.save()
    return jsonify({}), 200

@app_views.route('/states/<string:state_id>/cities',
                    methods=['POST'],
                    strict_slashes=False)
def create_city(state_id):
    the_state = storage.get(State, state_id)
    if the_state is None:
        return jsonify({'error': 'Not found'}), 404
    new_city = request.get_json()
    if new_city is None:
        return jsonify({'error': 'Not a JSON'}), 400
    if 'name' not in new_city:
        return jsonify({'error': 'Missing name'}), 400
    new_city['state_id'] = state_id
    city = City(**new_city)
    city.save()
    storage.save()
    return jsonify(city.to_dict()), 201

@app_views.route('/cities/<string:city_id>',
                    methods=['PUT'],
                    strict_slashes=False)
def edit_city(city_id):
    new_city = request.get_json()
    the_city = storage.get(City, city_id)
    if new_city is None:
        return jsonify({'error': 'Not a JSON'}), 400
    if the_city is None:
        return jsonify({'error': 'Not found'}), 404
    for key, value in new_city.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(the_city, key, value)
    the_city.save()
    return jsonify(the_city.to_dict()), 200

if __name__ == '__main__':
    pass
