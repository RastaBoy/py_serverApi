from functools import wraps
from flask import jsonify

def api_result(func):
    
    @wraps(func)
    def formatter(*args, **kwargs):
        result = dict()
        try:
            result['result'] = True
            result['data'] = func(*args, **kwargs)
        except Exception as e:
            result['result'] = False
            result['error'] = str(e)
        return jsonify(result)
    
    return formatter


from .ui import ui
from .api import api