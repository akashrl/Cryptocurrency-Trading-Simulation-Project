from db import db, Notification, Profile, Friends
from werkzeug.exceptions import BadRequest

from notifications.services import send_notification

@db.atomic()
def create_request(requester_name, requestee_name, status):
    requester_profile = Profile.get_or_none(Profile.username == requester_name)
    requestee_profile = Profile.get_or_none(Profile.username == requestee_name)
    if requester_profile is None:
        raise BadRequest('Could not find requester')
    if requestee_profile is None:
        send_notification(requester_profile, f'User {requestee_name} does not exist.')
        raise BadRequest('Could not find requestee')
    if requester_profile == requestee_profile:
        send_notification(requester_profile, f'Cannot friend yourself!')
        raise BadRequest('Cannot friend self')
    check_duplicates = Friends.get_or_none((Friends.requester == requester_profile) & (Friends.requestee == requestee_profile))
    if check_duplicates is not None:
        send_notification(requester_profile, f'Friend request to {requestee_profile.username} has already been created')
        raise BadRequest('Friend request has already been made')
    req = Friends.create(
        requester=requester_profile,
        requestee=requestee_profile,
        status=status)
    send_notification(requester_profile, f'Friend request to {requestee_profile.username} has been sent!')
    send_notification(requestee_profile, f'{requester_profile.username} has sent you a friend request!')
    return req

@db.atomic()
def accept_request(requester_name, requestee_name):
    requester_profile = Profile.get_or_none(Profile.username == requester_name)
    requestee_profile = Profile.get_or_none(Profile.username == requestee_name)
    if requester_profile is None:
        raise BadRequest('Could not find requester')
    if requestee_profile is None:
        raise BadRequest('Could not find requestee')
    req = Friends.get_or_none((Friends.requester == requester_profile) & (Friends.requestee == requestee_profile))
    req.status = 1
    other_way_friendship = Friends.create(
        requester=requestee_profile,
        requestee=requester_profile,
        status=1)
    send_notification(requester_profile, f'{requestee_profile.username} has accepted your friend request!')
    return req

@db.atomic()
def get_friends_by_username(username):
    get_friends = Friends.select().where((Friends.requester == username or Friends.requestee == username) and Friends.status == 1)
    if get_friends.count() == 0:
        raise BadRequest("This user has no friends.")
    return get_friends
