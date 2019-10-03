
# Flask教程

## 1、安装包
```python
pip install flask  # cmd
import flask    # python
```
## 2、第一个程序
####  hello.py
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello world!</h1>'

@app.route('/user/<name>')
def index():
    return '<h1>hello %s!</h1>'%(name)

if __name__ == '__main__':
    app.run(debug = True)
    
'''
第4行，引入Flask类，Flask类实现了一个WSGI应用
第5行，app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递__name__。
    让flask.helpers.get_root_path函数通过传入这个名字确定程序的根目录，以便获得静态文件和模板文件的目录。
第7~9行，使用app.route装饰器会将URL和执行的视图函数的关系保存到app.url_map属性上。
    处理URL和视图函数的关系的程序就是路由，这里的视图函数就是hello_world。
第11行，使用这个判断可以保证当其他文件引用这个文件的时候（例如“from hello import app”）不会执行这个判断内的代码，也就是不会执行app.run函数。
第12行，执行app.run就可以启动服务了。默认Flask只监听虚拟机的本地127.0.0.1这个地址，端口为5000。
    而我们对虚拟机做的端口转发端口是9000，所以需要制定host和port参数，0.0.0.0表示监听所有地址，这样就可以在本机访问了。
    服务器启动后，会调用werkzeug.serving.run_simple进入轮询，默认使用单进程单线程的werkzeug.serving.BaseWSGIServer处理请求，
    实际上还是使用标准库BaseHTTPServer.HTTPServer，通过select.select做0.5秒的“while TRUE”的事件轮询。
    当我们访问“http://127.0.0.1:9000/”,通过app.url_map找到注册的“/”这个URL模式,就找到了对应的hello_world函数执行，返回“hello world!”,状态码为200。
    如果访问一个不存在的路径，如访问“http://127.0.0.1:9000/a”,Flask找不到对应的模式，就会向浏览器返回“Not Found”，状态码为404
'''
```
```python
from flask import request

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s' % user_agent
```
```python
from hello import app 
from flask import current_app
current_app.name 
app_ctx = app.app_context()
app_ctx.push()
current_app.name
app_ctx.pop()
```

