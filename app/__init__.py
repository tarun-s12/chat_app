from flask import Flask 

from .events import handle_connect, handle_name, handle_new_message
from .routes import main
from .extensions import socket

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = 'secret'

    app.register_blueprint(main)

    socket.init_app(app)

    return app