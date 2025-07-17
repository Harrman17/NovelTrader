from flask import Blueprint, request, jsonify
from services.grab_mot import get_mot_data

mot_blueprint = Blueprint('mot', __name__)

@mot_blueprint.route('/mot', methods=['POST'])
def fetch_mot():
    data = request.get_json()
    registration = data.get('registration')
    try:
        mot_data = get_mot_data(registration)
        return jsonify(mot_data)
    except Exception as e:
        return jsonify({ 'error': 'Failed to fetch MOT data', 'details': str(e) }), 500
