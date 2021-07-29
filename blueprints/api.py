from flask import Blueprint
from time import sleep
from . import api_result

api = Blueprint('api_server', __name__)

@api.route('/numbers', methods=['GET'])
@api_result
def numbers():
    raise Exception('You was fucked up')
    sleep(2)
    return [1,2,3,4,5,6]

