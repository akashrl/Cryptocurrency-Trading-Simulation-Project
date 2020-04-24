from datetime import datetime, timedelta
from http import HTTPStatus
from unittest.mock import Mock, patch, MagicMock
import json
import pytz
from functools import wraps

from db import db, AuthToken, Profile, Coin, Game, GameProfile, GameCoin, Ticker, GameProfileCoin, Message
from tests.utils import DbTest, AuthDbTest


def mock_require_authentication():
    print('inside mock')

    def side_effect(route_func):
        print('inside side_effect')

        @wraps(route_func)
        def wrapper(*args, **kwargs):
            print('calling mocked')
            return route_func('todo standin profile', *args, **kwargs)
        return wrapper
    return MagicMock(side_effect=side_effect)


class AdminTest(AuthDbTest):

    def setUp(self):
        super().setUp()
        with db.atomic() as txn:
            self.admin = Profile.create(username='admin1', hashed_password='password', is_admin=True)
            self.token = AuthToken.create(profile=self.admin, token='thevalidtoken').token

    # @patch('game.routes.require_authentication', mock_require_authentication())
    def test_ban_player(self):
        profile = Profile.create(username='username', hashed_password='password')
        res = self.client.delete('/users/{}'.format(profile.id),
                                 headers={
                                     'Authorization': 'Bearer ' + self.token,
                                 },
                                 content_type='application/json',
                                 )
        self.assertEqual(int(HTTPStatus.OK), res._status_code)

        updated = Profile.get_or_none(Profile.id == profile.id)
        self.assertIsNotNone(updated)
        self.assertEqual(updated.is_banned, True)


