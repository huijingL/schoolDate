from flask import jsonify  # 用于向前端返回Json数据
# from app.model import *
import importlib   # 动态加载模块
import json


class baseController():
    def __init__(self):
        print(123)

    def index(self):
        dict = {"want":"小姐姐"}
        return jsonify(dict)


    def saveData(self,model,query):
        print(model,query)
        # 动态的导入模块
        module = importlib.import_module('app.model.'+model)
        # 动态的加载模块内部的方法
        # ** 是dict 的解包，相当于 username= ,password =
        try:
            getattr(module, model)(**query).save() # 增
            items = getattr(module, model).query.filter(query).all() # 查
            rows = []
            for item in items:
                row = item.to_json()
                rows.append(row)
            print(rows)
            data = {'error': 0,'rows':rows}
        except ImportError:
            data = {'error': 401}
        return jsonify(data)