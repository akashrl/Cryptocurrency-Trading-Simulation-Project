import flask
import traceback

from flask import Flask 
from flask_cors import CORS

from auth.routes import auth_bp
from errors.handlers import errors_bp
from db import * # FIXME get rid of * when you have db migrations
app = Flask(__name__)

def create_app():
    db.create_tables([Profile, AuthToken, Game, GameProfile, Coin, GameCoin,
        Ticker, Trade, GameProfileCoin])
    # FIXME get rid of this when you have db migrations
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

    @app.route('/')
    def hello():
        return 'hello world'

    return app
