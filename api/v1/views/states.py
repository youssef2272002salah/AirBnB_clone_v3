#!/usr/bin/python3
'''State file'''
from api.v1.views import app_views
from flask import jsonify, request
from models import storage
from models.state import State


@app_views.route('/states', strict_slashes=False)
def all_states():
    all_data = storage.all(State)
    new_list = []
    for state in all_data.values():
        new_list.append(state.to_dict())
    return jsonify(new_list)


@app_views.route('/states/<state_id>', strict_slashes=False)
def one_state(state_id):
    the_state = storage.get(State, state_id)
    if the_state is None:
        return jsonify({'error': 'Not found'}), 404
    the_state = the_state.to_dict()
    return jsonify(the_state)


@app_views.route('/states/<state_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    the_state = storage.get(State, state_id)
    if the_state is None:
        return jsonify({'error': 'Not found'}), 404
    storage.delete(the_state)
    storage.save()
    return {}, 200


@app_views.route('/states', methods={'POST'}, strict_slashes=False)
def create_state():
    new_state = request.get_json()
    if new_state is None:
        return jsonify({'error': 'Not a JSON'}), 400
    if 'name' not in new_state:
        return jsonify({'error': 'Missing name'}), 400
    state = State(**new_state)
    state.save()
    storage.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods={'PUT'}, strict_slashes=False)
def edit_state(state_id):
    new_state = request.get_json()
    the_state = storage.get(State, state_id)
    if new_state is None:
        return jsonify({'error': 'Not a JSON'}), 400
    if the_state is None:
        return jsonify({'error': 'Not found'}), 404
    for key, value in new_state.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(the_state, key, value)
    storage.save()
    return jsonify(the_state.to_dict()), 200


if __name__ == '__main__':
    pass
