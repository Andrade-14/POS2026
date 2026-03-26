from flask import Flask
from .routes.messages import messages_bp
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(messages_bp, url_prefix="/messages")

    return app