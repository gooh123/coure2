from flask import Flask


def create_app():
    app = Flask(__name__)

    from utils2 import main_blueprint
    app.register_blueprint(main_blueprint)

    from api.routes import api_bp
    app.register_blueprint(api_bp, urlprefix='/api')

    return app
