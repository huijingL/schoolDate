from flask import Flask,request
from flask_cors import CORS
from datetime import timedelta
from flask_mongoalchemy import MongoAlchemy


app = Flask(__name__)
CORS(app,resources=r'/*') # 解决跨域问题，这里的解释是允许所有的域名访问
app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] =timedelta(seconds=1)

# app.config['MONGOALCHEMY_SERVER'] = 'mongodb://localhost'
app.config['MONGOALCHEMY_DATABASE'] = 'myFlask'
db = MongoAlchemy(app)

from app.router import *
