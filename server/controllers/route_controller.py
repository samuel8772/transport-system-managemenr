from flask import Blueprint, request, jsonify
from server.models.route import Route
from server.extensions import db

route_bp = Blueprint('routes', __name__, url_prefix='/api/routes')

@route_bp.route('/', methods=['GET'])
def get_routes():
    routes = Route.query.all()
    return jsonify([route.to_dict() for route in routes]), 200

@route_bp.route('/', methods=['POST'])
def create_route():
    data = request.get_json()
    required = ['name', 'origin', 'destination', 'distance', 'base_fare', 'duration']
    if not all(k in data for k in required):
        return jsonify({'error': 'Missing fields'}), 400
    if data['distance'] <= 0 or data['base_fare'] <= 0:
        return jsonify({'error': 'Distance and base fare must be positive'}), 400
    route = Route(
        name=data['name'], origin=data['origin'], destination=data['destination'],
        distance=data['distance'], base_fare=data['base_fare'], duration=data['duration']
    )
    db.session.add(route)
    db.session.commit()
    return jsonify(route.to_dict()), 201
