from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..models import db, episode, Appearance

episode_bp = Blueprint('episodes', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = episode.query.all()
    return jsonify([{
        'id': e.id,
        'date': e.date.isoformat(),
        'number': e.number
    } for e in episodes]), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = episode.query.get_or_404(id)
    appearances = [{
        'id': a.id,
        'rating': a.rating,
        'guest': {
            'id': a.guest.id,
            'name': a.guest.name,
            'occupation': a.guest.occupation
        }
    } for a in episode.appearances]
    
    return jsonify({
        'id': episode.id,
        'date': episode.date.isoformat(),
        'number': episode.number,
        'appearances': appearances
    }), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'episode deleted successfully'}), 200