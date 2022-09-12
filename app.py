from flask import Flask
from routes import *
from utils import config


app = Flask(__name__,template_folder='views',static_url_path='',static_folder='views/static')
app.config.from_object(config)
  
  
  
app.register_blueprint(route, url_prefix='/')             # 注册rpute
app.register_blueprint(api, url_prefix='/api')            # 注册api


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)