from flask import jsonify  # 用于向前端返回Json数据

class baseController():
    def __init__(self):
        print(123)

    def index(self):
        dict = {"want":"小姐姐"}
        return jsonify(dict)
        