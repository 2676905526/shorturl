from flask import Blueprint,jsonify
from utils import DouyinSpider

spider = DouyinSpider()

api = Blueprint('api', __name__)


@api.route('/test', methods=['GET'])
def loadmore():
    # res = spider.
    return "sd"
