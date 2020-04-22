from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest

from auth.decorators import require_authentication
from db import Profile, Friends
from .services import create_request, get_friends_by_username
from .serializers import FriendsSerializer


friends_bp = Blueprint('friends', __name__, url_prefix='/friends')

@friends_bp.route('/', methods=['POST'])
@require_authentication
def send(profile):
    validated_data: dict = FriendsSerializer.deserialize(request.json)
    requester_name = validated_data['requester']
    requestee_name = validated_data['requestee']
    status = validated_data['status']
    friend_req = create_request(requester_name, requestee_name, status)
    if friend_req is None:
        raise BadRequest('Could not create request')
    return jsonify(FriendsSerializer.serialize(friend_req))

@friends_bp.route('/<username>', methods=['GET'])
def get_by_username(username):
    friends = get_friends_by_username(username)
    return jsonify(FriendsSerializer.serialize(friends))
