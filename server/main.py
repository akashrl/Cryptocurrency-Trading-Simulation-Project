import flask
import traceback

from flask import Flask 
from flask_cors import CORS

from auth.routes import auth_bp
from errors.handlers import errors_bp
from game.routes import game_bp
from db import * # FIXME get rid of * when you have db migrations

def create_app():
    db.create_tables([Profile, AuthToken, Game, GameProfile, Coin, GameCoin,
        Ticker, Trade, GameProfileCoin])
    try:
        Coin.create(name='Bitcoin', symbol='BTC')
        Coin.create(name='Ethereum', symbol='ETH')
        Coin.create(name='Litecoin', symbol='LTC')
        Coin.create(name='Coin 3', symbol='CO3')
        Coin.create(name='Coin 4', symbol='CO4')
        Coin.create(name='Coin 5', symbol='CO5')
    except:
        pass
    # FIXME get rid of this when you have db migrations
    app = Flask(__name__)
    CORS(app)

    @app.before_request
    def before_request():
        db.connect(reuse_if_open=True)
        #pass

    @app.after_request
    def after_request(res):
        db.close()
        return res

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(errors_bp)
    app.register_blueprint(game_bp)

    @app.route('/')
    def hello():
        return 'hello world'

    return app
