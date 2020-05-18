# query for leaderboard (inactive)

from datetime import datetime, timedelta
from decimal import Decimal

import pytz
from werkzeug.exceptions import BadRequest
from db import db, Game, Profile, GameCoin, Coin, GameProfile, GameProfileCoin, Ticker


# @db.atomic()
# def get_username_by_game_id(game_id)

# 	user_names = [game_profile.profile.username for game_profile in GameProfile.select().join(Profile).where(GameProfile.game == game_id)]

#     return user_names

# @db.atomic()
# def get_cash_by_game_id_and_profile_id(pofile_id, game_id)

# 	user_cash = GameProfile.select().where(GameProfile.game == game_id & GameProfile.profile == profile_id)

# 	return user_cash

@db.atomic()
def get_game_profile_by_game_id(game_id):
	return GameProfile.selcet(profile).where(GameProfile.game == game_id)

@db.atomic()
def get_user_name_by_profile_id(profile_id):
	return Profile.select(username).where(Profile.id == profile_id)


@db.atomic()
def get_user_coins_by_game_profile_id(gameprofile_id):
	return GameProfileCoin.select().where(gameprofile_id == GameProfileCoin.game_profile)

@db.atomic()
def get_ticker_price_by_coin_id(coin_id):
	return Ticker.select(Ticker.price).where(coin_id == Ticker.coin)
