from flask import Flask
from blueprints import ui, api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(ui, url_prefix="/")
    app.register_blueprint(api, url_prefix="/api/v1/")
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    return app