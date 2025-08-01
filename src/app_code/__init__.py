from flask import Flask
from src.app_code.db import init_app as init_db_app
from src.app_code.views import bp as main_bp
from src.app_code.api import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)

    init_db_app(app)

    return app
