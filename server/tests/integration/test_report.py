from datetime import datetime, timedelta
from http import HTTPStatus
from unittest.mock import Mock, patch, MagicMock
import json
import pytz
from functools import wraps

from db import db, AuthToken, Profile, Coin, Game, GameProfile, GameCoin, Ticker, GameProfileCoin, Message, Report
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


class ReportTest(AuthDbTest):

    def setUp(self):
        super().setUp()
        with db.atomic() as txn:
            self.game = Game.create(
                name='Game',
                starting_cash=10000.00,
                shareable_link='aaaabbbbccccdddd',
                shareable_code='aaaa',
                ends_at=(datetime.utcnow().replace(tzinfo=pytz.utc) + timedelta(days=7)).isoformat()
            )
            self.profile = Profile.create(username='username', hashed_password='password')
            self.profile2 = Profile.create(username='username2', hashed_password='password2')
            GameProfile.create(game=self.game, profile=profile, cash=-1.0)
            self.message = Message.create(
                game=self.game.id,
                profile=self.profile2.id,
                content="first message",
            )
            self.token = AuthToken.create(profile=self.profile, token='thevalidtoken').token

    # @patch('game.routes.require_authentication', mock_require_authentication())
    def test_create_report_success(self):
        res = self.client.post('/reports',
                               data=json.dumps({
                                   'messageID': self.message.id
                               }),
                               headers={
                                   'Authorization': 'Bearer ' + self.token,
                               },
                               content_type='application/json',
                               )
        self.assertEqual(int(HTTPStatus.OK), res._status_code)
        report = Report.get_or_none(Report.message == self.message.id)
        assert report is not None

    # @patch('game.routes.require_authentication', mock_require_authentication())
    def test_get_reports_success(self):
        Report.create(
            game=self.game.id,
            issuer=self.profile.id,
            offender=self.profile2.id,
            message=self.message.id,
        )
        res = self.client.get('/reports/?sortByStatusDescending=true&numPerPage=9&page=1',
                              headers={
                                  'Authorization': 'Bearer ' + self.token,
                              },
                              content_type='application/json',
                              )

        self.assertEqual(int(HTTPStatus.OK), res._status_code)
        self.assertNotEqual(0, len(res.json['reports']))

    # @patch('game.routes.require_authentication', mock_require_authentication())
    def test_update_reports_success(self):
        report = Report.create(
            game=self.game.id,
            issuer=self.profile.id,
            offender=self.profile2.id,
            message=self.message.id,
        )
        res = self.client.put('/reports/{}'.format(report.id),
                              data=json.dumps({
                                'userAction': "warning"
                              }),
                              headers={
                                  'Authorization': 'Bearer ' + self.token,
                              },
                              content_type='application/json',
                              )

        self.assertEqual(int(HTTPStatus.OK), res._status_code)
        updated = Report.get_or_none(Report.id == report.id)
        self.assertIsNotNone(updated)
        self.assertIsNotNone(updated.takenAction)

