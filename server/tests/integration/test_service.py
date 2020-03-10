from decimal import Decimal
import os
from unittest.mock import patch, Mock, MagicMock

from db import Ticker, Coin
from scripts.service import ping
from tests.utils import DbTest


class TestService(DbTest):
    @patch('requests.get', MagicMock(return_value=Mock(json=lambda: [
        # NOTE these must be actual coins defined in the migrations!
        {'symbol': 'BTC', 'price': '56.12345678'},
    ])))
    def test_parsing_with_one_coin(self):
        os.environ['NOMICS_BASE_URL'] = 'foo'
        ping('BTC')
        btc = Coin.get(Coin.symbol == 'BTC')
        btc_ticker = Ticker.get(Ticker.coin == btc)
        self.assertEqual(btc_ticker.price, Decimal('56.12345678'))

    @patch('requests.get', MagicMock(return_value=Mock(json=lambda: [
        # NOTE these must be actual coins defined in the migrations!
        {'symbol': 'BTC', 'price': '56.12345678'},
        {'symbol': 'ETH', 'price': '42.98765432'},
    ])))
    def test_parsing_with_many_coins(self):
        os.environ['NOMICS_BASE_URL'] = 'foo'
        ping('BTC', 'ETH')
        btc = Coin.get(Coin.symbol == 'BTC')
        eth = Coin.get(Coin.symbol == 'ETH')
        btc_ticker = Ticker.get(Ticker.coin == btc)
        eth_ticker = Ticker.get(Ticker.coin == eth)
        self.assertEqual(btc_ticker.price, Decimal('56.12345678'))
        self.assertEqual(eth_ticker.price, Decimal('42.98765432'))

