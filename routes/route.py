from flask import Blueprint


route  = Blueprint('route', __name__)


@route.route('/', methods=['GET'])
def index():
    return "index"