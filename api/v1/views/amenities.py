#!/usr/bin/python3
'''Amenity file'''
from api.v1.views import app_views
from flask import jsonify, request
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', strict_slashes=False)
def all_amenities():
    all_data = storage.all(Amenity)
    new_list = []
    for amenity in all_data.values():
        new_list.append(amenity.to_dict())
    return jsonify(new_list)


@app_views.route('/amenities/<string:amenity_id>', strict_slashes=False)
def one_amenity(amenity_id):
    the_amenity = storage.get(Amenity, amenity_id)
    if the_amenity is None:
        return jsonify({'error': 'Not found'}), 404
    the_amenity = the_amenity.to_dict()
    return jsonify(the_amenity)


@app_views.route('/amenities/<string:amenity_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    the_amenity = storage.get(Amenity, amenity_id)
    if the_amenity is None:
        return jsonify({'error': 'Not found'}), 404
    storage.delete(the_amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities',
                 methods=['POST'],
                 strict_slashes=False)
def create_amenity():
    new_amenity = request.get_json()
    if new_amenity is None:
        return jsonify({'error': 'Not a JSON'}), 400
    if 'name' not in new_amenity:
        return jsonify({'error': 'Missing name'}), 400
    amenity = Amenity(**new_amenity)
    amenity.save()
    storage.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<string:amenity_id>',
                 methods=['PUT'],
                 strict_slashes=False)
def edit_amenity(amenity_id):
    new_amenity = request.get_json()
    the_amenity = storage.get(Amenity, amenity_id)
    if new_amenity is None:
        return jsonify({'error': 'Not a JSON'}), 400
    if the_amenity is None:
        return jsonify({'error': 'Not found'}), 404
    for key, value in new_amenity.items():
        setattr(the_amenity, key, value)
    the_amenity.save()
    return jsonify(the_amenity.to_dict()), 200


if __name__ == '__main__':
    pass
