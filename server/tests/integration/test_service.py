from datetime import datetime
from decimal import Decimal
from functools import wraps
import json
import os
from unittest.mock import patch, Mock, MagicMock

from db import Ticker, Coin, PriceAlert, Profile, Notification, Game, GameProfile
from scripts.service import ping, check_global_timed_game
from tests.utils import DbTest


class TestService(DbTest):
    @patch('requests.get', MagicMock(return_value=Mock(json=lambda: [
        {'symbol': 'BTC', 'price': '56.12345678', '1d': {'price_change_pct': '-2.33334567'}},
    ])))
    def test_parsing_with_one_coin(self):
        ping('BTC')
        btc = Coin.get(Coin.symbol == 'BTC')
        btc_ticker = Ticker.get(Ticker.coin == btc)
        self.assertEqual(btc_ticker.price, Decimal('56.12345678'))
        self.assertEqual(btc_ticker.price_change_day_pct, Decimal('-2.33334567'))

    @patch('requests.get', MagicMock(return_value=Mock(json=lambda: [
        {'symbol': 'BTC', 'price': '56.12345678', '1d': {'price_change_pct': '-2.33334567'}},
    ])))
    def test_parsing_with_many_ping_calls(self):
        ping('BTC')
        btc = Coin.get(Coin.symbol == 'BTC')
        btc_ticker = Ticker.get(Ticker.coin == btc)
        self.assertEqual(btc_ticker.price, Decimal('56.12345678'))
        self.assertEqual(btc_ticker.price_change_day_pct, Decimal('-2.33334567'))
        Ticker.delete().execute()
        ping('BTC')
        btc = Coin.get(Coin.symbol == 'BTC')
        btc_ticker = Ticker.get(Ticker.coin == btc)
        self.assertEqual(btc_ticker.price, Decimal('56.12345678'))
        self.assertEqual(btc_ticker.price_change_day_pct, Decimal('-2.33334567'))

    @patch('requests.get', MagicMock(return_value=Mock(json=lambda: [
    ])))
    def test_parsing_with_no_coins(self):
        num_tickers_before = Ticker.select().count()
        ping()
        num_tickers_after = Ticker.select().count()
        self.assertEqual(num_tickers_before, num_tickers_after)

    @patch('requests.get', MagicMock(return_value=Mock(json=lambda: [
        {'symbol': 'BTC', 'price': '56.12345678', '1d': {'price_change_pct': '-1.23456789'}},
        {'symbol': 'ETH', 'price': '42.98765432', '1d': {'price_change_pct': '-8.98765432'}},
    ])))
    def test_parsing_with_many_coins(self):
        ping('BTC', 'ETH')
        btc = Coin.get(Coin.symbol == 'BTC')
        eth = Coin.get(Coin.symbol == 'ETH')
        btc_ticker = Ticker.get(Ticker.coin == btc)
        eth_ticker = Ticker.get(Ticker.coin == eth)
        self.assertEqual(btc_ticker.price, Decimal('56.12345678'))
        self.assertEqual(btc_ticker.price_change_day_pct, Decimal('-1.23456789'))
        self.assertEqual(eth_ticker.price, Decimal('42.98765432'))
        self.assertEqual(eth_ticker.price_change_day_pct, Decimal('-8.98765432'))

    @patch('requests.get', MagicMock(return_value=Mock(json=lambda: [
        # NOTE these must be actual coins defined in the migrations!
        {'symbol': 'FOO', 'price': '56.12345678', '1d': {'price_change_pct': '-2.33334567'}},
    ])))
    def test_price_alerts(self):
        os.environ['NOMICS_BASE_URL'] = 'foo'
        profile = Profile.create(username='theusername', hashed_password='thehashedpassword')
        coin = Coin.create(name='foocoin', symbol='FOO')
        alert = PriceAlert.create(
            profile=profile,
            above=True,
            coin=coin,
            strike_price=Decimal(0.1),
        )
        alert = PriceAlert.create(
            profile=profile,
            above=False,
            coin=coin,
            strike_price=Decimal(0.1),
        )
        ping('FOO')
        self.assertEqual(1, Notification.select().count())
        # ok, the line below throws an exception which causes all other tests to fail
        # as tearDown is not called and because db is in inconsistent state
        notif = Notification.get(Notification.profile == profile)

    @patch('requests.get', MagicMock(return_value=Mock(json=lambda: [
        {'symbol': 'DASH', 'price': '56.12345678', '1d': {'price_change_pct': '-1.23456789'}},
    ])))
    def test_parsing_with_four_character_symbol(self):
        coin = Coin.create(name='foocoin', symbol='DASH')
        ping('DASH')
        dash = Coin.get(Coin.symbol == 'DASH')
        ticker = Ticker.get(Ticker.coin == dash)
        self.assertEqual(ticker.price, Decimal('56.12345678'))
        self.assertEqual(ticker.price_change_day_pct, Decimal('-1.23456789'))

    @patch('requests.get', MagicMock(return_value=Mock(json=lambda: [
        {'symbol': 'FOO', 'price': '56.12345678', '1d': {'price_change_pct': '-1.23456789'}},
    ])))
    def test_raises_error_if_token_not_exists(self):
        with self.assertRaises(Exception):
            ping('FOO')

    def test_check_global_timed_game_creates_new_game_upon_expiration(self):
        game_before_check = Game.get(Game.name == 'Global Timed')
        game_before_check.ends_at = datetime.utcnow()
        game_before_check.save()
        check_global_timed_game()
        self.assertEqual(0, Game.select().where(Game.id == game_before_check.id).count())
        Game.get(Game.name == 'Global Timed')
    
    def test_user_automatically_joins_new_global_time_game(self):
        # register user
        res = self.client.post('/auth/register', data=json.dumps({
            'username': 'randomusername',
            'password': 'randompassword',
            'password': 'randompassword',
        }), headers={
            'Content-Type': 'application/json'
        })
        self.assertEqual(200, res._status_code)
        game_before_check = Game.get(Game.name == 'Global Timed')
        game_before_check.ends_at = datetime.utcnow()
        game_before_check.save()
        # assert deletes old GameProfile
        profile = Profile.get_by_id(1)
        qry = GameProfile.select().join(Game).where((GameProfile.profile == profile) & (Game.name == 'Global Timed'))
        self.assertEqual(2, len(profile.game_profiles)) # should have 2: global timed and indefinite
        self.assertEqual(1, qry.count()) # just to make sure
        gp_old = qry.get()

        check_global_timed_game()

        # assert creates new GameProfile
        qry = GameProfile.select().join(Game).where((GameProfile.profile == profile) & (Game.name == 'Global Timed'))
        self.assertEqual(1, qry.count())
        gp_new = qry.get()

        # but the ids should not be the same
        self.assertNotEqual(gp_old.id, gp_new.id)
