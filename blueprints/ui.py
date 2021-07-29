from flask import Blueprint

ui = Blueprint('static_server', __name__, static_folder='../static')

@ui.route('/', methods=['GET'])
def index():
    return ui.send_static_file('index.html')

