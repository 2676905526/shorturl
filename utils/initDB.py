from utils import SqlHelper


DB_FILE_PATH = r'data/shorturl.db'

class initDB(object):
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        DB = SqlHelper.Connect(DB_FILE_PATH)
        DB.table('shortURL').create({
            'id': 'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
            'shortID': 'TEXT NOT NULL',
            'longUrl': 'TEXT NOT NULL',
            'shortUrl': 'TEXT NOT NULL',
            'creatTime': 'varchar(24) NOT NULL'
        })
        if DB.table('soup').count('id')==0:
            file = open('data/soup.txt','r',encoding='utf-8')
            ls = file.readlines()
            DB.table('soup').create({
                'id': 'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                'text': 'TEXT NOT NULL',
            }, insert=[{'text': item} for item in ls])
        DB.close()
    
db = initDB()