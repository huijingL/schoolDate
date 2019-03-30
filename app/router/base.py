from app import app

# from app.controller import baseController # 注意模块的导入,这是将一个模块整个导入
# newBase = baseController.baseController()  # 注意类的实例化

# from app.controller.baseController import baseController # 这是只导入一个类
# newBase = baseController()


from app.controller import * # 这里导入所有的模块，被vscode 坑了一把 ，垃圾编辑器
newBase = baseController.baseController()


@app.route('/')
def index():
    return newBase.index()
