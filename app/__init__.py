from flask import Flask
from .db import init_app as init_db_app
from .views import bp as main_bp
from .api import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)

    init_db_app(app)

    return app
