import re,time,urllib,random
from unittest import result
from flask import Blueprint,jsonify, request
from utils import SqlHelper,s64,getSoup
from urllib.parse import urlparse

api = Blueprint('api', __name__)


@api.route('/', methods=['GET'])
def loadmore():
    # url = request.values.get("url")
    host = f"{urlparse(request.host_url).scheme}s://{urlparse(request.host_url).netloc}/"
    url = urllib.parse.unquote(request.url.split("url=")[-1])
    if url == request.url:
        return jsonify({"code": 400, "msg": "请输入URL"})
    pattern = r'^(http|https|ftp|file)?:/{2}\w.+$'
    result = re.match(pattern, url)
    if result:
        DB_FILE_PATH = r'data/shorturl.db'
        shortDB = SqlHelper.Connect(DB_FILE_PATH)
        longURL = result[0]
        urlQuery = shortDB.table('shortURL').where(f"longUrl = '{longURL}'").find()
        if len(urlQuery) > 0:
            data = {'shortID': urlQuery[0]["shortID"], 'longUrl':  urlQuery[0]["longUrl"],"shortUrl": f'{host}{urlQuery[0]["shortID"]}','creatTime':  urlQuery[0]["creatTime"]}
            return jsonify({"code": 200, "msg": "URL已存在","data": data })
        shortID = s64(int(time.time()))
        data = {'shortID': shortID, 'longUrl': longURL,"shortUrl":f'{host}{shortID}','creatTime': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}
        shortDB.table("shortURL").add(data)
        shortDB.close()
        return jsonify({
            "code": 200, 
            "msg": "短链接创建成功!", 
            "data": data
        })
    return jsonify({"code": 400, "msg": "URL格式错误"})



@api.route('/soup', methods=['GET'])
def soup():
    result = getSoup()
    return jsonify(result)
    

