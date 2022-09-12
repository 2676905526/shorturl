import random 
from utils import SqlHelper

DB_FILE_PATH = r'data/shorturl.db'

table = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZαβ"
def s64(n: int):
    s = bin(n)[2:]
    if j := (h := len(s)) % 6:
        s = "0" * j + s
    return "".join([table[int(s[i : i + 6][::-1], 2)] for i in range(0, h, 6)])


def getSoup():
    DB_FILE_PATH = r'data/shorturl.db'
    DB = SqlHelper.Connect(DB_FILE_PATH)
    count = DB.table('soup').count('id')
    text = DB.table('soup').where(f'id = {random.randint(0,count)}').find()[0]
    text['text'] = text['text'].replace("\n","")
    DB.close()
    return {"code": 200, "data": text}