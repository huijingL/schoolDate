from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app,resources=r'/*') # 解决跨域问题，这里的解释是允许所有的域名访问
from app.router import *
