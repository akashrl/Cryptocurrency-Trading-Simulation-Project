from flask import Blueprint, request, jsonify
import os
import secrets
from uuid import uuid4
import string
import random
from werkzeug.exceptions import BadRequest
import pytz

from auth.decorators import require_authentication
from db import Game, GameProfile, Coin, GameCoin, db

from .services import (
	get_username_by_game_id,
)

from .serializers import (
	UserNameScoreResponse,
)

leaderboard_bp = Blueprint('leaderboard', __name__, url_prefix='/leaderboard')

@leaderboard_bp.route('/', methods=['GET'])
@require_authentication
def get_users_and_user_cashs(game_id):

	gameProfiles = get_game_profile_by_game_id(game_id)
	user_names = [get_user_name_by_profile_id(gameProfile.profile) for gameProfile in gameProfils]
	user_cashs = [gameProfile.cash for gameprofile in gameProfiles]
	user_coins = [get_user_coins_by_game_profile_id(gameProfile.profile) for gameProfile in gameProfiles]
	for user_coin in user_coins:
		coin_price = 0
		for coin_id in user_coin:
			coin_price += coin_id.amount*get_ticker_price_by_coin_id(coin_id.coin) 
		coin_prices.append(coin_price)
	user_scores = coin_prices + user_cashs

	return  jsonify(UserNameScoreResponse.serialize({
		"username" : user_names,
		"userscores" : user_scores
		}))                 