from app import app,request

# from app.controller import baseController # 注意模块的导入,这是将一个模块整个导入
# newBase = baseController.baseController()  # 注意类的实例化

# from app.controller.baseController import baseController # 这是只导入一个类
# newBase = baseController()


from app.controller import * # 这里导入所有的模块，被vscode 坑了一把 ，垃圾编辑器
newBase = baseController.baseController()


@app.route('/')
def index():
    return newBase.index()


# 通过<> 拿到参数， 类似于 node 的 : , 拿到的是params
# 对<> 内的数据可以进行数据的控制例如 <int: > 设置 数据必须为int
@app.route('/show')
def show():
    return '我想要一个小姐姐'
#  拿到的数据需要传到方法里面，才能被使用

@app.route('/api/v1/schema/<model>/')
def show_model(model):
    # print(model,request.args.to_dict())
    newBase.saveData(model,request.args.to_dict())
    return '我想要一个小姐姐，她最好是个大长腿'