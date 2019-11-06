
# Flask�̳�

## 1����װ��
```python
pip install flask  # cmd
import flask    # python
```
## 2����һ������
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
��4�У�����Flask�࣬Flask��ʵ����һ��WSGIӦ��
��5�У�app��Flask��ʵ���������հ�����ģ���������Ϊ��������һ�㶼�Ǵ���__name__��
    ��flask.helpers.get_root_path����ͨ�������������ȷ������ĸ�Ŀ¼���Ա��þ�̬�ļ���ģ���ļ���Ŀ¼��
��7~9�У�ʹ��app.routeװ�����ὫURL��ִ�е���ͼ�����Ĺ�ϵ���浽app.url_map�����ϡ�
    ����URL����ͼ�����Ĺ�ϵ�ĳ������·�ɣ��������ͼ��������hello_world��
��11�У�ʹ������жϿ��Ա�֤�������ļ���������ļ���ʱ�����硰from hello import app��������ִ������ж��ڵĴ��룬Ҳ���ǲ���ִ��app.run������
��12�У�ִ��app.run�Ϳ������������ˡ�Ĭ��Flaskֻ����������ı���127.0.0.1�����ַ���˿�Ϊ5000��
    �����Ƕ���������Ķ˿�ת���˿���9000��������Ҫ�ƶ�host��port������0.0.0.0��ʾ�������е�ַ�������Ϳ����ڱ��������ˡ�
    �����������󣬻����werkzeug.serving.run_simple������ѯ��Ĭ��ʹ�õ����̵��̵߳�werkzeug.serving.BaseWSGIServer��������
    ʵ���ϻ���ʹ�ñ�׼��BaseHTTPServer.HTTPServer��ͨ��select.select��0.5��ġ�while TRUE�����¼���ѯ��
    �����Ƿ��ʡ�http://127.0.0.1:9000/��,ͨ��app.url_map�ҵ�ע��ġ�/�����URLģʽ,���ҵ��˶�Ӧ��hello_world����ִ�У����ء�hello world!��,״̬��Ϊ200��
    �������һ�������ڵ�·��������ʡ�http://127.0.0.1:9000/a��,Flask�Ҳ�����Ӧ��ģʽ���ͻ�����������ء�Not Found����״̬��Ϊ404
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

