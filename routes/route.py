from flask import Blueprint,redirect,url_for,render_template,request
from utils import SqlHelper, getSoup
from urllib.parse import urlparse
import time 



route  = Blueprint('route', __name__)


@route.route('/', methods=['GET'])
def index():
    soup = getSoup()
    year = time.strftime('%Y', time.localtime())
    index = f"{urlparse(request.host_url).scheme}s://{urlparse(request.host_url).netloc}/"
    return render_template("index.html",soup=soup,year=year,index=index)


@route.route('/<shortID>', methods=['GET'])
def redirectUrl(shortID):
    DB_FILE_PATH = r'data/shorturl.db'
    shortDB = SqlHelper.Connect(DB_FILE_PATH)
    urlQuery = shortDB.table('shortURL').where(f"shortID = '{shortID}'").find()
    shortDB.close()
    if len(urlQuery) > 0:
        return redirect(urlQuery[0]['longUrl'])
    return redirect(url_for('route.index'))

