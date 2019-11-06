from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
import json

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return redirect(url_for('Add'))

@app.route('/Add', methods=['GET','POST'])
def Add():
    if request.method == 'POST':
        a = request.form['adder1']
        b = request.form['adder2']
        a = int(a)
        b = int(b)
        c = a + b
        return render_template('index.html', message=str(c))
    return render_template('index.html')

@app.route('/echart01', methods=['GET','POST'])
def Echart01():
    # return render_template('html_echart_001.html')

    aa = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
    xiaoliang = [5,20,36,10,10,20]
    chengben = [5,20,36,10,10,20]
    return render_template('html_echart_001.html', aa=aa, xiaoliang=xiaoliang, chengben=chengben, ensure_ascii=False)

@app.route('/echart01_data')
def get_data():
    aa = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
    xiaoliang = [5,20,36,10,10,20]
    chengben = [5,20,36,10,10,20]
    return json.dumps({'aa':aa, 'xiaoliang':xiaoliang, 'chengben':chengben},
                      ensure_ascii=False)    #如果有中文的话，就需要ensure_ascii=False

@app.route('/echart02', methods=['GET','POST'])
def Echart02():
    return render_template('html_echart_002.html')

@app.route('/echart03', methods=['GET','POST'])
def Echart03():
    return render_template('html_echart_003.html')

@app.route('/web01', methods=['GET','POST'])
def web01():
    return render_template('web01.html', title='测试', message=url_for('Add'))

# 错误时，返回指定界面
@app.errorhandler(404)
def miss(e):
    return render_template('index.html'), 404

@app.errorhandler(500)
def error(e):
    return render_template('index.html'), 500

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8081)
    # context = ('../zhengshu/1_bundle.crt', '../zhengshu/2_key.key')
    # app.run(host="0.0.0.0", port=8080, threaded=True, ssl_context=context)