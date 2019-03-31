from flask import jsonify  # 用于向前端返回Json数据
# from app.model import *
import importlib   # 动态加载模块


class baseController():
    def __init__(self):
        print(123)

    def index(self):
        dict = {"want":"小姐姐"}
        return jsonify(dict)


    def saveData(self,model,query):
        print(model,query)
        # 动态的导入模块
        data = importlib.import_module('app.model.'+model)
        # 动态的加载模块内部的方法
        getattr(data, model)(username=query['username'],password=query['password']).save()
        # data.sys_user(username=query['username'],password=query['password']).save()
